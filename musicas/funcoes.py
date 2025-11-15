# Para eu ler uma base de dados, preciso importar um modulo que lê
import csv

# agora eu vou dizer onde está o arquivo
path = "musicas/assets/musicas.csv"

def lerMusicas():
    print("--------------- Lista de Musicas -----------------------")
    try:
        with open(path,"r",encoding="utf-8") as arquivo_musica:
        # O comando with open perimite que eu abra um arquivo, mas para 
        # isso, deo informar:
        # 1- O path
        # 2- Read add or write 
        # 3- colocar a codificação (se nescessário), como uft-8
            leitor = csv.reader(arquivo_musica)
            # Para pular o cabeçalho, eu posso usar o next(variavel)
            # para pular a primeira linha
            next(leitor)
            
            for linha in leitor:
                if linha:
                    titulo,artista,ano,genero,duracao_segundos = linha
                    print("Musica",titulo+", criada por",artista)
    except FileNotFoundError:    
        print("Arquivo não encontrado")

lerMusicas()