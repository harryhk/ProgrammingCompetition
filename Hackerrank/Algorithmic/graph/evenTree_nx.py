import networkx as nx

f = open('t')

N, ne = f.readline().split()
N= int(N)
ne= int(ne)
G=nx.Graph()

for i in range(ne):
    u,v = f.readline().split()
    G.add_edge( u,v )

#for i in G.nodes():
#    G.add_node(i, v=0, d=1)
#
#def explore(node):
#    G.node[node]['v']=1
#
#    for nn in G.neighbors(node):
#        if G.node[nn]['v'] == 0:
#            explore(nn)
#            G.node[node]['d'] += G.node[nn]['d']
#
#explore(G.nodes()[0])
#print len( [i for i in  nx.get_node_attributes(G,'d').values() if i%2==0 ] ) -1


