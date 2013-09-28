

N, ne = raw_input().split()
N= int(N)
ne= int(ne)
graph=[]
for i in range(N):
    graph.append([])

for i in range(ne):
    u,v = raw_input().split()
    u = int(u)-1
    v = int(v)-1
    graph[u].append(v) 
    graph[v].append(u)

visited= [0]*N
degree = [1] * N  




def explore(node):
    global graph, degree, visited
    visited[node] =1
    for nn in  graph[node]:
        if visited[nn] ==0:
            explore(nn)
            degree[node] += degree[nn]

explore(0)
print len( [i for i in degree if i%2==0] )-1
