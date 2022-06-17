import math
import matplotlib.pyplot as plt


g = 5
p = 0.49
t = 10

max_iter = 200
x=11
m=0
c=0
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


#print(list)
plt.plot(list)
plt.show()
