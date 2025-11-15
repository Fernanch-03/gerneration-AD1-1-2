a = True
b = False

print("Nor A",not a)

print("a ou b", a or b)

print("a e b", a and b)

## Exemplo de como usar or

idade = int(input("Digite a sua idade: "))
carteira = False

while(idade < 18 or carteira == False):
    pergunta_aniversario = input("Você ja fez aniversário?\n")
    if pergunta_aniversario.lower() == "sim":
        idade = idade + 1
        print("Então você tem ", idade)
    if carteira == False:
        pergunta_carteira = input("Você ja tirou a carteira?\n")
        if pergunta_carteira.lower() == "sim":
            carteira = True
    else:
        print("Ja tirou a carteira")
        
print("Dirigivel")