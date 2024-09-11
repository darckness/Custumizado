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
        assoc_status = response.json()['assoc_status']
        version = response.json()['fw_version']
        return assoc_status, version
    else:
        nomac = 10
        return nomac
        
mac = "30e1f1eaa287"

consulta_mac(mac)