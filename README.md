# Consulta de CEP via API ViaCEP

## Descrição do projeto
Este projeto é uma aplicação simples em Python que permite consultar informações de um CEP brasileiro utilizando a API pública ViaCEP. O usuário digita um CEP válido com 8 números, e o programa retorna os dados correspondentes ao CEP, como endereço, bairro, cidade e estado, em formato JSON.

Além disso, o programa verifica se há conexão com a internet e se o servidor está respondendo antes de fazer a consulta, garantindo maior robustez no uso.

## Como instalar e executar

### Requisitos
- Python 3.x instalado
- Biblioteca `requests` instalada (`pip install requests`)

### Instalação
1. Clone ou faça download deste repositório.
2. Navegue até o diretório do projeto no terminal.

### Execução
No terminal, execute o arquivo principal:
```bash
python main.py
```

O programa pedirá para você digitar um CEP com 8 números e exibirá as informações consultadas.

## Exemplo de uso
```bash
Digite o seu CEP: 01001000
{
  "cep": "01001-000",
  "logradouro": "Praça da Sé",
  "complemento": "lado ímpar",
  "bairro": "Sé",
  "localidade": "São Paulo",
  "uf": "SP",
  "ibge": "3550308",
  "gia": "1004",
  "ddd": "11",
  "siafi": "7107"
}
```

## Contribuições futuras
- Implementar tratamento de erros mais detalhado para CEPs inválidos ou não encontrados.
- Adicionar suporte para consultar CEPs de outros países.
- Criar uma interface gráfica para facilitar o uso.
- Salvar históricos de consultas para análises futuras.

---

Se você quiser contribuir, fique à vontade para abrir issues ou pull requests!