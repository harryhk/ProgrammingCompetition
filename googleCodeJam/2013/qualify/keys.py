import sys 

def could_open( keys_sets, keytyps_open_chests ):
    tmp =[]
    for i in set(keys_sets):
        try:
            tmp += keytyps_open_chests[i]
        except KeyError:
            pass

    return sorted(tmp)

def solve(keys_sets, chests_has_keys , chests_opened_by_keys,keytyps_open_chests, path):

    if len(path) == chests:
        return path
    
    chest_candid = could_open( keys_sets, keytyps_open_chests  )

    for i in chest_candid:
        if i not in path:
            new_path = path[:]
            new_path.append(i)
            
            new_keys_sets = keys_sets[:]
            new_keys_sets.remove(chests_opened_by_keys[i])
            new_keys_sets += chests_has_keys[i]
            solution =  solve( new_keys_sets, chests_has_keys, chests_opened_by_keys, keytyps_open_chests, new_path )
            if solution == None:
                continue
            if len(solution) == chests:
                return solution
        
    return None
    
    

f = open(sys.argv[1])
N = int(f.readline())

for i in range(N):
    keys, chests = f.readline().split()
    keys, chests = ( int(keys), int(chests)  )

    keys_sets = f.readline().split()
    keys_sets = [int(_) for _ in keys_sets]

    chests_has_keys={}
    keytyps_open_chests={}
    chests_opened_by_keys={}
    for chests_id in range(chests):
        tmp = f.readline().split()
        tmp = [ int(_) for _ in tmp ]
        if keytyps_open_chests.has_key(  tmp[0] ):
            keytyps_open_chests[ tmp[0] ].append(chests_id)
        else:
            keytyps_open_chests[tmp[0]] = [ chests_id ]
        chests_opened_by_keys[chests_id] = tmp[0]
        chests_has_keys[chests_id] = tmp[2:]
    
    #print keys_sets, chests_has_keys, chests_opened_by_keys, keytyps_open_chests
    if i==2:
        print keys_sets
        print chests_has_keys
        print chests_opened_by_keys
        print keytyps_open_chests
        break
    
    solution= solve(keys_sets, chests_has_keys, chests_opened_by_keys, keytyps_open_chests , [])

    if solution == None:
        solution = "IMPOSSIBLE"
    elif len(solution) ==chests:
        solution = ' '.join([str(_+1) for _ in solution])
    else:
        sys.stderr.write("wrong\n")
    
    print "Case #%d: %s" %( i+1, solution )
    
    
