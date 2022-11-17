#[Exercício 2] Escreva um programa que o computador vai “pensar” em um número inteiro entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar o número, mostrando no final quantos palpites
# foram necessários para vencer.
import random

Nrandom = random.randint(1, 11)
#print("PC escolheu o {}".format(Nrandom))

chute = None

i = 0
while Nrandom != chute:
    chute = int(input("Adivinhe o número que o PC escolheu [1 a 10]? "))
    i += 1
print(f"Foram {i} tentativas!\nO número escolhido pela Skynet foi {Nrandom}")


