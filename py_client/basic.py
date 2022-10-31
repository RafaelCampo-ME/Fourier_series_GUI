import re
from urllib import request


import requests  

endpoint = "https://httpbin.org/anything"
 

get_response = requests.get(endpoint) #Metodo para traer API

print(f"Respuesta del servicio: {get_response}" ) 
print(f"Nuestra respuesta JSON \n{get_response.text)}"  

