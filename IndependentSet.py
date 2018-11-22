import matplotlib.pyplot as plt
import random
import time
import itertools

ops = 0

def get_vertice_list(nv):
    return [i for i in range(nv)]

def powerset(iterable):
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s) + 1))

def calculate_independents(graph,vertices): # basic_ops = len(possible_sets)*(4+2(len(possible_edges))) - (count incrementions)
    indeps = []
    global ops
    possible_sets = list(powerset(vertices))[len(vertices)+1:]
    for s in possible_sets:
        possible_edges = list(itertools.combinations(s,2))
        isIndep = True
        for e in possible_edges:
            if e in graph:
                isIndep = False
            ops+=(2-1)
        if isIndep==True:
            indeps.append(s)
        ops+=(4-1)
    return max(indeps,key=lambda item:len(item))

def get_max_edges(nv):
    return int((nv * (nv-1))/2)

def generate_graphs(nv, ne):
    return [graph for graph in itertools.combinations([edge for edge in itertools.combinations(range(0, nv), 2)], ne)]



v_sizes = [4,5,6,7,8,9]  # diferent graph sizes
e_sizes = [0.2,0.3,0.4,0.5] # diferent edge quantity in relation to number of vertices
times_dict = {}
ops_dict = {}
vecEdge = [(v,e) for v in v_sizes for e in e_sizes]

def main():
    indepList = []
    for v, e in vecEdge:
        global ops
        start = time.time()                                                         # Timer starts
        graphs = generate_graphs(v, int(v*e))
        for g in graphs:
            indepList.append(calculate_independents(g, get_vertice_list(v))[0])
        elapsed_time = time.time() - start                                          # Timer ends
        print("Time:", elapsed_time)
        print("Vertices/Edges: ", v, int(e*get_max_edges(v)))
        ops=ops*len(graphs)
        if e in times_dict.keys():
            times_dict[e][v] = elapsed_time
        else:
            times_dict[e] = {v:elapsed_time}

        if e in ops_dict.keys():
            ops_dict[e][v] = ops
        else:
            ops_dict[e] = {v:ops}
        ops = 0
    return indepList

main()
print(times_dict)

print("Results (Operations):")
print("%15s\t%15s\t%15s\t%15s\t%15s\t%15s\t%15s"%("Edges/Vertices","4","5","6","7","8","9"))
cnt = 0
for nVert, edgOps in ops_dict.items():
    line = "%15s\t"%("x"+str(e_sizes[cnt]))
    cnt+=1
    for op in edgOps.values():
        line+="%15s\t"%(str(op)) # Number of operations
    print(line)


print("\nResults (time):")
print("%25s\t%25s\t%25s\t%25s\t%25s\t%25s\t%25s"%("Edges/Vertices","4","5","6","7","8","9"))
cnt = 0
for nVert, edgTime in times_dict.items():
    line = "%25s\t"%("x"+str(e_sizes[cnt]*get_max_edges(nVert)))
    cnt+=1
    for time in edgTime.values():
        line+="%25s\t"%(str(time))
    print(line)

    plt.plot(edgTime.keys(), edgTime.values(), nVert)
    plt.axis([min(edgTime.keys()), max(edgTime.keys()) + 0.00000001, min(edgTime.values()),max(edgTime.values()) + 0.00000001])
    plt.show()
