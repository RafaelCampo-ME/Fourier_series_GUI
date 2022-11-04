import re
from urllib import request
import requests  

endpoint = "http://localhost:8000/api-home" ##This is my localhost with the 8000 port 

get_response = requests.get(endpoint,params={"abc":123}, json={"query":"Hello World"}) #Metodo para traer API

print(f"Respuesta del servicio: {get_response}" )  
print(f"Nuestra respuesta JSON \n{get_response.text}" ) 



#def api_home(request, *args, **kwargs):
#    body = request.body
#    data = {}
#    try:
#        data = json.loads(body)
#    except:
#        pass
#    print(data)
#    data['headers'] = request.headers
