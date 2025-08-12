import requests

class Cep:
    def __init__(self, cep: str):
        self.cep = cep
        self.url = f"https://viacep.com.br/ws/{self.cep}/json/"
        self.dados = None

    def consultar(self):
        response = requests.get(self.url)
        self.dados = response.text
        return self.dados
