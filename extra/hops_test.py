from decimal import DivisionByZero
import math

from psutil import net_connections

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

conn_groups = [] 

def get_n_connections(n):
    l_n = math.log2(n)
    if int(l_n) == l_n:
        return l_n
    return int(l_n)+1

n_connections = get_n_connections(n)
print("n_connections: ", n_connections)

zero = []
first = []
second = []
third = []



def finish(last:list, origin:int):
    global n, n_connections
    
    final = []
    for t in last:
        if len(t) == 6:
            pass
        for i in range(1, n):
            temp = [origin, i]
            temp.sort()
            num = 0
            for val in t:
                if val[1] == origin or val[0] == origin or val[1] == i or val[0] == i:
                    num += 1
            if not temp in t or not num >= n_connections:
                final.append([*t, temp])
    return final

for i in range(1, n):
    temp = [0, i]
    temp.sort()
    first.append([temp])

for _ in range(n_connections-1):
    first = finish(first, 0)

for _ in range(n_connections-1):
    first = finish(first, 1)    
    
for _ in range(n_connections-1):
    first = finish(first, 2)    

for _ in range(n_connections-1):
    first = finish(first, 3)    

#for _ in range(n_connections-1):
#    first = finish(first, 4)    

text = ""

for temp in first:
    for t in temp:
        text += str(t)+"\n"
    text += "\n"

print(text)

print(first[0])

print(len(first), len(third))
