import networkx as nx
import random
import csv
import numpy as np
import scipy
G = nx.DiGraph()
eage = []
with open('stormofswords.csv') as f:
    for row in csv.reader(f):
        if row[0] != '#Source':
            Scource = row[0]
            Target = row[1]
            eage.append((Scource,Target))

G.add_edges_from(eage)

pagerank = nx.pagerank(G,alpha=0)

# pagerank_1 = sorted(pagerank.items(),key=lambda x: x [1])
P_1 = []
for x in pagerank.values():
    P_1.append(x)

print(P_1)


rwp = {}
nodes = [i for i in G.nodes]
# nodes = list(G.nodes())
for x in pagerank.keys():
    rwp[x] = 0
r = random.choice(nodes)
rwp[r] = 1

neigh = list(G.out_edges(r))
z = 0

while (z != 10000):
        if (len(neigh) == 0):
            focus = random.choice(nodes)
        else:
            r1 = random.choice(neigh)
            focus = r1[1]
        rwp[focus] += 1
        neigh = list(G.out_edges(focus))
        z += 1


# t = np.array(rwp)
# t_1 = sorted(rwp.items(),key=lambda x: x [1])
T_1 = []
for x in rwp.items():
    a = list(x)
    a[1] = x[1]
    T_1.append(a[1])
print(T_1)

S = scipy.stats.spearmanr(P_1, T_1)[0]
print(S)





def gini(x, w=None):
    x = np.asarray(x)
    if w is not None:
        w = np.asarray(w)
        sorted_arg = np.argsort(x)
        sorted_x = x[sorted_arg]
        sorted_w = w[sorted_arg]
        result_w = np.cumsum(sorted_w, dtype=float)
        result_xw = np.cumsum(sorted_x * sorted_w, dtype=float)
        return (np.sum(result_xw[1:] * result_w[:-1] - result_xw[:-1] * result_w[1:]) /
                (result_xw[-1] * result_w[-1]))
    else:
        sorted_x = np.sort(x)
        n = len(x)
        result_x = np.cumsum(sorted_x, dtype=float)
        return (n + 1 - 2 * np.sum(result_x) / result_x[-1]) / n


Gini = gini(P_1)
print(Gini)