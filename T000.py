#tratamento contra donkeys
while True:
    resposta = str(input("Deseja continuar [S/N]?")).upper().strip()[0]
    while resposta not in 'SN':
        resposta = str(input("\nRESPOSTA INVÁLIDA. \nDeseja continuar [S/N]?")).upper().strip()[0]
    if resposta == 'N':
         break

print('--FIM--')
