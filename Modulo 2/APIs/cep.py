# crie uma api que consulte o cep e informe o endereço

# iniciamos fazendo a importação da biblioteca requests
import requests

# indicamos a url para consulta da api
cep = input("digite o cep (somente numeros):") # usuario informa o cep que deseja consultar
url = f'https://viacep.com.br/ws/{cep}/json/' # endereço de url formatado para pesquisa do cep

# fazemos a requisição
resposta = requests.get(url) # aqui estamos fazendo a requisição

if resposta.status_code == 200:
    dados = resposta.json()
    if 'erro' not in dados:
        print(f'CEP: {dados[cep]}')
        print(f'logradouro: {dados['logradouro']}')
        print(f'bairro: {dados['bairro']}')
        print(f'cidade: {dados['localidade'] }')
        print(f'estado: {dados['uf']} ')
    else:
        print('cep nao foi encontrado')
else:
    print(f'erro na requisição:{resposta.status_code}')
    print(resposta.content)