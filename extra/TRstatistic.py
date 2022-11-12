import math
import matplotlib.pyplot as plt

#log(g*n)=nodes preguntats
g = 1
#lier fraction
p = 0.49
#1/t=fraction of false accepted
t = 2

#max_iteration
max_iter = 10000
#start iteration (sometimes if too small can't do factorial for negatives)
x0=200
x=x0
#quantity of honest nodes
m=0
#probability that gets added
c=0
#list of data
list=[]



def fact(n):
    f = math.factorial(int(math.ceil(n)))
    return f

def log(g, n):
    l = int(math.ceil(math.log(int(math.ceil(g*n)), 2)))
    return l

def calc(p, g, m, x):
    log_log = log(g, x)
    fact_px = fact(p*x)
    fact_xminpx = fact(x-p*x)
    fact_log = fact(log_log)
    fact_xminlog = fact(x-log_log)
    fact_x = fact(x)
    fact_m = fact(m)
    fact_xminpxminm = fact(x-x*p-m)
    fact_logminm = fact(log_log-m)
    fact_xpmaxmminlog = fact(p*x+m-log_log)
    ans = fact_px * fact_xminpx *fact_log * fact_xminlog * 100 / (fact_x * fact_m * fact_xminpxminm * fact_logminm * fact_xpmaxmminlog)
    return ans


while x < max_iter:
    m=0
    c=0
    max0 = log(g, x)
    max = int(math.ceil(max0/t))
    while m < max:
        c0 = calc(p, g, m, x)
        c = c + c0
        m = m + 1
    list.append(c)
    x = x + 1
    print(x)


#log(g*n)=nodes preguntats
g = g
#lier fraction
p = 1-p
#1/t=fraction of false accepted
t = t

#max_iteration
max_iter = max_iter
#start iteration (sometimes if too small can't do factorial for negatives)
x=x0
#quantity of honest nodes
m=0
#probability that gets added
c=0
#list of data
list_2=[]

while x < max_iter:
    m=0
    c=0
    max0 = log(g, x)
    max = int(math.ceil(max0/t))
    while m < max:
        c0 = calc(p, g, m, x)
        c = c + c0
        m = m + 1
    list_2.append(c)
    x = x + 1
    print("_", x)

final_list = []
for a in range(max_iter-x0):
    value=(list_2[a]/list[a])
    print(value)
    final_list.append(value)

#print(list)
plt.plot(list)
plt.show()

#plt.plot(list_2)
#plt.show()
