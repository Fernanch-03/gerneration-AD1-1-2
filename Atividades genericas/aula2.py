'''
print("Digite o seu nome: ")
nome = input()
print("Digite a sua senha: ")
senha = input()

print(nome+", bom dia, sua senha registrada seria",senha)
'''
'''
nome_persona = int(input("Digite o seu nome: "))
idade_persona = int(input("Digite a sua idade: "))
altura_persona =float(input("Digite a ua altura: "))
print("Nome do usuário:",nome_persona,"\nIdade:",idade_persona,"\nAltura:",altura_persona)

falta_100 = 100 - idade_persona

print("falta",idade_persona,"anos para esta pessoa chegar aos 100 anos")

print(type(falta_100))

falta_100_txt = str(falta_100)

print(type(falta_100_txt))
'''

'''
# array (bem cedo alias wtf)

aluno = ["Ana","Bruno","Carlos","Daniela"]

print(aluno)

print(aluno[0])

print(aluno[-1])
'''


pessoa = {
    "nome":"Ana",
    "idade":25,
    "cidade":"São Vincente"}

print(pessoa["nome"])
print(pessoa.keys())
print(pessoa.values())