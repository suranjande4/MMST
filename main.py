import math
import random
import networkx as nx
import copy
import matplotlib.pyplot as plt
from itertools import combinations
from networkx.algorithms import tree
class point:
    def __init__(self):
        self.x=0
        self.y=0
        self.oldx=0
        self.oldy=0
        self.radius=random.randint(1,20)
        self.theta=math.pi/5
    def make_point_random(self):
        self.x=random.randint(0,20)
        self.y=random.randint(0,20)
        self.oldx=self.x
        self.oldy=self.y
        self.center_x=self.x - self.radius
        self.center_y=self.y
    def distance(self,another_point):
        return math.sqrt((self.x-another_point.x)**2 + (self.y-another_point.y)**2)
    def __str__(self):
        return 'x:'+str(self.x)+'\ny:'+str(self.y)
    def at_time_t(self,t):
        self.x=round(self.center_x  + (self.radius*(round(math.cos(self.theta*t),2))),2)
        self.y =round(self.center_y +  (self.radius * (round(math.sin(self.theta * t),2))),2)

n=int(input("Enter the number of nodes:- "))


##Creation of the initial weighted complete graph where the weights are the distances between the points#####

G=nx.Graph()
all_points=[]
pos={}
for i in range(n):
    p=point()
    p.make_point_random()
    all_points.append(copy.deepcopy(p))
    pos[all_points[i]] = (p.x,p.y)
    G.add_node(all_points[i])
    print(pos[all_points[i]],p.radius)
plt.rcParams["figure.figsize"] = (6,7)
edges = list(combinations(all_points,2))
for edge in edges:
    G.add_edge(edge[0],edge[1],weight=round(edge[0].distance(edge[1]),2))
'''nx.draw(G,pos = pos)
labels = nx.get_edge_attributes(G,'weight')
nx.draw(G,pos=pos)
nx.draw_networkx_edge_labels(G,pos=pos,edge_labels=labels)
#plt.savefig("Initial_graph.png")
plt.show()'''


###Computed MST Of the initial graph #####

mst = tree.minimum_spanning_edges(G, algorithm="kruskal", weight="weight")
tree = list(mst)
H = nx.Graph()
H.add_edges_from(tree)
labels = nx.get_edge_attributes(H, 'weight')
'''nx.draw(H, pos=pos, with_labels=True)
nx.draw_networkx_edge_labels(H, pos=pos, edge_labels=labels)
plt.text(0.5,0.5,"cost= "+str(H.size(weight="weight")))
plt.title("MST_at_time 0")
plt.show()'''


###Fixed the tree and rotating the points in a circular path(Anti-clock wise) each with radius between (1,3) and computing the cost ######


cost=[]
time=[]
cost.append(H.size(weight="weight"))
time.append(0)

for i in range(1,11):
    time.append(i)
    for k in range(n):
        all_points[k].at_time_t(i)
    O = nx.Graph()
    for a in range(n):
        N = H.neighbors(all_points[a])
        for j in N:
            if (O.has_edge(all_points[a], j) == False):
                O.add_edge(all_points[a], j, weight=round(all_points[a].distance(j), 2))
    labels = nx.get_edge_attributes(O, 'weight')
    '''nx.draw(O, pos=pos, with_labels=True)
    nx.draw_networkx_edge_labels(O, pos=pos, edge_labels=labels)
    plt.title("MST_at_time " + str(i))
    plt.show()'''
    cost.append(round(O.size(weight="weight"),2))


f=open('result.txt','a')
max=cost[0]
for i in range(len(cost)):
    if cost[i] > max:
        max= cost[i]
ratio=round(max/cost[0],2)
f.write(str(ratio)+" "+str(n))
f.write("\n")
f.close()
plt.xlabel("Time")
plt.ylabel("Cost")
plt.plot(time,cost) ### plotted the time vs cost graph
plt.title("result")
plt.show()
#plt.imsave