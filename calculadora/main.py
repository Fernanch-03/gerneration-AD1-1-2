from funcoes import *
def main():
    try:
        opcao = int(input("\nBem vindo a calculadora, por favor selecione uma opção:\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Potência\n6 - Raiz\n7 - Encerrar\n"))
        match(opcao):
            case 1:
                print("Digite os valores a serem somados")
                n1 = int(input(""))
                n2 = int(input(""))
                return print(soma(n1,n2))
            case 2:
                print("Digite os valores a serem subtraidos")
                n1 = int(input(""))
                n2 = int(input(""))
                return print(subtrcao(n1,n2))
            case 3:
                print("Digite os valores a serem multiplicados")
                n1 = int(input(""))
                n2 = int(input(""))
                return print(multiplicacao(n1,n2))
            case 4:
                n1 = int(input("Digite o dividendo: "))
                n2 = int(input("Digite o divisor: "))
                return print(divisao(n1,n2))
            case 5:
                n1 = int(input("Digite a base: "))
                n2 = int(input("digite o expoente: "))
                return print(potencia(n1,n2))
            case 6:
                n1 = int(input("Digite o indice: "))
                n2 = int(input("Digite o radicando: "))
                return print(raiz(n1,n2))
            case 7:
                return False
            case _:
                return print("Wrong way, turn back now")
    except(ValueError):
        return print("Por favor digite uma das opções")
    
if __name__ == "__main__":
    while main() is not False:
        pass
    