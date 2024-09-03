import os
import requests

def start_consulta_mac(mac,):
    
    URL = "https://helpdesk.remotize.intelbras.com.br/api/devices/" + mac    

    token_file_path = os.path.join(os.path.dirname(__file__), '..', 'token.txt')
    with open(token_file_path, 'r') as file:
        token = file.read().strip()

    headers = {
    "Authorization": f"Bearer {token}"
    }
    
    response = requests.get(URL, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        print(data)
    
    else:
        print("Erro na requisição response")
    
    
start_consulta_mac(mac="30e1f1eaa287")