import os
import requests

def consulta_mac(mac):
    URL = "https://helpdesk.remotize.intelbras.com.br/api/devices/" + mac    

    token_file_path = os.path.join(os.path.dirname(__file__), '..', 'token.txt')
    with open(token_file_path, 'r') as file:
        token = file.read().strip()

    headers = {
    "Authorization": f"Bearer {token}"
    }
    
    response = requests.get(URL, headers=headers)
    
    if response.status_code == 200:
        status = response.json()['profile']['status']
        client = response.json()['profile']['name']
        version = response.json()['fw_version']
        
        #print(status, client, version)

        return status, version, client
    else:
        nomac = 10
        return nomac
