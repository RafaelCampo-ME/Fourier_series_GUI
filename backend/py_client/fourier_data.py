import requests

endpoint ="http://127.0.0.1:8000/"

get_response = requests.get(endpoint,params={'Type':'Square','Num_aprox':1})

print(f"Get response method status code: {get_response.status_code}" )
print(f"Get response method's return headers{get_response.headers}")