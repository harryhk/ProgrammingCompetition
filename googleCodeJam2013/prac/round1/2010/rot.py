import sys, pdb
import numpy as np 

debug =0

class Board(object):
    def __init__(self, lines, n, k ):
        self.n , self.k = n, k
        
        self.board = np.array( [  [j for j in i.strip()]  for i in lines ] )
        

    def rotate(self):
        tmp = []
        for i in range( self.n) :
            tmp.append( self.board[:,i][::-1]  )

        self.board = np.array( tmp )
        
    def fall(self):
        tmp_col = []
        for i in range(self.n):
            tmp = self.board[:,i]
            tmp = ''.join(list(tmp) ) 
            tmp = tmp.replace('.', '')
            tmp = '.' * ( self.n- len(tmp) ) + tmp 
            tmp_col.append(tmp)
        
        
        new_board =[]
        for i in range(self.n):
            tmp = []
            for j in range(self.n):
                tmp.append( tmp_col[j][i])
            new_board.append(tmp)

        self.board = np.array(new_board)


    def win(self, c):
        win_string= c * self.k
        # check row:
        for i in range(self.n):
            tmp = ''.join(self.board[i,:])
            if tmp.find(win_string) != -1:
                return True

        # check col:
        for i in range(self.n):
            tmp = ''.join(self.board[:,i])
            if tmp.find(win_string) != -1:
                return True

        
        diags = [ self.board.diagonal(i) for i in range(-self.n+1, self.n )  ]
        diags.extend( [ self.board[:, ::-1].diagonal(i)  for i in range(-self.n+1, self.n) ] )

        if debug:
            pdb.set_trace()
        
        for i in diags:
            tmp = ''.join( i) 
            if tmp.find(win_string) !=-1:
                return True

        return False



fin = open(sys.argv[1])
cases = int( fin.readline() ) 

for case in range(cases) :
    
    n , k = map(int, fin.readline().split() ) 
    tmp = [] 
    for _ in range(n):
        tmp.append(  fin.readline().strip() ) 

    game = Board(tmp, n, k)
    game.rotate()
    game.fall()
    rwin = game.win('R')
    bwin = game.win('B')
    if rwin and bwin:
        solution = "Both"
    elif rwin:
        solution = 'Red'
    elif bwin:
        solution = 'Blue'
    else:
        solution = 'Neither'
    
    print "Case #%d: %s" %(case +1, solution)
