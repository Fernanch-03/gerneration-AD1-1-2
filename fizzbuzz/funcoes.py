def normal():
    # Função normal do FizzBuzz, 
    # incluido um input do usuario para escolher quantos numeros mostrar
    fizzbuzz = ''
    r = int(input('Digite quantos numeros você deseja na sequencia do fizzbuzz: '))

    for i in range(1,r+1):
        if i%3 == 0:
            fizzbuzz += 'fizz'
        elif i%5 == 0:
            fizzbuzz += 'buzz'
        else:
            fizzbuzz += str(i)
        fizzbuzz += ' '
    return fizzbuzz
    

def complicado():
    # Versão mais complexa, permitindo customizar quais numeros substituirão
    # tais palavras. incluindo a feature anterior de selecionar 
    # uma range customizada
    fizzbuzz = ''
    tamanho = int(input("Digite quantos numeros serão mostrados no fizzbuzz: "))
    lista = [None]*int(input('Digite  quantos numeros você deseja serem usados como vetores para substituirem outros numeros: '))

    for i in range(len(lista)):
        valor = int(input('Digite um numero para ser verificado: '))
        chave = input('Digite a palavra para substituir os multiplos desse numero: ')
        lista[i] = {"valor": valor, "chave": chave}
        print("\n")
        
    lista = sorted(lista, key=lambda d: d['valor'])
        
    for i in range(1, (tamanho+1)):
        count = 0
        for j in range(len(lista)):
            if i%(lista[j]["valor"]) == 0:
                fizzbuzz += str(lista[j]["chave"])
            else: 
                count+= 1
        if(count == len(lista)):
            fizzbuzz += str(i)
        fizzbuzz += ' '
    return fizzbuzz

def beeMovie():
    # Versão com as mesmas features da anterior, porem 
    # adicionando a funcionalidade de ler arquivos e 
    # transformar em arrays, nesse caso, o script em inglês do 
    # filme "Bee Movie"
    path = "fizzbuzz/assets/Bee Movie Script"
    try:
        falas = fileReader(path)
        fizzbuzz = ""
        tamanho = int(input("Digite quantos numeros serão mostrados no fizzbuzz: "))
        lista = [None]*int(input("Quantas Falas do filme 'bee movie' você deseja usar para substituir os numeros: "))
        for i in range(len(lista)):
            valor = int(input("Digite um numero para ser verificado: "))
            chave = int(input("Digite a posição da fala do 'Bee Movie' a substituir os multiplos desse numero:"))
            lista[i] = {"valor": valor, "chave": falas[chave]}
            print("\n")
        lista = sorted(lista, key=lambda d: d['valor'])
            
        for i in range(1, (tamanho+1)):
            count = 0
            for j in range(len(lista)):
                if i%(lista[j]["valor"]) == 0:
                    fizzbuzz += str(lista[j]["chave"])
                else: 
                    count+= 1
            if(count == len(lista)):
                fizzbuzz += str(i)
            fizzbuzz += ' | '
        return fizzbuzz
    except FileNotFoundError:    
        print("Arquivo não encontrado")
    
# Funções Recursos
def fileReader(filename: str) -> list[str]:
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]
    
