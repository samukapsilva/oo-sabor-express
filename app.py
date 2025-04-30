from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

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
    #Restaurante.listar_restaurantes()
    restaurante_praca.exibir_cardapio


if __name__ == '__main__':
    main()

