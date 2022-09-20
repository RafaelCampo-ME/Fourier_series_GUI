import numpy as np 
import matplotlib.pyplot as plt 
from scipy import integrate
import scipy as sp 


class Fourier():
    def __init__(self) -> None:
        pass

    def func_triangle(self):
        """Triangle shape function"""
        
        t=np.arange(-1*np.pi,np.pi,0.01)
        s=((1/np.pi)*-(t/abs(t))*(t)+1)
        fig = plt.plot(t,s,'r--')
        return fig



    def plot_sin(self ):
      t = np.arange(-1*np.pi,np.pi,0.01) 
      s= np.sin(t)
      fig = plt.plot(t,s)
      return fig
       

    def plot_cos(self ):
      t = np.arange(-1*np.pi,np.pi,0.01) 
      s=  np.cos(t)
      fig = plt.plot(t,s)
      return fig
      

    def plot_func(self):
      t = np.arange(-1*np.pi,np.pi,0.01) 
      s=  (t/np.abs(t)) 
      fig = plt.plot(t,s,'r--')
      return fig

    def plot_error(self):
      t = np.arange(-1*np.pi,np.pi,0.01) 
      s=  (t/np.abs(t)) * self.amplitud.get()
      fig = plt.plot(t,s)
      return fig
       
    def fourier_escalon_coeficientes(self):
        
      s= lambda x: (x/np.abs(x)) 
      termino_cos = lambda x: (x*np.cos(2*x))/np.abs(x)
      termino_sin = lambda x: (x*np.sin(2*x))/np.abs(x)

      a_0 = 1/(np.pi)*( integrate.quad(s,0, np.pi)[0] + integrate.quad(s, -np.pi, 0)[0])
      a_n = 1/(np.pi)* ((integrate.quad( termino_cos,-np.pi,0)[0])+(integrate.quad( termino_cos,0,np.pi)[0])) 
      b_n = 1/(np.pi)* ((integrate.quad( termino_sin,-np.pi,0)[0])+(integrate.quad( termino_sin,0,np.pi)[0])) 

      return (a_0,a_n,b_n)


      
f = Fourier()
print(f.fourier_escalon_coeficientes())
