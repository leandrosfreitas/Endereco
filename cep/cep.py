import requests  # Biblioteca para fazer requisições HTTP

# Classe para consultar informações de um CEP usando a API ViaCEP
class Cep:
    def __init__(self, cep: str):
        self.cep = cep  # Armazena o CEP fornecido
        self.url = f"https://viacep.com.br/ws/{self.cep}/json/"  # URL da API ViaCEP para consulta
        self.dados = None  # Variável para armazenar a resposta da API

    def consultar(self):
        """
        Faz a consulta do CEP na API ViaCEP.
        Retorna um dicionário com os dados do endereço.
        Lança ConnectionError se o status HTTP for diferente de 200.
        Lança ValueError se o CEP não for encontrado.
        """
        response = requests.get(self.url)
        
        if response.status_code != 200:
            raise ConnectionError(f"Erro na requisição: status code {response.status_code}")
        
        self.dados = response.json()
        
        if str(self.dados.get("erro")).lower() == "true":
            return "CEP não encontrado."

        return self.dados
