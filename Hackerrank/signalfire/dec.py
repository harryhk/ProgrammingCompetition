import networkx as nx 

def build_graph(g, detec_list, w):
    for ci in range(len(detec_list)):
        d_ci = detec_list[ci]
        ci_in = str(ci)+'in'
        ci_out = str(ci) + 'out'

        g.add_edge(ci_in, ci_out, capacity=1)
        
        if d_ci[0] - d_ci[2] <=0:
            g.add_edge('s', ci_in, capacity=1)
        if d_ci[0] + d_ci[2] >=w:
            g.add_edge(ci_out, 't', capacity=1)
        
        
        for cj in range(ci+1, len(detec_list) ):
            d_cj = detec_list[cj]
            
            cj_in = str(cj) + 'in'
            cj_out = str(cj) + 'out'
            
            if (d_ci[0] - d_cj[0])**2 + (d_ci[1]- d_cj[1])**2 <= (d_ci[2]+d_cj[2])**2:
                g.add_edge(ci_out, cj_in, capacity=1  )
                g.add_edge(cj_out, ci_in, capacity=1  )
            


N= int( raw_input() ) 

for _ in range(N):
    w, h , nc = raw_input().split()
    w = int(w)
    h = int(h)
    nc= int(nc)
    g = nx.DiGraph()
    g.add_node('s')
    g.add_node('t')
    detec_list = []
    for _ in range(nc):
        x, y , r =  raw_input().split()
        x = int(x)
        y = int(y)
        r = int(r)
        detec_list.append( (x,y,r) )

    build_graph(g, detec_list, w)
    print  nx.max_flow(g, 's', 't')

        
