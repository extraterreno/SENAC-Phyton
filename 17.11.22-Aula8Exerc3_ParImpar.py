#[Exercício 3] Escreva um programa que jogue par ou impar com o computador.
# O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random


numeropc = random.randint(1, 2)
soma = 0
i = 0
resposta = None


while True:

    PI = str(input("Vamos jogar?? \n [ P ] - PAR \n [ I ] - IMPAR \n Escolha: ")).upper().strip()

    while PI not in 'PI':
        print("Escolha inválida!")
        PI = str(input("Vamos novamente... \n [ P ] - PAR \n [ I ] - IMPAR \n Escolha: ")).upper().strip()

    numero = int(input("Digite um número INTEIRO: "))
    soma = numeropc + numero

    if (soma % 2 == 0 and PI == "P") or (soma % 2 == 1 and PI == "I"):
       resultado = "VENCEU"
       i += 1
    else:
       resultado = "PERDEU"
       break


    print('=' * 20)
    print("O Cara mais esperto escolheu {0}!\n Você escolheu {2}!\n O resultado é {1}\n VOCE {3}".format(numeropc, soma, numero, resultado))
    print('=' * 20)


    while resposta not in 'SN':
        print("Resposta de Merda!")
        resposta = str(input(("Quer perder NOVAMENTE [S/N]??"))).upper().strip()


print("O Cara mais esperto escolheu {0}!\n Você escolheu {2}!\n O resultado é {1}\n VOCE {3}".format(numeropc, soma, numero, resultado))

print('#' * 40)
print(f"{'RESULTADO FINAL':^40}")
print(f"{'-' * 25:^40}")
print("Você teve {} vitórias consecutivas".format(i).center(40))
print('#' * 40),







