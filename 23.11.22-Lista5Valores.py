#[Exercício 1] [DESAFIO] Escreva um programa que leia 5 valores e guarde-os dentro de uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

vetor = list()

#while True:
for i in range(0, 5):
    vetor.append(int(input(f"{i + 1}) Digite um valor inteiro: ")))
#print(f"posicao = ", j)
maior = vetor[0]
j = 1
while j <= 5:
    if vetor[j] > maior:
        maior = vetor[j]
    else:
        break
print(f"Vetor = {vetor}")
print(f"Maior valor do Vetor = {maior} na posicão ...")

