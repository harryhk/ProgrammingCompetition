#!/usr/bin/env python 

import sys
import itertools 


_debug=0

class Problem(object):
    
    def __init__(self, nSeq):
        # Give number of sequences, read the rest of lines 
        self.nSeq = nSeq
        self.seqs = [] 
        for i in range(nSeq):
            tmp = sys.stdin.readline()
            self.seqs.append( tmp.strip()  )
        
        tmp= sys.stdin.readline()
        self.nQuery = int( tmp.strip() ) 
        self.query = []
        for i in range(self.nQuery):
            tmp = sys.stdin.readline()
            # adjust index starting from 0
            self.query.append( int(tmp.strip() ) -1 )

    def solv(self):
        # range of length of seq align
        nMin = max( [ len(i)  for i in self.seqs ]  )
        nMax = sum( [ len(i)  for i in self.seqs ]  ) 

        totalAlign={}
        

        for alignLen in range( nMin, nMax+1 ):
            #totalAlign[alignLen] = self.fixLenAlign( alignLen )
            
            alignTupleFixLen = []
            for seq in self.seqs: 
                alignTupleFixLen.append( self.fixLenAlign( seq  , alignLen  ) )

            if _debug:
                print alignTupleFixLen

            # create combination of different sequences 


            totalAlign[alignLen] = self.combinationSeqs( alignTupleFixLen, alignLen  )

        # sort totalAlign
        for i in totalAlign.keys():
            totalAlign[i].sort( self.mycomp )

    
        # cat totalAlign
        sortedAlign = []
        for i in  sorted( totalAlign.keys() )  :
            sortedAlign = sortedAlign + totalAlign[i]

        print "Possible Alignments:", len(sortedAlign)

        for i in self.query:
            if i< 0 or i >= len(sortedAlign) :
                print "There is no alignment at position:", i+1
            else:
                print "Alignment at Position:", i+1
                tmp = sortedAlign[i]
                for i in tmp:
                    print i.replace('{','-')



    def mycomp(self, l1, l2):
        # customized compare l1, l2 two alignments
        # same len already
        
        for i in range(self.nSeq):
            if l1[i] != l2[i]:
                return cmp(l1[i], l2[i])



    def combinationSeqs(self, alignTuple , alignLen ):
        # alignTuple : each tuple are filled '{' for each seq 
        
        combinations = []
        # get first two seqs 
        if self.nSeq < 2 :
            print >> sys.stderr,  "seq < 2 "

        combinations = [ [i, j ] for i in alignTuple[0] for j in alignTuple[1]   ]

        if _debug:
            print combinations

        if self.nSeq > 2 :
            for i in range(2, self.nSeq):

                tmp = [  ii1+[ii2]    for ii1 in combinations for ii2 in alignTuple[i ]  ]

                combinations = tmp 

        if _debug:
            print combinations

        return self.removeDup(combinations, alignLen)

         
    
    def removeDup(self, combinations , fixlen):
        final = []
        for combi in combinations: 
            flag = True
            for i in range( fixlen ):
                c= 0 
                for j in combi : 
                    if j[i] == '{':
                        c = c+1

                if c == self.nSeq:
                    flag = False
                    break
        
            if flag:
                final.append(combi)

        return final


        
    
    def fixLenAlign(self, seq,  fixLen):
        # aligned seq given a fixed length

        alignChar = '{'
        alignEachSeq = []

        lenSeq = len(seq) 
        nslots = lenSeq +1 

        if _debug:
            print fixLen , lenSeq

        if fixLen == lenSeq:
            alignEachSeq.append(seq)
            return alignEachSeq


        for spacePos  in itertools.combinations_with_replacement( range(nslots), fixLen - lenSeq  ):
            # spacePos is tuple indicate insert '{' position 
            
            insertIdx = [ 0 for _ in range(nslots)  ]
            for i in  spacePos:
                insertIdx[i] +=1 
            
            tmp = ''
            for i in range(nslots):
                tmp = tmp +  alignChar * insertIdx[i]  
                if i < lenSeq:
                    tmp = tmp + seq[i]

            alignEachSeq.append( tmp )
            

        return alignEachSeq

                        

            


    def p(self):
        print self.__dict__


if __name__ == '__main__':
    
    line=sys.stdin.readline()
    while line:
        numSeq = int( line.strip() ) 
        prob = Problem(numSeq)
        if _debug:
            prob.p()
        prob.solv()

        line = sys.stdin.readline()
        
