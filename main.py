from cep.cep import Cep  # Importa a classe Cep de um módulo chamado 'cep/cep.py'

# Função para pedir o CEP do usuário e validar a entrada
def pedir_cep():
    while True:
        num_cep = input("Digite o seu CEP: ")
        # Verifica se tem exatamente 8 caracteres e se são apenas números
        if len(num_cep) == 8 and num_cep.isdigit():
            return num_cep
        print("CEP inválido! Por favor, digite exatamente 8 números.")

# Função principal do programa
def main():
    cep_digitado = pedir_cep()  # Solicita CEP válido
    cep = Cep(cep_digitado)     # Cria um objeto Cep
    print(cep.consultar())      # Consulta e imprime os dados retornados pela API

# Garante que o código só execute se o script for executado diretamente
if __name__ == "__main__":
    main()
