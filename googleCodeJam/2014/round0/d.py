import sys 

f = open( sys.argv[1]) 

N = int( f.readline().strip() ) 

for ncase in range(1, N+1):
    
    blocks = int( f.readline().strip() ) 
    naomi = map( float, f.readline().strip().split() ) 
    ken = map( float, f.readline().strip().split() ) 

    naomi.sort()
    ken.sort()

    # war 
    jdx=0
    cken = 0 
    for i in naomi:
        
        while jdx < blocks:
            if ken[jdx] < i :
                jdx += 1 
            else:
                cken +=1 
                jdx += 1 
                break 

        if jdx == blocks:
            break 

    # deceive war 

    jdx=0
    cmiao = 0 
    for i in ken:
        
        while jdx < blocks:
            if naomi[jdx] < i :
                jdx += 1 
            else:
                cmiao +=1 
                jdx += 1 
                break 

        if jdx == blocks:
            break 

    print "Case #%d: %d %d" % (ncase, cmiao, blocks - cken ) 
