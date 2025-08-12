import sys
import requests

# Função para verificar se a internet está disponível
def check_internet(url="https://google.com.br", timeout=3):
    try:
        response = requests.get(url, timeout=timeout)  # Tenta acessar o site
        return response.status_code == 200             # Retorna True se sucesso
    except requests.RequestException:
        return False                                   # Retorna False se erro
    
# Testa a conexão antes de continuar
if not check_internet():
    print("❌ Sem conexão ou resposta inválida do servidor.")
    sys.exit(1)  # Encerra o programa
else:
    print("✅ Internet disponível e servidor respondeu com sucesso.")
