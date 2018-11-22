import copy
import random
import time
import itertools
import os
#import psutil


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


def maximal_independent_set(G, nodes=None):
    if not nodes:
        nodes = set([random.choice(G.nodes())])  # pick a random node
    else:
        nodes = set(nodes)
    if not nodes.issubset(G):
        print("not subset")

    # All neighbors of nodes
    neighbors = set.union(*[set(G.neighbors(v)) for v in nodes])
    if set.intersection(neighbors, nodes):
        print("%s is not an independent set of G" % nodes)

    indep_nodes = list(nodes)  # initial
    available_nodes = set(G.nodes()).difference(
        neighbors.union(nodes))  # available_nodes = all nodes - (nodes + nodes' neighbors)

    while available_nodes:
        # pick a random node from the available nodes
        node = random.choice(list(available_nodes))
        indep_nodes.append(node)

        available_nodes.difference_update(
            G.neighbors(node) + [node])  # available_nodes = available_nodes - (node + node's neighbors)

    return indep_nodes

def get_vertice_list(nv):
    return [i for i in range(nv)]

def get_neighbors(v,edges):
    n = []
    for e in edges:
        if v in e:
            n.append(e[(e.index(v)+1)%2])
    return n

def checker(edges,vertice_set):
    possible_edges = itertools.combinations(vertice_set,2)
    for e in possible_edges:
        if e in edges:
            return False
    return True

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s) + 1))

def calculate_independents(graph,vertices):
    indeps = []
    possible_sets = list(powerset(vertices))[len(vertices)+1:]
    for s in possible_sets:
        possible_edges = list(itertools.combinations(s,2))
        isIndep = True
        for e in possible_edges:
            if e in graph:
                isIndep = False
        if isIndep==True:
            indeps.append(s)
    return max(indeps,key=lambda item:len(item))

def get_max_edges(nv):
    return int((nv * (nv-1))/2)

def generate_graphs(nv, ne):
    return [graph for graph in itertools.combinations([edge for edge in itertools.combinations(range(0, nv), 2)], ne)]

graphs=generate_graphs(5,3)
for g in graphs:
    print(g)
    print(calculate_independents(g,get_vertice_list(5)))

v_sizes = [4,5,6,7] # diferent graph sizes
e_sizes = [0.2,0.3,0.4,0.5] # diferent edge quantity in relation to number of vertices
times_dict = {}
vecEdge = []

def main():
    indepList = []
    for v, e in vecEdge:
        start = time.time()
        ne = int(e*get_max_edges(v))
        vList = get_vertice_list(v)
        print(vList)
        graphs = generate_graphs(v, ne)
        print(graphs)
        indeps = [calculate_independents(g, vList) for g in graphs]
        print(indeps)
        print("Time:", time.time() - start)
        print("Vertices/Edges: ", v, int(e*get_max_edges(v)))
        process = psutil.Process(os.getpid())
        print(process.memory_info().rss)
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
    plt.show()'''
