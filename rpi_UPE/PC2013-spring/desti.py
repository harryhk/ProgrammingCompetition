import networkx as nx
import sys

def solve( curr_city, edgetype  ):
    tmp ={}
    if len( curr_city.keys()) == 0:
        sys.stderr.write("curr city none\n")
        exit(1)

    for city in curr_city:
        for tovisit in G.edge[city]:
            if G.edge[city][tovisit].has_key( edgetype):
                tmp_cost = curr_city[city] + G.edge[city][tovisit][edgetype]
                if tmp.has_key(tovisit):
                    if tmp[tovisit] < tmp_cost:
                        tmp[tovisit] = tmp_cost
                else:
                    tmp[tovisit] = tmp_cost
    return tmp

f = open(sys.argv[1])
N_test = int(f.readline())

for _ in range( N_test ):
    G= nx.Graph()
    edge_guide=[]
    N_pair = int(f.readline())
    for _ in range(N_pair):
        u, v, t, c  = f.readline().strip().split()
        G.add_edge( u, v )
        G.edge[u][v][t]=int(c)

    
    start, n_trips = f.readline().strip().split()
    for _ in range(int(n_trips)):
        edge_guide.append(f.readline().strip())
    
    curr_city={}
    curr_city[start]=0
    
    for edgetype in edge_guide:
        #print curr_city
        curr_city = solve( curr_city, edgetype)
    
    
    print sorted( curr_city.items(), key=lambda x: x[1] )[-1][0]
