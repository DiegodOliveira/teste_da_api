import requests
import json

from requests import get

API_KEY = input("Digite a key a ser utilizada:")
arquivo_desejado = input("Digite o nome do arquivo a ser lido:")

dados = []
with open(arquivo_desejado, "r", encoding="utf-8") as arquivo:
    for linha in arquivo.readlines():
        linha = linha.replace("/n","").replace(" ","")
        novo_formato = linha.split(",")
        dados.append(novo_formato)

for info in dados:
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={info[3]}&lon={info[2]}&appid={API_KEY}'
    resposta = get(url)

    while resposta.status_code == 200:
     print(f'Gerando: {info[0]}.json')
     with open(info[0] + '.json', 'w', encoding='UTF-8') as arquivo:
          dados_json = json.dumps({info[1]: resposta.json()}, indent=4)
          arquivo.write(dados_json)

          break

