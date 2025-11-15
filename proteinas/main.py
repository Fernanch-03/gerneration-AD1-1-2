# Autor: Fernando 
# Projeto: Calculadora de proteinas
# Versão: v1.0
# Descrição: Calculadora que realiza os calculos de quantas proeinas uma
# pessoa precisa, e também tem a opção de calcular o imc da pessoa

from funcoes import *

def main():
    menu()
    try:
        opcao = int(input("Escolha umaa opção: "))
        match(opcao):
            case 1:
                menu_objetivo()
                objetivo = int(input(""))
                peso = float(input("Qaul o seu peso em kg?\n"))
                resultado = calc_proteinas(peso, objetivo) 
                return print("Você precisa de",round(resultado,2))
            case 2:
                peso = float(input("Qaul o seu peso em kg?\n"))
                altura = float(input("Qaul a sua altura em metros?\n"))
                resultado = calc_imc(altura,peso)
                return print("Você está",imc(resultado))
            case _:
                print("Adeus")
                return False
    except(ValueError):
        print("Adeus")
        return False
                


if __name__ == "__main__":
    while main() is not False:
        pass
    