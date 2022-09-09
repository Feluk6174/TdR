from decimal import DivisionByZero
import math

class Node():
    def __init__(self, node_id):
        self.id = node_id
        self.connections = []
        
    def set_connection(self, node_id):
        if not node_id in self.connections and not node_id == self.id:
            self.connections.append(node_id)
            return True
        return False
        
    
    def hop(self, target):
        pass
    
n = 6

def get_n_connections(n):
    l_n = math.log2(n)
    if int(l_n) == l_n:
        return l_n
    return int(l_n)+1
    
conn_groups = []

num_groups = 1

for i in range(get_n_connections(n)):
    num_groups *= (n-3-i)
    
for i in range(num_groups):
    conn_groups.append([Node(j) for j in range(n)])
    
def iter(n, conn_groups, depth):
    if depth == 0:
        return

    

    depth -= 1
    iter(n, depth)
    return

for group in conn_groups:
    for i in range(n):
        try:
            group[i].set_connection(group[i].id-1)
            group[i].set_connection(group[i].id+1)
        except IndexError:
            if i == 0:
                group[i].set_connection(n-1)
                group[i].set_connection(group[i].id+1)
            elif i == n-1:
                group[i].set_connection(group[i].id-1)
                group[i].set_connection(0)
                
                
for group in conn_groups:
    for node in group:
        for i in range(n-3):
            l = i
            res = False
            while not res:
                res = node.set_connection(i)
                if not res:
                    l += 1
                if l > n:
                    raise DivisionByZero
        