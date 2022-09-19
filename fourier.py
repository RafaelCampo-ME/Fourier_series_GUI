import numpy as np 
import matplotlib.pyplot as plt 

class Fourier():
    def __init__(self) -> None:
        pass

    def func_triangle(self):
        """Triangle shape function"""
        
        t=np.arange(-1*np.pi,np.pi,0.01)
        s=((1/np.pi)*-(t/abs(t))*(t)+1)
        fig = plt.plot(t,s)
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
      fig = plt.plot(t,s)
      return fig

    def plot_error(self ):
      t = np.arange(-1*np.pi,np.pi,0.01) 
      s=  (t/np.abs(t)) * self.amplitud.get()
      fig = plt.plot(t,s)
      return fig
       