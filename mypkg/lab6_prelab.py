import numpy
import math

def f(x): return(math.cos(x))
print(f(0))
def fd(s,h):
    j=len(h)
    i=0
    v1=numpy.zeros((j,1))
    v2=numpy.zeros((j,1))
    while(i<j):
        v1[i]=(f(s+h[i])-f(s))/h[i]
        v2[i]=(f(s+h[i])-f(s-h[i]))/(2*h[i])
        i=i+1
    return [v1,v2]

h=(.01*2*-numpy.arange(1,11))
print(h)
[a1,a2]=fd((math.pi)/2,h)
print(math.pi)
print(numpy.transpose(a1))
print(a2)

print(abs(a1[0]+1)/abs(a1[1]+1))
print(abs(a2[0]+1)/abs(a2[1]+1))
