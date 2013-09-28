import networkx as nx


f = open('pass')
n = int( f.readline() ) 

for i in range(1):
    tot = int(f.readline().split()[0])
    G = nx.DiGraph()    
    for j in range(tot):
        fr = f.readline().strip()
        for jj in range(len(fr)):
            for jjj in range(jj+1, len(fr)):
                G.add_edge(fr[jj], fr[jjj])
   
    print ''.join(nx.topological_sort(G))

