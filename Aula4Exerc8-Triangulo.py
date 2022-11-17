#[Exercício 8] Escreva um programa que leia o comprimento de três retas e diga ao usuário se
# elas podem ou não formar um triângulo.

from os import system

L1 = float(input("Entre com o primeiro lado: "))
L2 = float(input("Entre com o segundo lado: "))
L3 = float(input("Entre com o terceiro lado: "))

V1 = (L1 < L2 + L3)
V2 = (L2 < L1 + L3)
V3 = (L3 < L1 + L2)

system('cls')
if V1 and V2 and V3:
    print("FORMA UM TRIANGULO")
else:
    print("NAO FORMA")


