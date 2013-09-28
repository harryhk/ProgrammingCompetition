import sys,pdb
import networkx as nx


def explore(u, pre):
    pre.append(u)
    
    if len(nx.neighbors(G,u)) == 0:
        Leafs[u]=set(pre)
        return

    for v in nx.neighbors(G, u):
        explore(v, pre[:])

def pick(candidate, workout_sofar, final_workout):
    pick_id=0
    max_score= -1
    if len(candidate) == 0:
        sys.stderr.write( "candidate none\n")
        exit(1)
    #pdb.set_trace()
    for i in candidate:
        tmp_gain = sum([ G.node[j]['v'] for j in Leafs[i].difference(workout_sofar)  ])
        if tmp_gain > max_score:
            max_score = tmp_gain 
            pick_id = i
    # pick tmp_id
    candidate.remove(pick_id)
    final_workout.append(pick_id)
    return workout_sofar.union( Leafs[pick_id] )

f=open(sys.argv[1])
N = int(f.readline())
for _ in range(N):
    n_wo, ndays = f.readline().split()
    n_wo, ndays = ( int(n_wo), int(ndays) )
    G = nx.DiGraph()
    Leafs={}
    for _ in range(n_wo):
        wid, wpid, wv = f.readline().split()
        (wid, wpid, wv) = ( int(wid), int(wpid), int(wv) )
        G.add_edge(wpid, wid)
        G.node[wid]['v']=wv

    explore(1, [])
    # greedy 
    # the first day
    workid_candidate =  Leafs.keys() 
    workouts_sofar= set([])
    final_workout=[]
    
    for _ in range(ndays):
        workouts_sofar = pick(workid_candidate, workouts_sofar, final_workout)

    for fwid in sorted(final_workout): 
        sys.stdout.write("%d " % fwid)
    print

        
