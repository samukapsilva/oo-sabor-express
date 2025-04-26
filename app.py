from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')

restaurante_praca.reeber_avaliacao('Joao', 8)
restaurante_praca.reeber_avaliacao('Maria', 10)
restaurante_praca.reeber_avaliacao('Emy', 5)



def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()

