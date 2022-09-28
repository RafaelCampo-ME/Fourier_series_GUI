import numpy as np
import logging



class fourierSeries:


	def __init__(self,function_name,num_expansion = 1, function_directory) -> None:
		self.function_name = function_name
		self.num_expansion = num_expansion
		self.function_directory = function_directory 


	def time_series(range=np.pi,num_partitions=0.01)->list:
		return np.arange(-1*range, range,num_partitions) 


	def fourier_series_aprox(self)->list:
		logging.info("Fourier series has been calculated succesfully")
		return (list)

	
	def fourier_series_info(self):

			if self.function_name not in self.function_directory.keys():
				raise ValueError (f"{self.function_name} had not been implemented yet")
				
			if self.num_expansion < 0:
				raise ValueError (f"Number of Fourier expansion series must be greater that 0. Number used:{self.num_expansion}")
			
			self.fourier_series_aprox()
			


		 
	 

		


f = fourierSeries("Square",1)
f.fourier_series_info()











