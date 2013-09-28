from operator import attrgetter
import sys

class Edge:
    def __init__(self,u,v,w):
        self.u = u
        self.v = v
        self.w = w
    
    def has_vertex(self,vertex_set):
        for v in vertex_set:
            if(self.v == v):
                return True
        return False

class graph:
    def __init__(self):
        self.edges = {}
        self.vertices = set()
        
    def add_vertex(self,v):
        self.edges[v] = []
        self.vertices.add(v)
    def add_edge(self,u,v,w):
        if u not in self.vertices:
            self.add_vertex(u)
        if v not in self.vertices:
            self.add_vertex(v)

        self.edges[u].append(Edge(u,v,w))
        self.edges[v].append(Edge(v,u,w))
    
    def get_edges(self,v):
        return self.edges[v]

    def mst(self,starter):
        
        mst_edges = []
        mst_vertices = set([starter])

        while(len(mst_vertices) < len(self.vertices)):
            min_edge = None
            min_val = -1
            for vertex in mst_vertices:
                test_edges = self.get_edges(vertex)
                for edge in test_edges:
#                    print "considering %s -- %s %d"%(edge.u,edge.v,edge.w)
                    if(edge.w < min_val or min_val == -1):
                        if edge.v not in mst_vertices:
 #                           print "accepted edge"
                            min_edge = edge
                            min_val = edge.w
            
  #          print "adding edge %s -- %s %d"%(min_edge.u,min_edge.v,min_edge.w)
            mst_edges.append(min_edge)
            mst_vertices.add(min_edge.v)
            mst_vertices.add(min_edge.u)
  #          print mst_vertices


        return mst_edges

def test_graph():
    g = graph()
    g.add_edge('abc','def',4)
    g.add_edge('ghi','def',4)
    g.add_edge('ghi','abc',10)
    return g.mst()

def run_one(line_list):
    g = graph()
    for line in line_list:
        larr = line.split(' ')
        g.add_edge(larr[0],larr[1],int(larr[2]))

    
    X = g.mst(line_list[0].split(' ')[0])
    tot = 0
    for x in X:
        tot+=x.w
    return tot

if __name__ == "__main__":
    fin = open(sys.argv[1])
    loop = int(fin.readline())
    for loopy in range(loop):
        input_num = int(fin.readline())
        X = []
        for i in range(input_num):
            X.append(fin.readline().strip())
        print run_one(X);
