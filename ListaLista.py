#[Exercício 1] Escreva um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

#1) Quantas pessoas foram cadastradas;
#2) Uma listagem com as pessoas mais pesadas;
#3) Uma listagem com as pessoas mais leve.

aux = list()
cadastro = list() #[['A', 50], ['B', 110], ['C', 60]]
qtd = int(input("Entre com a quantidade de cadastros: "))


for i in range(0, qtd):
    aux.append(str(input("Entre com o nome: ")))
    aux.append(int(input("Entre com o peso: ")))
    cadastro.append(aux[:])
    aux.clear()

for i in range(0, len(cadastro)):
    if i == 0:
        maior_peso = menor_peso = cadastro[0][1]
    else:
        if cadastro[i][1] > maior_peso:
            maior_peso = cadastro[i][1]

#            mais_gordo = cadastro[i][0]
        if cadastro[i][1] < menor_peso:
            menor_peso = cadastro[i][1]
#            mais_magro = cadastro[i][0]



print(cadastro)
print(f"1) Quantidade de cadastros = {qtd}")
print(f'2) MAIOR peso cadastrado foi de {maior_peso} de {mais_gordo}, MENOR peso cadastrado foi de {menor_peso} foi de {mais_magro}')




