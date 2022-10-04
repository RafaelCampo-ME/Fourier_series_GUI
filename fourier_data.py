import numpy as np
import logging
from scipy import integrate
from scipy.fft import fft


class fourierSeries:
	"""_summary_: Retrurns a tuple of list that contains the points of the original function and his fourier series aproximation
	"""

	def __init__(self,function_name:str, num_expansion:int = 1, function_directory:dict={}) -> None:
		self.function_name = function_name
		self.num_expansion = num_expansion
		self.function_directory = function_directory 
		


	def __time_series(self,range=np.pi,num_partitions=0.01)->list:
		return np.arange(-1*range, range,num_partitions) 


	def __fourier_series_aprox(self,time:list=[], function_name:str='Square', num_expansion:int=1)->list:
		"""_summary_

		Args:
			time (list, optional): _description_. Defaults to [].
			function_name (str, optional): _description_. Defaults to 'Square'.
			num_expansion (int, optional): _description_. Defaults to 1.

		Returns:
			list: _description_
		"""

		func_lambda= self.function_directory[function_name]
		func_cos = lambda x,y: np.cos(y*x)
		func_sin = lambda x,y: np.sin(y*x)
		a_0 =  (1/np.pi) * (integrate.quad(func_lambda,-1*np.pi,0)[0]+integrate.quad(func_lambda,0,np.pi)[0])

		time = self.__time_series(np.pi,0.01)

		s_list = []
		for i in range(len(time)):
			sumatory = 0
			for j in range(num_expansion):
				a_n = (1/np.pi)*(integrate.quad(lambda x: func_lambda(x)*func_cos(x,j),-np.pi,0)[0]+integrate.quad(lambda x: func_lambda(x)*func_cos(x,j),0,np.pi)[0])
				b_n = (1/np.pi)*(integrate.quad(lambda x: func_lambda(x)*func_sin(x,j),-np.pi,0)[0]+integrate.quad(lambda x: func_lambda(x)*func_sin(x,j),0,np.pi)[0])
				sumatory=sumatory+a_n*func_cos(time[i],j) + b_n*func_sin(time[i],j) 
			s_list.append(sumatory+a_0) 
		print("Message: The Fourier aproximation has been calculated.")
		return s_list 


	def __fourier_exp_series_aprox(self)->list:
		pass
	

	def __fast_fourier_series(time)->list:
		return fft(time)


	def __error_function(self,time,fourier)->list:
		error = []
		for i in range(len(time)):
			error.append((fourier[i]-time[i])/time[i]) 
		return error


	def __average_error(self,error:list)->float:
		avg_error = sum(error)/ len(error)
		return avg_error


	def fourier_series_info(self,aprox_type:str = 'LFS'):

			if self.function_name not in self.function_directory.keys():
				raise ValueError (f"{self.function_name} had not been implemented yet")
			if self.num_expansion < 0:
				raise ValueError (f"Number of Fourier expansion series must be greater that 0. Number used:{self.num_expansion}")
			if aprox_type not in ('LFS','FFT'):
				raise ValueError (f"{aprox_type} is a unsupported aproximation type.")

			time = self.__time_series(np.pi,0.01)
			origin_function =   self.function_directory[self.function_name](time)
			if aprox_type == 'LFS':
				serie = self.__fourier_series_aprox(time, self.function_name,self.num_expansion)
			else:
				serie = self.__fast_fourier_series(time)
			error = self.__error_function(time,serie)
			avg_error = self.__average_error(error)

			return time,origin_function,serie, error, avg_error

	def change_num_expansions(self)-> tuple:
		pass
			

