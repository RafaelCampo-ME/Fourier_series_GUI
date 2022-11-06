##from rest_framework import generics
##from api_fourier.models import documentation
##from .serializer import docuSerializer

import sys
from pathlib import Path
from django.http import JsonResponse 
from .fourier_data import fourierSeries 
import numpy as np
from datetime import datetime


#TODO: Change the API in order to bring all the necesary results to a format which javascrip can interpretate

class  pyfourierDataAPI():
    ##queryset = documentation.objects.filter(title="About Fourier Series GUI project") 
    ##serializer_class = docuSerializer

    def fourierList(request,*args,**kwargs):
        lista = [1,2,3,4]
        return JsonResponse({"list":lista})

    def fourierAprox(request,*args,**kwargs):
        start_time = str(datetime.now())         
        func_directory = { 'Square':   lambda x: x/np.abs(x)}
        expansion = 5
        f =  fourierSeries(function_name='Square',function_directory=func_directory,num_expansion=expansion)
        f = f.fourier_series_info()
        time = list(f[0])
        original_function = list(f[1])
        aprox_serie = list(f[2])
        error_serie = list(f[3])
        avg_error = float(f[4])
        now = str(datetime.now()) 
        return JsonResponse({"Fourier_aprox_python": {
            "Time_series":time,
            "original_function":original_function,
            "aproximation":aprox_serie,
            "error_serie":error_serie,
            "avg_error":avg_error},
            "Request_creation_time": start_time,
            "Request_completion_time":now
            })
