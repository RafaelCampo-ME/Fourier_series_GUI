import numpy as np 
import matplotlib.pyplot as plt 
from scipy import integrate
 

class Fourier:
	"""Fourier series object"""
	def __init__(self) -> None:
		pass

	def funcion_escalon(self)->list:
		"""Return a tuple object of a square pulse function, where 0 element is the time series and the 1 element is the y series"""
		t= np.arange(-1*np.pi, np.pi,0.01)
		func_escalon= lambda x: x/np.abs(x)
		s = func_escalon(t)
		return (t, s)

	def fourier_escalon(self,num_expansion:int)-> list:
		"""Return a tuple object of the Fourier series aproximation of a square pulse function, where 0 element is the time series and the 1 element is the y series"""

		t= np.arange(-1*np.pi, np.pi,0.01)   ## t represents the time (x axis)
		func_escalon= lambda x: x/(np.abs(x))
		func_cos = lambda x,y: np.cos(y*x )
		func_sin = lambda x,y: np.sin(y*x)


		a_0 = []
		for i in range(len(t)):
			s=0
			for j in range(num_expansion):
				a_n = (1/np.pi)*(integrate.quad(lambda x: func_escalon(x)*func_cos(x,j),-np.pi,0)[0]+integrate.quad(lambda x: func_escalon(x)*func_cos(x,j),0,np.pi)[0])
				b_n = (1/np.pi)*(integrate.quad(lambda x: func_escalon(x)*func_sin(x,j),-np.pi,0)[0]+integrate.quad(lambda x: func_escalon(x)*func_sin(x,j),0,np.pi)[0])
				s=s+a_n*func_cos(t[i],j) + b_n*func_sin(t[i],j) 
			a_0.append(s) 

		
		return (t, a_0)

	def error_function(self,num_expansion:int):
		"""Return a tuple object of the % of error between a square pulse function and his Fourier series aproximation, where 0 element is the time series and the 1 element is the y series"""
		escalon = self.funcion_escalon()
		aprox_fourier = self.fourier_escalon(num_expansion=num_expansion)
		error= []

		for i in range(len(escalon[0])):
			er=(escalon[1][i]-aprox_fourier[1][i])/escalon[1][i]
			error.append(er)

		print(f"Tamaño de la listta error: {len(error)}")
		print(f"Tamaño de la listta error: {len(escalon[0])}")
		return(escalon[0],error)

print("Inicio recorrido")
f= Fourier()
plt.subplot()
plt.grid()
print("Ya tengo el grid")
plt.plot(f.error_function(10)[0],f.error_function(10)[1],"r--")
plt.show()
