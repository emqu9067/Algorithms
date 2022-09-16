import numpy as np

def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess'''
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    count = 0
    # make an array of zeros of length Nmax
    x = np.zeros((Nmax,1))
    # save the initial guess
    x[0] = x0
    while (count < Nmax):
       count = count +1
       x1 = f(x0)
       # save the current iterate
       x[count] = x1
       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          # truncate the array to have only count entries
          x = x[0:count]
          print('count=')
          print(count)
          return [xstar,x,ier,count]
       x0 = x1

    xstar = x1
    x = x[0:count]
    ier = 1
    print('count =')
    print(count)
    return [xstar,x,ier,count]

def compute_order(x,p):
    length=len(x)
    lamb=abs(x[length-1]-p)/abs(x[length-2]-p);
    alpha=(log(abs(x[length-1]-p))-log(lamb))/log(abs(x[length-2]-p))
    print('order=')
    print(alpha)
    return alpha

def aitken(x,tol,max):
    y = np.zeros(max,1)
    i=0
    while(i<max):
        y[i]=(((x[i+2])**2)-((x[i+1])**2))/(2*(x[i+1]+x[i+2]))
        i=i+1;
        if(y[i]<tol):
            y=y[0:i-1]
            return y
    return y
