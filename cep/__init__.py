import sys
import requests

def check_internet(url="https://google.com.br", timeout=3):
    try:
        response = requests.get(url, timeout=timeout)
        return response.status_code == 200
    except requests.RequestException:
        return False
    
if not check_internet():
    print("❌ Sem conexão ou resposta inválida do servidor.")
    sys.exit(1)
else:
    print("✅ Internet disponível e servidor respondeu com sucesso.")
