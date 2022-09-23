import numpy as np 
import matplotlib.pyplot as plt 
from scipy import integrate
 

class Fourier:
	"""Fourier series object"""
	def __init__(self) -> None:
		pass

# TODO: This class just can handle the fourier serie for a square pulse when the pulse belows (-pi,pi), but can be refactored to use a Fourier Series in any function in that range
# Its necesary to add a new method and change the existing ones in order to archive that 

	def function_triangle_pulse(self):
		"""Return a tuple object of a triangle shape pulse, where the 0 element is the time series and the 1 element es the y series"""
		t = np.arange(-1*np.pi,np.pi, 0.01)
		s=((1/np.pi)*-(t/abs(t))*(t)+1)
		return (t,s)



	def function_square_pulse(self)->list:
		"""Return a tuple object of a square pulse function, where 0 element is the time series and the 1 element is the y series"""
		t= np.arange(-1*np.pi, np.pi,0.01)
		func_escalon= lambda x: x/np.abs(x)
		s = func_escalon(t)
		return (t, s)


	def function_cos_sin_random_pulse(self):
		"""Return a tuple object of a triangle shape pulse, where the 0 element is the time series and the 1 element es the y series"""
		t = np.arange(-1*np.pi,np.pi, 0.01)
		s= np.abs(np.sin(t)) + np.cos(t)
		return (t,s)


	def fourier_escalon(self,num_expansion:int)-> list:
		"""Return a tuple object of the Fourier series aproximation of a square pulse function, where 0 element is the time series and the 1 element is the y series"""

		t= np.arange(-1*np.pi, np.pi,0.01)   ## t represents the time (x axis)
		func_escalon= lambda x: x/(np.abs(x))
		func_cos = lambda x,y: np.cos(y*x)
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
	
	
	def fourier_series_aprox(self,num_expansion:int,func_name:str):
		"""Return a tuple object of the Fourier serie aproximation of function"""
		
		func_lambda = lambda x: x/np.abs(x)

		if func_name == 'Square':
			func_lambda = lambda x: x/np.abs(x)
		elif func_name == 'Triangle':
			func_lambda = lambda x: ((1/np.pi)*-(x/abs(x))*(x)+1)   
		elif func_name == 'Random_sin_cos':
			func_lambda = lambda x: np.abs(np.sin(x)) + np.cos(x)
		else:
			pass 

		t= np.arange(-1*np.pi, np.pi,0.01)   ## t represents the time (x axis)
		func_cos = lambda x,y: np.cos(y*x)
		func_sin = lambda x,y: np.sin(y*x)
		a_0 =  (1/np.pi) * (integrate.quad(func_lambda,-1*np.pi,0)[0]+integrate.quad(func_lambda,0,np.pi)[0])

		s_list = []
		for i in range(len(t)):
			s= a_0
			for j in range(num_expansion):
				
				a_n = (1/np.pi)*(integrate.quad(lambda x: func_lambda(x)*func_cos(x,j),-np.pi,0)[0]+integrate.quad(lambda x: func_lambda(x)*func_cos(x,j),0,np.pi)[0])
				b_n = (1/np.pi)*(integrate.quad(lambda x: func_lambda(x)*func_sin(x,j),-np.pi,0)[0]+integrate.quad(lambda x: func_lambda(x)*func_sin(x,j),0,np.pi)[0])
				s=s+a_n*func_cos(t[i],j) + b_n*func_sin(t[i],j) 
			s_list.append(s) 

		return (t, s_list)


	def error_function(self,num_expan:int = 1,func_name:str='Square',abs_error:bool = True):
		"""Return a tuple object of the % of error between a square pulse function and his Fourier series aproximation, where 0 element is the time series and the 1 element is the y series"""
		escalon = self.function_square_pulse()
		aprox_fourier = self.fourier_series_aprox(num_expansion=num_expan,func_name='Square')

		if func_name == 'Square':
			escalon = self.function_square_pulse()
			aprox_fourier = self.fourier_series_aprox(num_expansion=num_expan,func_name='Square')
		elif func_name == 'Triangle':
			escalon = self.function_triangle_pulse()  
			aprox_fourier = self.fourier_escalon(num_expansion=num_expan,func_name='Triangle')
		elif func_name == 'Random_sin_cos':
			escalon = self.function_cos_sin_random_pulse() 
			aprox_fourier = self.fourier_escalon(num_expansion=num_expan,func_name='Random_sin_cos')
	
		

		#aprox_fourier = self.fourier_escalon(num_expansion=num_expan)
		error= []

		if abs_error ==True:
			for i in range(len(escalon[0])):
				er= np.abs(np.abs((aprox_fourier[1][i]-escalon[1][i]))/escalon[1][i]) 
				error.append(er)
		else:
			for i in range(len(escalon[0])):
				er=np.abs((aprox_fourier[1][i]-escalon[1][i]))/escalon[1][i]
				error.append(er)

		print(f"Tamaño de la lista error: {len(error)}")
		print(f"Tamaño de la listta error: {len(escalon[0])}")
		return(escalon[0],error)

##print("Inicio recorrido")
##f= Fourier()
##plt.subplot()
##plt.grid()
##print("Ya tengo el grid")
##plt.plot(f.error_function(10)[0],f.error_function(10)[1],"r--")
##plt.show()
