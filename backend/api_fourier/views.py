##from rest_framework import generics
##from api_fourier.models import documentation
##from .serializer import docuSerializer

import sys
from pathlib import Path
from django.http import JsonResponse 
from .fourier_data import fourierSeries 
import numpy as np

#TODO: Change the API in order to bring all the necesary results to a format which javascrip can interpretate

class  pyfourierDataAPI():
    ##queryset = documentation.objects.filter(title="About Fourier Series GUI project") 
    ##serializer_class = docuSerializer

    def fourierList(request,*args,**kwargs):
        lista = [1,2,3,4]
        return JsonResponse({"list":lista})

    def fourierAprox(request,*args,**kwargs):        
        func_directory = { 'Square':   lambda x: x/np.abs(x)}
        expansion = 3
        f =  fourierSeries(function_name='Square',function_directory=func_directory,num_expansion=expansion)
        f = f.fourier_series_info()[0]
        f = list(f)
        return JsonResponse({"RESPUESTA":f})
