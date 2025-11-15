# Autor: Fernando 
# Projeto: FizzBuzz
# Versão: v1.4
# Descrição: As várias maneiras de como fazer uma aplicação lógica fizzbuzz 

from funcoes import *


def main(opcao):
    match opcao:
        case 1:
            normal()
        case 2:
            complicado()
        case 3:
            beeMovie()
        case _:
            print("Selecione um input valido")

if __name__ == "__main__":
    main(int(input("Quer usar o programa:\n1 (Normal)\n2 (Mais personalizavel)\n3 (Bee Movie?)\n")))