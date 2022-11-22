#[Teste01] - Jogo da Forca: Escreva um programa que:
# - Tenha um um grupo de palavras de um determinado assunto; (ver como alimentar isso de forma random mais tarde)
# - NAO use LISTAS ou TUPLAS, podendo apenas usar um "choice" para sortear a palavra que será usada;
# -
## Por FAZER: Fzer o user escolher um número (tipo escolha) e Criar
# um embaralhamento dos tipos de palavras (cores, objetos...);


import random
from random import randint


print('+'*40)
print(f"{'Vamos Jogar FORCA?':^40}")
print('+'*40)

'''respSN = str(input(f"{'[S]im - [N]ão?':^40}".upper().strip()))

if respSN == "S":
    print("Começou...")
else:
    print("Porque STARTOU esse programa?\n --- FIM ---")'''

cores = ['VERMELHO', 'AZUL', 'VERDE', 'AMARELO']
cor = random.randint(0, len(cores)-1)                             # randomizar a palavra
print(f"a cor escolhida foi", cores[cor])                         # sorteada oculta / OCULTAR ESSA PARTE DEPOIS
                                                                  # E MOSTRAR A MATRIZ ESTILO FORCA _ _ _ _
c = 6
while c >= 1:
    letra = str(input(f"Você tem {c} chance(s) de erro\nEscolha uma letra: ")).upper().strip()
    if letra not in cores[cor]:
        print(f"A letra {letra} não está na palavra oculta")
        c -= 1
    else:
        print(f"Tem {letra} na palavra oculta. ")              # colocar quantas acertou - Você ACERTOU {} letra(s)!
#        for i in range(cor):
        print(cores[cor])




