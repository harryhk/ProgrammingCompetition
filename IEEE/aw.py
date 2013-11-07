#!/usr/bin/env python 


import sys

from string import maketrans

_debug = 0

class Prob(object):
    def __init__(self, n ) :
        self.dictionary = []
        self.dictFixLen ={}
        for i in range(n):
            item = sys.stdin.readline().strip()
            itemLen = len(item)
            self.dictionary.append( item ) 
            if len(item) not in self.dictFixLen:
                self.dictFixLen[itemLen] = [ item ]
            else:
                self.dictFixLen[itemLen].append(item)

        tmp = sys.stdin.readline()

        self.encryOrig = sys.stdin.readline().strip().lower()

        self.encry = self.encryOrig.split()

    
    def solv(self):
        # freq count for dictionary 
        self.dictCharFreq = {}
        self.encryCharFreq = {}


        for i in self.dictionary:
            for idx in range( len(i)  ) :
                for idx2 in range( idx+1, len(i) +1  ):
                    w = i[idx: idx2]
                    if self.dictCharFreq.has_key(w):
                        self.dictCharFreq[w] +=1
                    else:
                        self.dictCharFreq[w] = 1
        
        for i in self.encry:
            for idx in range( len(i)  ) :
                for idx2 in range( idx+1, len(i) +1  ):
                    w = i[idx: idx2]
                    if self.encryCharFreq.has_key(w):
                        self.encryCharFreq[w] +=1
                    else:
                        self.encryCharFreq[w] = 1
        
        if 0: # _debug:
            print sorted( [ i for i in  self.dictCharFreq.items() if len(i[0] ) ==1 ] , key = lambda x: -x[1] ) 
            print sorted( [ i for i in  self.encryCharFreq.items() if len(i[0] ) ==1 ], key = lambda x: -x[1] ) 

            print sorted( [ i for i in  self.dictCharFreq.items() if len(i[0] ) ==2 ] , key = lambda x: -x[1] ) 
            print sorted( [ i for i in  self.encryCharFreq.items() if len(i[0] ) ==2 ], key = lambda x: -x[1] ) 

        # create traslate table based on feq 
        tmp = sorted( [ i for i in  self.dictCharFreq.items() if len(i[0] ) ==1 ] , key = lambda x: -x[1] ) 
        orig = [ i[0] for i in tmp  ]

        tmp = sorted( [ i for i in  self.encryCharFreq.items() if len(i[0] ) ==1 ], key = lambda x: -x[1] ) 

        encry = [ i[0] for i in tmp  ]

        if 0 : #_debug:
            print zip(encry, orig)

        transTab = maketrans(''.join(encry), ''.join(orig) )

        # give best try
        print self.encryOrig.translate(transTab).upper()



        # 
        #self.temptedTransTab = [ ''.join(encry), ''.join(orig)  ]


        ## find one already in dictionary , believe them correct
        #self.transTabTrue = {}
        #
        #tmp_deci = [ ( i, i.translate(transTab) ) for i in self.encry ]
        #
        #tmp = {}
        #
        #self.encryNotYetSet = set() # store not yet done word
        #
        #for en, de in tmp_deci:
        #    if de in self.dictionary:
        #        for ii in range(len(en)):
        #            if en[ii] not in self.transTabTrue:
        #                self.transTabTrue[en[ii]] = de[ii]
        #    else:
        #        self.encryNotYetSet.add(de)
        #


        #while len(self.encryNotYetSet)> 0 and len( self.transTabTrue.keys() ) < len(self.encryCharFreq.keys() ):
        #    self.updateTransTable( )
        #    # find the most probable match and update transTabTrue


        #
        #print self.transTabTrue 
        #print self.encryOrig.translate(transTab)

    def updateTransTable(self  ):
        
        score={}
        for i in self.encryNotYetSet:
            # { encry: (sore, matchedDecry)  }
            score[i] = self.matchScore(i)

        # find best match and update transTabTrue and encryNotYetSet
        
        sortMatch = sorted( [ i for i in score.items() ] , cmp=self.mycmp )
        
        bestMatch = sortMatch[0]
        
        tmp_en = bestMatch[0]
        tmp_de = bestMatch[1][1]
        for idx in range(tmp_en):
            if tmp_en[idx] not in self.transTabTrue:
                self.transTabTrue[tmp_en[idx]] = tmp_de[idx]
                # also update tempated one
                en1 , de1 = self.temptedTransTab 
                de_idx = de1.find(tmp_de[idx])
                tmp = de1[de_idx]
                
                de1_tmp = [  _ for _ in de1 ]
                de1_tmp[de_idx] = de1_tmp[idx]
                de1_tmp[idx] = tmp
                self.temptedTransTab = [ en1, ''.join(de1_tmp) ]
    
    def matchScore(self):
        pass
    
    def mycmp(self, i, j ):
        if i[1][0] != j[1][0]:
            return -cmp(i[1][0], j[1][0])
        else:
            return -cmp( len(i[0]), len(j[0])  )

    def p(self):
        print self.__dict__


if __name__ == "__main__":

    line =  sys.stdin.readline()
    
    while line:
        
        n = int( line.strip() )
        prob = Prob(n)
        
        if _debug:
            prob.p()
        
        prob.solv()

        line = sys.stdin.readline()
    

