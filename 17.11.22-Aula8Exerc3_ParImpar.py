#[Exercício 3] Escreva um programa que jogue par ou impar com o computador.
# O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random


numeropc = random.randint(1, 2)
soma = 0
i = 0


while True:
    PI = str(input("Vamos jogar?? \n [ P ] - PAR \n [ I ] - IMPAR \n Escolha: "))
    numero = int(input("Digite um número INTEIRO: "))
#    print(PI)
    soma = numeropc + numero
#    print(numeropc)

    if (soma % 2 == 0 and PI == "P") or (soma % 2 == 1 and PI == "I"):
       resultado = "VENCEU"
       i += 1
    else:
       resultado = "PERDEU"
       break

    print("O Cara mais esperto escolheu {0}!\n Você escolheu {2}\n O resultado é {1} \n VOCE {3}".format(numeropc, soma, numero, resultado))

print('#' * 20)

print("Você teve {} vitórias consecutivas".format(i))
print("O Cara mais esperto escolheu {0}!\n Você escolheu {2}!\n O resultado é {1} \n VOCE {3}".format(numeropc, soma,
                                                                                                         numero,
                                                                                                         resultado))

while PI not in 'PI':
    print("Escolha inválida!")
    PI = str(input("Vamos jogar?? \n [ P ] - PAR \n [ I ] - IMPAR \n Escolha: "))




