class Edge(object):
    def __init__(self, u, v, w):
        self.source = u
        self.sink = v
        self.capacity = w
    def __repr__(self):
        return "%s->%s:%s" % (self.source, self.sink, self.capacity)
 
class FlowNetwork(object):
    def __init__(self):
        self.adj = {}
        self.flow = {}
 
    def add_vertex(self, vertex):
        self.adj[vertex] = []
 
    def get_edges(self, v):
        return self.adj[v]
 
    def add_edge(self, u, v, w=1):
        if u == v:
            raise ValueError("u == v")
        edge = Edge(u,v,w)
        redge = Edge(v,u,0)
        edge.redge = redge
        redge.redge = edge
        self.adj[u].append(edge)
        self.adj[v].append(redge)
        self.flow[edge] = 0
        self.flow[redge] = 0
 
    def find_path(self, source, sink, path):
        if source == sink:
            return path
        for edge in self.get_edges(source):
            residual = edge.capacity - self.flow[edge]
            if residual > 0 and not (edge,residual) in path:
                result = self.find_path( edge.sink, sink, path + [(edge,residual)] ) 
                if result != None:
                    return result
 
    def max_flow(self, source, sink):
        path = self.find_path(source, sink, [])
        while path != None:
            flow = min(res for edge,res in path)
            for edge,res in path:
                self.flow[edge] += flow
                self.flow[edge.redge] -= flow
            path = self.find_path(source, sink, [])
        return max(self.flow[edge] for edge in self.get_edges(source))



def build_graph(g, a, d):
    for i in range(len(a)):
        g.add_edge( 's', 'a'+str(i), 1e15 )
        for j in range(len(d)):
            if a[i] >= d[j]:
                g.add_edge('a'+str(i), 'd'+str(j) )

    for j in range(len(d)):
        g.add_edge('d'+str(j) , 't')


raw_input()
a=[ int(i) for i in raw_input().split() ]
d=[ int(i) for i in raw_input().split() ]
g = FlowNetwork()

for i in range(len(a)):
    g.add_vertex( 'a'+str(i) )
for i in range(len(d)):
    g.add_vertex( 'd'+str(i) )

g.add_vertex('s')
g.add_vertex('t')

build_graph(g, a, d)
print g.max_flow('s', 't')
print [ g.flow[i] for i in  g.get_edges('s') ]