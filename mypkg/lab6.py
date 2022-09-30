import numpy
import math
def evalF(x):return numpy.array([4*(x[0]**2) + (x[1]**2)-4,x[0]+x[1]-math.sin(x[0]-x[1])])
def evalJ(x):return numpy.array([[8*x[0],2*x[1]],[1-math.cos(x[0]-x[1]),1+math.cos(x[0]-x[1])]])
def Newton(x0,tol,Nmax):

    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

    for its in range(Nmax):
       J = evalJ(x0)
       Jinv = numpy.linalg.inv(J)
       F = evalF(x0)

       x1 = x0 - Jinv.dot(F)

       if (numpy.linalg.norm(x1-x0) < tol):
           xstar = x1
           ier =0
           return[xstar, ier, its]

       x0 = x1

    xstar = x1
    ier = 1
    return[xstar,ier,its]

def LazyNewton(x0,tol,Nmax):

    ''' Lazy Newton = use only the inverse of the Jacobian for initial guess'''
    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

    J = evalJ(x0)
    Jinv = numpy.linalg.inv(J)
    for its in range(Nmax):

       F = evalF(x0)
       x1 = x0 - Jinv.dot(F)

       if (numpy.linalg.norm(x1-x0) < tol):
           xstar = x1
           ier =0
           return[xstar, ier,its]

       x0 = x1

    xstar = x1
    ier = 1
    return[xstar,ier,its]

def LazyNewton2(x0,tol,Nmax):

    ''' Lazy Newton = use only the inverse of the Jacobian for initial guess'''
    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

    J = evalJ(x0)
    Jinv = numpy.linalg.inv(J)
    for its in range(Nmax):

       F = evalF(x0)
       x1 = x0 - Jinv.dot(F)

       if (numpy.linalg.norm(x1-x0) < tol):
           xstar = x1
           ier =0
           return[xstar, ier,its]
       if((numpy.linalg.norm(x1)) > (numpy.linalg.norm(x0))/2):
           J=evalJ(x1)
           Jinv=numpy.linalg.inv(J)
       x0 = x1

    xstar = x1
    ier = 1
    return[xstar,ier,its]

p0=numpy.array([1,0])
print(Newton(p0,10**-10,100))
print(LazyNewton(p0,10**-10,100))
print(LazyNewton2(p0,10**-10,100))
