#[Exercício 1] Escreva um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

#1) Quantas pessoas foram cadastradas;
#2) Uma listagem com as pessoas mais pesadas;
#3) Uma listagem com as pessoas mais leve.

#aux = list()
cadastro = [['A', 100], ['B', 80], ['C', 60]] #list()
#qtd = int(input("Entre com a quantidade de cadastros: "))


"""for i in range(0, qtd):
    aux.append(str(input("Entre com o nome: ")))
    aux.append(int(input("Entre com o peso: ")))
    cadastro.append(aux[:])
    aux.clear()"""

"""print(cadastro)
print(cadastro[0])
print(cadastro[1])
print(cadastro[2])"""

for pessoa in cadastro:
    for i in range(0, 2):
        print(f"{pessoa[i]}")


"""maior_peso = cadastros[1]

for peso in cadastros:
    if peso[1] > maior_peso:
        maior_peso = peso[1]
    else:
        maior_peso = maior_peso

print(cadastros)
print(f"1) Quantidade de cadastros = {qtdcadastros}")
print(maior_peso)
"""



