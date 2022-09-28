import numpy as np
import logging
from scipy import integrate


class fourierSeries:
	"""_summary_: Retrurns a tuple of list that contains the points of the original function and his fourier series aproximation
	"""


	def __init__(self,function_name:str, num_expansion:int = 1, function_directory:dict={}) -> None:
		self.function_name = function_name
		self.num_expansion = num_expansion
		self.function_directory = function_directory 


	def __time_series(range=np.pi,num_partitions=0.01)->list:
		return np.arange(-1*range, range,num_partitions) 


	def __fourier_series_aprox(self,time:list=[], function_name:str='Square', num_expansion:int=1)->list:
		 
		func_lambda= self.function_directory[function_name]
		func_cos = lambda x,y: np.cos(y*x)
		func_sin = lambda x,y: np.sin(y*x)
		a_0 =  (1/np.pi) * (integrate.quad(func_lambda,-1*np.pi,0)[0]+integrate.quad(func_lambda,0,np.pi)[0])

		s_list = []
		for i in range(len(t)):
			sumatory = 0
			for j in range(num_expansion):
				
				a_n = (1/np.pi)*(integrate.quad(lambda x: func_lambda(x)*func_cos(x,j),-np.pi,0)[0]+integrate.quad(lambda x: func_lambda(x)*func_cos(x,j),0,np.pi)[0])
				b_n = (1/np.pi)*(integrate.quad(lambda x: func_lambda(x)*func_sin(x,j),-np.pi,0)[0]+integrate.quad(lambda x: func_lambda(x)*func_sin(x,j),0,np.pi)[0])
				sumatory=sumatory+a_n*func_cos(time[i],j) + b_n*func_sin(time[i],j) 
			s_list.append(sumatory+a_0) 
		print("Message: The Fourier aproximation has been calculated.")
		return s_list 




		logging.info("Fourier series has been calculated succesfully")
		return ()

	def __fourier_exp_series_aprox(self)->list:
		pass
	

	def __fast_fourier_series()->list:
		return ()


	def __error_function()->list:
		return ()


	def __average_error()->float:
		return()


	def fourier_series_info(self,aprox_type:str = 'LFS'):

			if self.function_name not in self.function_directory.keys():
				raise ValueError (f"{self.function_name} had not been implemented yet")
				
			if self.num_expansion < 0:
				raise ValueError (f"Number of Fourier expansion series must be greater that 0. Number used:{self.num_expansion}")
			
			if aprox_type not in ('LFS','FFT'):
				raise ValueError (f"{aprox_type} is a unsupported aproximation type.")


			time = self.__time_series()

			if aprox_type == 'LFS':
				s = self.__fourier_series_aprox(time, self.function_name,self.num_expansion)
			else:
				s = self.__fast_fourier_series(time)
			
			return time,s

	def change_num_expansions(self)-> tuple:
		pass
			

