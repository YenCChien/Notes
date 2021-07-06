## Tree.py
As a binary tree for creating

### Step 1, Create Graph 
```python
import networkx as nx
import matplotlib.pyplot as plt

#Step 1, Create Graph
class Graph(nx.Graph):
    def __init__(self,n):
        super(Graph, self).__init__()
        self.add_nodes_from(range(n))                                                   # give nodes for this graph
        self.full_tree_pos()
        self.dic = nx.convert.to_dict_of_dicts(self)
        self.color = ['blue']*n
    #Step 2, Shortest path
    def get_shortest_path(self,start_node_id,end_node_id,path=[]):
        path = path + [start_node_id]                                                   # record whole node path
        if start_node_id == end_node_id: return path                                    # final node return path
        if start_node_id not in self.dic.keys() or end_node_id not in self.dic.keys(): 
            return None
        shortlist = None
        for n in self.dic[start_node_id].keys():                                        # find node edge
            if n not in path:
                newpath = self.get_shortest_path(n, end_node_id, path)                  # keep exploring subtree until last node
                if newpath:
                    # print(shortlist)
                    if not shortlist or len(newpath) < len(shortlist):                  # record the path once get shorter than before
                        shortlist = newpath
        self.t = shortlist
        if self.t:                                                                      # give nodes of path green color for result of shortest path
            for i in self.t: 
                self.color[i] = 'green'
        return shortlist
    def full_tree_pos(self):
        n = self.number_of_nodes()
        if n == 0 : return {}
        self.pos = {0:(0.5,0.9)}
        if n == 1: return self.pos
        i = 1
        while True:
            if n >= 2**i and n<2**(i+1):
                height = i
                break
            i+=1
        p_key = 0                                       # node 0 to n
        p_y = 0.9
        p_x = 0.5
        l_child = True
        for i in range(height):                         # seperate each node and give two edge
            for j in range(2**(i+1)):
                if 2**(i+1)+j-1 < n:
                    # print(2**(i+1),j-1)
                    if l_child == True:
                        self.pos[2**(i+1)+j-1] = (p_x - 0.2/(i*i+1) ,p_y - 0.1)
                        self.add_edge(2**(i+1)+j-1,p_key)
                        l_child = False
                    else:
                        self.pos[2**(i+1)+j-1] = (p_x + 0.2/(i*i+1) ,p_y - 0.1)
                        l_child = True
                        self.add_edge(2**(i+1)+j-1,p_key)
                        p_key += 1
                        (p_x,p_y) = self.pos[p_key]
    def show(self):
        nx.draw(self, pos=self.pos,node_color=self.color, with_labels=True) 
        plt.show()
        self.color = ['blue']*self.number_of_nodes() # reset color
    def get_subtrees(self,selected_node_ids):
        q = []
        for n in selected_node_ids:
            q.append([s for s in self.edges if n == s[0]])
        return q
```

```python
g=g=Graph(11)
g.show()
```
![image](https://github.com/ty3n/Notes/blob/master/n11.png)
```python
g=g=Graph(11)
g.show()
```
![image](https://github.com/ty3n/Notes/blob/master/n25.png)

### Step 2,3 Shortest Path & Test
```python
g.get_shortest_path(22,24)
g.show()
# [22, 10, 4, 1, 0, 2, 5, 11, 24]
```
![image](https://github.com/ty3n/Notes/blob/master/s1.png)

```python
g.get_shortest_path(0,8)
g.show()
# [0, 1, 3, 8]
```
![image](https://github.com/ty3n/Notes/blob/master/s2.png)
```python
g.get_shortest_path(5,23)
g.show()
# [5, 11, 23]
```
![image](https://github.com/ty3n/Notes/blob/master/s3.png)

### Step 4, get_subtrees retrun edges of node id
```python
g.get_subtrees([4,3,20,23])
#[[(4, 9), (4, 10)], [(3, 7), (3, 8)], [], []]
```
```python
g.get_subtrees([10,11,1,9])
[[(10, 21), (10, 22)], [(11, 23), (11, 24)], [(1, 3), (1, 4)], [(9, 19), (9, 20)]]
```
