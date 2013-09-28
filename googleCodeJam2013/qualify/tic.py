import sys 

def judge(line):
    d={}
    for i in 'XO.T':
        d[i]=0
    for i in line:
        d[i] += 1
    
    if d['O'] ==4 or d['O'] + d['T'] == 4:
        return 'O'
   
    if d['X'] ==4 or d['X'] + d['T'] == 4:
        return 'X'
        
    return None 


def solve(game):
    status = None
    complete = 1 
    # test raw and column
    test_cases = []
    for i in range(4):
        col = ''
        for j in range(4):
            col +=  game[j][i] 
        test_cases.append(game[i])
        test_cases.append(col)

    di = ''
    di_1 =''
    for i in range(4):
        di += game[i][i]
        di_1 += game[i][3-i]
    test_cases.append(di)
    test_cases.append(di_1)

    for line in game:
        if '.' in line:
            complete =0
            break

    for i in test_cases:
        status = judge(i)
        if status == 'X':
            return "X won"
        if status == 'O':
            return "O won"
    
    if status == None and complete == 0:
        return "Game has not completed"
    if status == None and complete == 1:
        return "Draw"

f = open(sys.argv[1])
N = int(f.readline())

for i in range(N):
    game = []
    for _ in range(4):
        game.append( f.readline().strip() )
    
    #print game
    print "Case #%d: %s" %( i+1, solve(game) )  
    f.readline()
