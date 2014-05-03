import sys
import pdb

class Case(object):
    def __init__(self, curr_chests, avail_keys ):
        self.curr_chests = curr_chests
        self.avail_keys  = avail_keys
        self.keys_left  = tot_keys.copy()
        for i in self.avail_keys:
            if self.keys_left.has_key(i) :
                if self.keys_left[i] > 0:
                    self.keys_left[i] -= 1 

        for i in self.curr_chests:
            if self.keys_left[ chests_opened_by_keys[i] ] >0 :
                self.keys_left[ chests_opened_by_keys[i] ] -=1
    
    def __eq__(self, other):
        return self.keys_left == other.keys_left
    
    def __lt__(self, other):
        return self.curr_chests < other.curr_chests

    def __repr__(self):
        return "curr_chests %s : avail_keys %s , keys_left %s" % ( self.curr_chests.__repr__(), self.avail_keys.__repr__() , self.keys_left.__repr__())


def solve():
    roundi_1 = []
    for key_id in set(keys_sets):
        for chest_id in keytyps_open_chests[key_id] if keytyps_open_chests.has_key(key_id) else [] :
            new_key_sets = keys_sets[:]
            new_key_sets.remove( key_id )
            new_key_sets += chests_has_keys[chest_id]
            
            tmp_case = Case([chest_id] , new_key_sets )
            try:
                tmp_idx = roundi_1.index(tmp_case)
                if tmp_case < roundi_1[tmp_idx]:
                    roundi_1[tmp_idx] = tmp_case  
                else:
                    continue
            except ValueError:
                roundi_1.append(tmp_case)
                    
    
    
    for _ in range(1, chests):
    
        round_i=[]
        for case in roundi_1:
            for akeys in set(case.avail_keys):
                for chest_candid in keytyps_open_chests[akeys] if keytyps_open_chests.has_key(akeys) else []:
                    
                    if chest_candid not in case.curr_chests:
                        tmp_chest =  case.curr_chests[:]
                        tmp_chest.append( chest_candid )
                        
                        new_keys = case.avail_keys[:]
                        new_keys.remove( akeys )
                        new_keys += chests_has_keys[ chest_candid ]
                        
                        tmp_case = Case( tmp_chest, new_keys  ) 
                        # test if tmp_chest existed in round_i 
                        try:
                            tmp_idx = round_i.index(tmp_case)
                            if tmp_case < round_i[tmp_idx ]:
                                round_i[tmp_idx] = tmp_case
                            else:
                                continue
                                
                        except ValueError:
                            round_i.append( tmp_case )
                        
        roundi_1 = round_i[:] 

    return roundi_1

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
    

    tot_keys={}
    for _ in chests_opened_by_keys.values():
        try:
            tot_keys[ _ ] +=1
        except KeyError:
            tot_keys[_] =1 
    #pdb.set_trace()
    
    solution= solve()
    if solution:
        solution = sorted( [  _.curr_chests  for _ in solution  ] )[0]
        solution = ' '.join( [ str(_+1) for _ in solution ] )
    else:
        solution = "IMPOSSIBLE"

    print "Case #%d: %s" %( i+1, solution )
    
    
