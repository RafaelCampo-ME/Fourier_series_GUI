import numpy as np 
import matplotlib.pyplot as plt 
from scipy import integrate
import scipy as sp 

class Fourier:
  def __init__(self) -> None:
    pass

  def funcion_escalon(self):
    t= np.arange(-1*np.pi, np.pi,0.01)
    func_escalon= lambda x: x/np.abs(x)
    s = func_escalon(t)
    plt.plot(t,s,'r--')
    plt.show()

  def fourier_escalon(self,num_expansion):
    t= np.arange(-1*np.pi, np.pi,0.01)
    func_escalon= lambda x: x/(np.abs(x))
    func_cos = lambda x,y: np.cos(2*y*x/np.pi)
    func_sin = lambda x,y: np.sin(2*y*x/np.pi)



    a_0 = []
    for i in range(len(t)):
      s=0
      for j in range(num_expansion):
        a_n = (2/np.pi)*(integrate.quad(lambda x: func_escalon(x)*func_cos(x,j),-np.pi,0)[0]+integrate.quad(lambda x: func_escalon(x)*func_cos(x,j),0,np.pi)[0])
        b_n = (2/np.pi)*(integrate.quad(lambda x: func_escalon(x)*func_sin(x,j),-np.pi,0)[0]+integrate.quad(lambda x: func_escalon(x)*func_sin(x,j),0,np.pi)[0])
        s=s+func_escalon(t[i])*a_n*func_cos(t[i],j) + b_n*func_escalon(t[i])*func_sin(t[i],j) 
      a_0.append(s) 
    s = func_escalon(t)

    plt.plot(t,a_0,'r--')
    plt.show()
 
f= Fourier()
plt.grid()
f.fourier_escalon(100)
