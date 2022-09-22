import numpy as np

def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess'''
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''
    x=np.zeros((Nmax,1))
    x[0]=x0
    count = 0
    while (count <Nmax-1):
       count=count+1
       x[count] = f(x[count-1])
       if (abs(x[count]-x[count-1]) <tol):
          ier = 'found: '
          x=x[0:count]
          return [ier,x,count]

    if (count==Nmax-1):
        ier = 'no more iterations'
        return [ier,x,count]

def aitken(x,tol,max):
    y = np.zeros((max,1))
    i=0
    while(i<max-2):
        y[i]=((x[i+2]*x[i])-(x[i+1]**2))/((x[i+2])-(2*(x[i+1]))+(x[i]))
        if(abs(y[i]-p)<tol):
            y=y[0:i]
            print('success:',i,'iterations needed')
            return y
        i=i+1
    if (i==max-2):
        print('failure')
        return y

def compute_order(x,p):
        #print('the order equation is')
        #print('log(|p_{n+1}-p|) = log(lambda) + alpha*log(|p_n-p|) where')
    length=len(x)
    lamb=(abs(x[length-1]-p))/(abs(x[length-2]-p))
    if (lamb<1):return 'order is one'
    lamb=(abs(x[length-1]-p))/((abs(x[length-2]-p))**2)
    if (lamb<1):return 'order is two'
    return '???'

g=lambda x:((10)/(x+4))**(1/2)

[eyy,bee,see]=fixedpt(g,1.5,10**(-10),100)
print(eyy,see,'iterations needed')
print(bee)
p=1.3652300134140976
print(compute_order(bee,p))
y1=aitken(bee,10**(-10),len(bee))
print(compute_order(y1,p))
print(y1)
print('the order of convergence of the aitken and')
print('fixed point method are the same')
print('possibly becuase the aitken method takes')
print('its points from the fixed point method')
print('but the aitken method required less iterations')
