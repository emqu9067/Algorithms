from math import e
import math
def ex(x):return (x**2)+(7*x)-30
def xp(x):return (2*x)+7
def f(x):return (e**(ex(x)))-1
def fp(x):return (e**(ex(x)))*(xp(x))
def fpp(x):return (2*(e**(ex(x))))+(xp(x)*(fp(x)))
def gprime(x):return ((fp(x)**2)-(f(x)*fpp(x)))/(fp(x)**2)
def newton(p0,Nmax,tol):
    i=0

    while(i<Nmax):
        p1=p0-(f(p0)/fp(p0))
        if(abs(p1-p0)<tol):
            print('root found with newton at',p1,'with',i,'iterations')
            return p1
        p0=p1
        i=i+1
    print('tol condition not met,newton failed')
    return p0

def bisection(a,b,Nmax,tol):
    x=f(a);y=f(b)

    if(x*y>0):
        #secent method
        print('same signed evaluation, use secent')
        return a

    if(x==0):
        print('root found at points given')
        return x

    if(y==0):
        print('root found at points given')
        return y

    if(x*y<0):
        print('evaluated prodect is negative')
        print('guaranteed root in given interval')

        count=0
        while(count<Nmax):
            c=(a+b)/2;z=f(c)
            if(gprime(c)<0):
                print('hybrid used at iteration',count+1,', p=',c)
                Npoint=c
            if(x*z<0):
                b=c;y=z
            elif(y*z<0):
                a=c;x=z
            else:
                print('sketch')
                return c
            if(abs(b-a)<tol):
                print('normal bisectin results')
                print('fount root tolrance at',a,'with',count,'iterations')
                return [a,Npoint]
            count=count+1;
        return [a,0]



a=-2;b=4.5
Nmax=100
tol=10**-10
p0=4.5
print("bisection")
[p1,p2]=bisection(a,b,Nmax,tol)
print('normal newton results')
newton(p0,Nmax,tol)
print('using the hybrid point we foung in bisection')
print('these the results of passing that point to newton')
newton(p2,Nmax,tol)
