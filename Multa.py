#[Exercício 2] Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80 Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input("Qual a velocidade que passou no radar? "))
if velocidade > 80:
    multa = (velocidade - 80)*7
    print("Você foi MULTADO!")
    print("Sua multa será de R$ {:.2f}".format(multa))