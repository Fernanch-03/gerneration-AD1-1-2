def menu():
    print("\nBem vindo ao calculador de proteinas!")
    print("Escolha uma opção")
    print("1 - Calcular proteinas\n2 - Calcular IMC\n")
    
def menu_objetivo():
    print("Qual a sua meta?")
    print("1 - Perder peso\n2 - Manter peso\n3 - Ganhar peso")

def calc_proteinas(peso, objetivo):
    if objetivo == 1:
        return peso * 2
    elif objetivo == 2:
        return peso * 1.6
    elif objetivo ==3:
        return peso * 1.8
    else:
        return None
    
def calc_imc(altura,peso):
    return peso/(altura**2)

def imc(valor_imc):
    if valor_imc < 18.5:
        return "Abaixo do peso"
    elif valor_imc <24.9:
        return "Peso normal"
    elif valor_imc <29.9:
        return "Sobre peso"
    else:
        "Obesidade"