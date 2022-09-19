import numpy as np 

class Fourier():
    def __init__(self) -> None:
        pass

    def func_triangle():
        """Triangle shape function"""
        
        t=np.arange(-1*np.pi,np.pi,0.01)
        s=((1/np.pi)*-(t/abs(t))*(t)+1)
        return t,s



    def plot_sin(self ):
      t = np.arange(-1*np.pi,np.pi,0.01) 
      s=  self.amplitud.get()*np.sin(t)
      return(t,s)

    def plot_cos(self ):
      t = np.arange(-1*np.pi,np.pi,0.01) 
      s=  self.amplitud.get()*np.cos(t)
      return(t,s)
      

    def plot_func(self):
      t = np.arange(-1*np.pi,np.pi,0.01) 
      s=  (t/np.abs(t)) 
      return(t,s)

    def plot_error(self ):
      t = np.arange(-1*np.pi,np.pi,0.01) 
      s=  (t/np.abs(t)) * self.amplitud.get()
      return(t,s)
       