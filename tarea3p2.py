#! /usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import ode
from mpl_toolkits.mplot3d import Axes3D


"""
este script integra el oscilador de lorenz mediante el metodo de rK4,
utilizando un metodo ya implementado de scipy



"""
def Lorenz(t,v,cons):
#funcion para definir las ecuaciones de lorenz, t=tiempo, v=variables (x,y,z)

  sigma=cons[0]
  beta=cons[1]
  rho=cons[2]

  dv=np.zeros([3])
  dv[0]=sigma*(v[2]-v[1])
  dv[1]=v[0]*(rho-v[2])-v[1]
  dv[2]=v[0]*v[1]-beta*v[2]


  return dv


cons=[10 , 2.666 , 28]
ti=0
tf=200
dt=0.01
vi=[100,2000,400]
Y=[]
T=[]

solucion = ode(Lorenz).set_integrator('vode',method='adams')
#metodo que ejecuta RK4

solucion.set_f_params(cons).set_initial_value(vi,ti) #configuracion de los parametros del problema

while solucion.successful() and solucion.t+dt < tf:

  solucion.integrate(solucion.t+dt)
  Y.append(solucion.y)
  T.append(solucion.t)

Y = np.array(Y)


fig = plt.figure(3)
fig.clf()
ax = fig.add_subplot(111, projection='3d')
ax.set_aspect('auto')
ax.set_title(r'$Grafico \ de \ las \ soluciones \ de \ las \ ecuasiones \ de \ Lorenz$')
ax.plot(Y[:,0], Y[:,1],Y[:,2],'r-')
ax.set_xlabel(r'$Eje \ X$')
ax.set_ylabel(r'$Eje \ Y$')
ax.set_zlabel(r'$Eje \ Z$')
fig.savefig('3d')
plt.show()
