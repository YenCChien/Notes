import networkx as nx
import matplotlib.pyplot as plt

class Graph(nx.Graph):
    def __init__(self,n):
        super(Graph, self).__init__()
        self.add_nodes_from(range(n))
        self.full_tree_pos()
        self.dic = nx.convert.to_dict_of_dicts(self)
    def get_shortest_path(self,start_node_id,end_node_id,path=[]):
        path = path + [start_node_id]
        if start_node_id == end_node_id: return path
        if start_node_id not in self.dic.keys():return None
        shortlist = None
        for n in self.dic[start_node_id].keys():
            if n not in path:
                newpath = self.get_shortest_path(n, end_node_id, path)
                if newpath:
                    if not shortlist or len(newpath) < len(shortlist):
                        print(start_node_id,n)
                        shortlist = newpath
        self.t = shortlist
        return shortlist
    def rshow(self):
        # m = [self.pos[i] for i in self.t]
        nx.draw_networkx_edges(self, self.pos, edgelist=[(0, 1), (0, 2), (1, 3)],width=8, alpha=0.5, edge_color='r')
        plt.show()
    def full_tree_pos(self):
        n = self.number_of_nodes()
        if n == 0 : return {}
        # Set position of root
        self.pos = {0:(0.5,0.9)}
        if n == 1:
            return self.pos
        # Calculate height of tree
        i = 1
        while(True):
            if n >= 2**i and n<2**(i+1):
                height = i
                break
            i+=1
        # compute positions for children in a breadth first manner
        p_key = 0
        p_y = 0.9
        p_x = 0.5
        l_child = True # To indicate the next child to be drawn is a left one, if false it is the right child
        for i in range(height):
            for j in range(2**(i+1)):
                if 2**(i+1)+j-1 < n:
                    print (2**(i+1)+j-1,p_key)
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
        nx.draw(self, pos=self.pos, with_labels=True)
        plt.show()

g=Graph(11)
g.get_shortest_path(0,10)
g.rshow()

# import networkx as nx
# import matplotlib.pyplot as plt
# g = nx.Graph()
# g.add_edge(131,673,weight=673)
# g.add_edge(131,201,weight=201)
# g.add_edge(673,96,weight=96)
# g.add_edge(201,96,weight=96)
# nx.draw(g,with_labels=True)
# plt.show()
