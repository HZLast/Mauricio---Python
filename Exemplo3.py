ingresso = int(input("Qual ingresso você deseja? (1 - VIP 2 - Standard)"))
pipoca = int(input("Quer o combo com pipoca? (1 - SIM 2 - NÂO)"))
if ingresso == 1:
    if pipoca == 1:
        print("Valor a pagar: 110 reais")
    else:
        print("Valor a pagar: 80 reais")
else:
    if pipoca == 1:
        print("Valor a pagar 70 reais")
    else:
            print("Valor a pagar: 40 reais")