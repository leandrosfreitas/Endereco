from cep.cep import Cep

def pedir_cep():
    while True:
        num_cep = input("Digite o seu CEP: ")
        if len(num_cep) == 8 and num_cep.isdigit():
            return num_cep
        print("CEP inválido! Por favor, digite exatamente 8 números.")

def main():
    cep_digitado = pedir_cep()
    cep = Cep(cep_digitado)
    print(cep.consultar())

if __name__ == "__main__":
    main()
