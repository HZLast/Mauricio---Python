numero = int(input("Digite um numero:"))
resto = numero % 15
if(resto == 0):
    print("O numero",numero," é divisivel simultaneamente por 3 e por 5.")
else:
    print("O numero ",numero," não é divisível simultaneamente por 3 e por 5.")