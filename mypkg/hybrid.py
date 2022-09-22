class hybrid:
    def __init__(self,f,fp):
        self.f=f
        self.fp=fp
        self.a=None
        self.b=None
        self.p0=None
        self.Nmax=None
        self.tol=None


def bisection(f,fp,fpp,a,b,tol,Nmax):

    x=f(a);y=f(b);c=(a+b)/2;z=f(c)

    if(f(a) * f(b) >0):
        #secent method
        return 'same signed evaluation, use secent'

    if(x==0 or y==0 or z==0):
        return 'root found at points given'

    if(f(a) * f(b) <0):return 'evaluated prodect is negative'

def newton(f,fp,p0,tol,Nmax):
    i=0

    while(i<Nmax):
        p1=p0-(f(p0)/fp(p0))
        if(abs(p1-p0)<tol):return p1
        p0=p1
        i=i+1
