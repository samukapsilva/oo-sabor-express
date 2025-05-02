from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa
import requests
import json

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')

restaurante_praca.reeber_avaliacao('Joao', 8)
restaurante_praca.reeber_avaliacao('Maria', 10)
restaurante_praca.reeber_avaliacao('Emy', 5)

bebida_suco = Bebida ('Suco de Melancia', 5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()
sobremesa_pudim = Sobremesa('Pudim', 7.5,'','grande', 'Pudim de leite condensado')
sobremesa_pudim.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)
restaurante_praca.adicionar_no_cardapio(sobremesa_pudim)

def main():
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        dados_json = response.json()

        dados_restaurante = {}  # cria a lista vazia que vai receber cada array de restaurante, como se fosse um armario

        for item in dados_json:
            nome_restaurante = item['Company']  # pego o nome do restaurante que tem em cada item
            if nome_restaurante not in dados_restaurante:  # se eu não tiver já o nome do restaurante na lista...
                dados_restaurante[nome_restaurante] = []   # crio a lista para cada restaurante diferente que tiver nos dados, como se fossem gavetas do armario

            dados_restaurante[nome_restaurante].append({   # adiciono cada dicionario de cada produto por por restaurante
                "item":item['Item'],
                "price":item['price'],
                "description":item['description']
            })
    else:
        print(f'O erro foi {response.status_code}')

    for nome_restaurante, dados in dados_restaurante.items():
        nome_arquivo = f'{nome_restaurante}.json'
        with open(nome_arquivo, 'w') as arquivo_restaurante:
            json.dump(dados, nome_arquivo, ident=4)


    #Restaurante.listar_restaurantes()
    #restaurante_praca.exibir_cardapio


if __name__ == '__main__':
    main()

