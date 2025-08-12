import requests  # Biblioteca para fazer requisições HTTP

# Classe para consultar informações de um CEP usando a API ViaCEP
class Cep:
    def __init__(self, cep: str):
        self.cep = cep  # Armazena o CEP fornecido
        self.url = f"https://viacep.com.br/ws/{self.cep}/json/"  # URL da API
        self.dados = None  # Vai guardar a resposta

    def consultar(self):
        response = requests.get(self.url)  # Faz a requisição à API
        self.dados = response.text         # Guarda a resposta como texto
        return self.dados                  # Retorna os dados (JSON em string)
