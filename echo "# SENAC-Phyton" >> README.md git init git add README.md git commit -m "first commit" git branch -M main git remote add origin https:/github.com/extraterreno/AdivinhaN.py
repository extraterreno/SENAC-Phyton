#[Exercício 1] Escreva um programa que o computador pensará em um número entre 0 e 5.
# Em seguida, o usuário deverá adivinhar esse valor. Caso o usuário acerte, retorne “VENCEU”,
# caso perca, retorne “PERDEU”.
import random
import time

print("="*20)
print("{:^20}".format("ADIVINHACAO"))
print("="*20)

NPC = random.randint(0, 5)
NH = int(input("Digite um número entre 0 e 5: "))

print("PROCESSANDO...")
time.sleep(2)
print("Escolheu {}, o número que o PC escolheu foi {}".format(NH, NPC))


if NH == NPC:
    print("Você GANHOU")
else:
    print("TENTE NOVAMENTE!")