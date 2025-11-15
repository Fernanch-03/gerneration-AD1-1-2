# Autor: Fernando 
# Projeto: Caixa de Banco
# Versão: v1.2
# Descrição: Criação e manutenção bancária python
from funcoes import *

def main():
    conta1 = criarConta()
    while(True):
        print("Nome da conta: ",conta1["nome"],"\nValor na conta:", conta1["saldo"],"\n")
        opcao = int(input("Digite a opção desejada:\n1- Deposiar\n2- Sacar\n3- Encerrar\n"))
        match(opcao):
            case 1:#depositar
                dinheiro = int(input("Digite o valor a ser depositado: "))
                conta1["saldo"] = depositarDinheiro(conta1["saldo"],dinheiro)

            case 2:#sacar
                dinheiro = int(input("Digite o valor a ser sacado: "))
                if(dinheiro>conta1["saldo"]):
                    print("Valor não presente na conta, saque um valor menor")
                else:
                    conta1["saldo"] = sacarDinheiro(conta1["saldo"],dinheiro)

            case 3:#encerrar
                break
            case _:
                print("Foi um prazer ter você,"+conta1["nome"]," como cliente")
        
        
if __name__ == "__main__":
    main()