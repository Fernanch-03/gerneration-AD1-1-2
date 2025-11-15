def criarConta():
    id = int(input("Digite o id: "))
    nome = str(input("Digite o nome: "))
    
    nova_conta = {"id" : id,"nome" : nome,"saldo" : 500}
    return nova_conta

def depositarDinheiro(saldo,valor):
    return saldo+valor
    
def sacarDinheiro(saldo,valor):
    return saldo-valor
    