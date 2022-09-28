import numpy as np
import logging
from scipy import integrate


class fourierSeries:


	def __init__(self,function_name:str, num_expansion:int = 1, function_directory:dict={}) -> None:
		self.function_name = function_name
		self.num_expansion = num_expansion
		self.function_directory = function_directory 


	def time_series(range=np.pi,num_partitions=0.01)->list:
		return np.arange(-1*range, range,num_partitions) 


	def fourier_series_aprox(self)->list:
		logging.info("Fourier series has been calculated succesfully")
		return (list)
	

	def fast_fourier_series()->list:
		return ()


	def error_function()->list:
		return ()


	def average_error()->float:
		return()


	def fourier_series_info(self,aprox_type:str = 'LFS'):

			if self.function_name not in self.function_directory.keys():
				raise ValueError (f"{self.function_name} had not been implemented yet")
				
			if self.num_expansion < 0:
				raise ValueError (f"Number of Fourier expansion series must be greater that 0. Number used:{self.num_expansion}")
			
			if aprox_type not in ('LFS','FFT'):
				raise ValueError (f"{aprox_type} is a unsupported aproximation type.")

			t = self.time_series()

			if aprox_type == 'LFS':
				s = self.fourier_series_aprox()
			else:
				s = self.fast_fourier_series()
			
			return t,s
			

