import numpy as np
import matplotlib.pyplot as plt
f=lambda x: 1.0/(1+np.power(10.0*x.2))
N=10
X=np.linspace(-1,1,N+1)
neval=1000
xeval=np.linspace(-1,1,neval)
v=np.zeros(N+1,N+1)
for j in range(0,N+1):
    v[:,j]=np.power(X,j)

F=f(X)
C=np.linalg.solve(v,F)
feval=f(xeval)
veval=np.zeros((neval,N+1))
for j in range(0,N+1)
    veval[:,j]=np.power(Xeval,j)

plt.plot(X,F,'ko-')
