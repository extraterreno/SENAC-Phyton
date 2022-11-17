#[Exercício 1] Escreva um programa que leia o sexo de uma pessoa, mas só aceite ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.


sexo = str(input("Entre com o seu sexo [M/F]: ").upper().split()[0].strip())
    while sexo not in "MF":
        print("RESPOSTA INVALIDA!")
        sexo = (str(input("Entre com o seu sexo [M/F]: ").upper().split()[0].strip()))

print("--FIM--")

"""
    if sexo == "M":
        sexo = "Gênero Masculino"
        print("Você é {}".format(sexo))
    else:

        if sexo == "F":i
            sexo = "Gênero Femenino"
            print("Você é {}".format(sexo))
        else:
            print("Resposta Iválida, digite M ou F: ")
            sexo = str(input("Entre com o seu sexo: ").upper().split()[0].strip())



while sexo not in (MF):
    print(str(input("Resposta Invalida! \nEntre com o seu sexo: ")))
"""