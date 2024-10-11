import requests
import time

def reset_padrao():
    URL_reset = ""
    URL = ""
    
    data = {
        "username": "admin",
        "password": "admin"
    }

    headers = {
        "Content-Type": "application/json"
    }

    while True:
        try:
            # Faz a requisição para pegar o token
            response_telnet = requests.post(URL, json=data, headers=headers, timeout=5)
            token = response_telnet.json().get('token')

            if token:
                # Data e headers para o reset
                data_reset = {
                    "actionID": 2
                }

                headers_reset = {
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json"
                }

                # Faz o reset com o token obtido
                response_reset = requests.post(URL_reset, json=data_reset, headers=headers_reset)
                print(f"Reset feito: {response_reset.status_code}")
            else:
                print("Falha ao obter o token")

        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")

        # Aguarda 1 segundo antes de rodar novamente
        time.sleep(1)

# Chama a função para rodar em loop
reset_padrao()