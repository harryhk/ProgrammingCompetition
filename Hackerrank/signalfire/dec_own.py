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
        return sum(self.flow[edge] for edge in self.get_edges(source))



def build_graph(g, detec_list, w):
    for ci in range(len(detec_list)):
        d_ci = detec_list[ci]
        ci_in = str(ci)+'in'
        ci_out = str(ci) + 'out'

        g.add_edge(ci_in, ci_out)
        
        if d_ci[0] - d_ci[2] <=0:
            g.add_edge('s', ci_in)
        if d_ci[0] + d_ci[2] >=w:
            g.add_edge(ci_out, 't')
        
        
        for cj in range(ci+1, len(detec_list) ):
            d_cj = detec_list[cj]
            
            cj_in = str(cj) + 'in'
            cj_out = str(cj) + 'out'
            
            if (d_ci[0] - d_cj[0])**2 + (d_ci[1]- d_cj[1])**2 <= (d_ci[2]+d_cj[2])**2:
                g.add_edge(ci_out, cj_in  )
                g.add_edge(cj_out, ci_in  )




N= int( raw_input() ) 

for _ in range(N):
    w, h , nc = raw_input().split()
    w = int(w)
    h = int(h)
    nc= int(nc)
    g = FlowNetwork() 
    g.add_vertex('s')
    g.add_vertex('t')
    detec_list = []
    for _ in range(nc):
        x, y , r =  raw_input().split()
        x = int(x)
        y = int(y)
        r = int(r)
        detec_list.append( (x,y,r) )

    for deci in range(len(detec_list)):
        g.add_vertex( str(deci) + 'in' )
        g.add_vertex( str(deci) + 'out')
    
    build_graph(g, detec_list, w)
    print  g.max_flow('s', 't')

