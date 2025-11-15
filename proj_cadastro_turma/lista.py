# Autor: Fernanod
# Projeto: Lista de varejo
# Versão: 1.0
# Descrição: Projeto que simula a atuação de um banco de dados, permitindo que o usuário insira, exclua e exiba frutas em um sistema.



frutas = []

# lista com apenas [] é uma lista vazia

# Usuario pode interagir com a lista das seguintes formas:
# Ver
# Adicionar 
# Excluir
# Sair

print("Bem vindo ao varejão Generation.")
while True:
    frutas_lower = [fruta.lower() for fruta in frutas]
    opcao = int(input("Selecione uma das opções para prosseguir:\n1- Adicionar fruta\n2- Excluir fruta\n3- Ver lista\n4- Sair\n"))
    match opcao:
        case 1:
            nova_fruta = str(input("Diga o nome da fruta a ser adicionada: "))
            if nova_fruta.lower() in frutas_lower:
                print("Fruta já existe no sistema\n")
            else:
                frutas.append(nova_fruta)
                print(frutas[-1],"adicionada com sucesso\n")
                
        case 2:
            print("Frutas cadastradas:")
            for posicao, cada_fruta in enumerate(frutas,start=1):
                print(posicao,"-",cada_fruta)
            fruta_excluida = str(input("Diga o nome da fruta a ser excluida: "))
            fruta_excluida = fruta_excluida.lower()
            if fruta_excluida in frutas_lower:
                frutas.pop(frutas_lower.index(fruta_excluida))
                print("Fruta excluida com suceso\n")
            else:
                print("Não existe essa fruta no sistema\n")
                
        case 3:
            print("Lista de todas as frutas:")
            for cada_fruta in frutas:
                print(cada_fruta)
            print("\n")
            
        case 4:
            print("Adeus")
            break
        
        case _:
            print("Você sabe ler?")