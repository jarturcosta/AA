import time
import itertools


'''         
def calculate_independents(self):
    vertices = self.v
    edges = self.e
    indeps = vertices
    for v in vertices:
        for e in edges:
            if v in e and e.strip(v) in indeps:  #nº de operações = 4 (2 condições + 1 remove + 1 strip) * nº arestas * nº vertices
                indeps.remove(e.strip(v))
    return indeps 
'''

def get_vertice_list(nv):
    return [i for i in range(nv)]

def calculate_independents(graph,vertices):
    indeps = vertices
    for edge in graph:
        if edge[0] in vertices:
            indeps.remove(edge[0])
        if edge[1] in vertices:
            indeps.remove(edge[1])
    return indeps

def get_max_edges(nv):
    return int((nv * (nv-1))/2)

def generate_graphs(nv, ne):
    return [graph for graph in itertools.combinations([edge for edge in itertools.combinations(range(0, nv), 2)], ne)]


v_sizes = [4,5,6,7,8] # diferent graph sizes
e_sizes = [0.2,0.3,0.4,0.5] # diferent edge quantity in relation to number of vertices
times_dict = {}
vecEdge = []
for e in e_sizes:
    for v in v_sizes:
        vecEdge.append((v, e))

def main():
    indepList = []
    for v, e in vecEdge:
        start = time.time()
        graphs = generate_graphs(v, int(e*get_max_edges(v)))
        indeps = [calculate_independents(g, get_vertice_list(5)) for g in graphs]
        print("Time:", time.time() - start)
        print("Vertices/Edges: ", v, int(e*get_max_edges(v)))
        indepList.append(indeps)
    return indepList

print(main())

'''
print("Calculating independent sets...")
for G in graphs:
    start_time = time.time_ns()
    G.calculate_independents()
    elapsed_time = time.time_ns() - start_time
    if(G.get_n_vertices() in times_dict.keys()):
        times_dict[G.get_n_vertices()][G.get_n_edges()] = elapsed_time
    else:
        times_dict[G.get_n_vertices()] = {G.get_n_edges():elapsed_time}

print("Results (Operations):")
print("%15s\t%15s\t%15s\t%15s\t%15s\t%15s\t%15s\t%15s\t%15s"%("Edges/Vertices","10","50","100","500","1000","5000","10000","50000"))
cnt = 0
for nVert, edgTime in times_dict.items():
    line = "%15s\t"%("x"+str(e_sizes[cnt]))
    cnt+=1
    for nEdges in edgTime.keys():
        line+="%15s\t"%(str(4*nVert*nEdges)) # Number of operations
    print(line)


print("\nResults (time):")
print("%15s\t%15s\t%15s\t%15s\t%15s\t%15s\t%15s\t%15s\t%15s"%("Edges/Vertices","10","50","100","500","1000","5000","10000","50000"))
cnt = 0
for nVert, edgTime in times_dict.items():
    line = "%15s\t"%("x"+str(e_sizes[cnt]))
    cnt+=1
    for time in edgTime.values():
        line+="%15s\t"%(str(time))
    print(line)

    plt.plot(edgTime.keys(), edgTime.values(), nVert)
    plt.axis([min(edgTime.keys()), max(edgTime.keys()) + 0.00000001, min(edgTime.values()),max(edgTime.values()) + 0.00000001])
    plt.show()
    '''


