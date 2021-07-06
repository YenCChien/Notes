import networkx as nx
import matplotlib.pyplot as plt

class Graph(nx.Graph):
    def __init__(self,n):
        super(Graph, self).__init__()
        self.add_nodes_from(range(n))                                                   # give nodes for this graph
        self.full_tree_pos()
        self.dic = nx.convert.to_dict_of_dicts(self)
        self.color = ['blue']*n
    def get_shortest_path(self,start_node_id,end_node_id,path=[]):
        path = path + [start_node_id]                                                   # record whole tree path
        if start_node_id == end_node_id: return path                                    # final node return path
        if start_node_id not in self.dic.keys() or end_node_id not in self.dic.keys(): 
            return None
        shortlist = None
        for n in self.dic[start_node_id].keys():                                        # find node edge
            if n not in path:
                newpath = self.get_shortest_path(n, end_node_id, path)                  # keep exploring subtree until last node
                if newpath:
                    print(shortlist)
                    if not shortlist or len(newpath) < len(shortlist):                  # record the path once get shorter than before
                        shortlist = newpath
        self.t = shortlist
        if self.t:                                                                      # give nodes of path green color
            for i in self.t: 
                self.color[i] = 'green'
        return shortlist
    def full_tree_pos(self):
        n = self.number_of_nodes()
        if n == 0 : return {}
        self.pos = {0:(0.5,0.9)}
        if n == 1: return self.pos
        i = 1
        while(True):
            if n >= 2**i and n<2**(i+1):
                height = i
                break
            i+=1
        p_key = 0                                       # as a root for subtree from node 0 to n
        p_y = 0.9
        p_x = 0.5
        l_child = True
        for i in range(height):                         # a height for each subtree that should be 2 to the nth
            for j in range(2**(i+1)):
                if 2**(i+1)+j-1 < n:
                    print(i,j)
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

g=Graph(11)
g.get_shortest_path(0,10)
# g.show()
