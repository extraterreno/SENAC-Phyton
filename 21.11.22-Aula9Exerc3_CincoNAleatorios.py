#[Exercício 3] Escreva um programa que vai gerar cinco números aleatórios e colocar dentro em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

myTuple = tuple(randint(0, 6) for i in range(0, 5)) #
                                                    # Números gerados aleatoriamente
print(myTuple)                                      #