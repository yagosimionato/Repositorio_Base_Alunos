# 1. identificação de numero positivo, negativo ou zero
# crie um código em python que leia um numero e informe se ele é
# positivo, negativo ou zero

#1) entrada de dados
num = int(input("digite um  numero inteiro:"))
#2) condicional para verificar se o numero é maior ou igual a zero
if num >= 0:
    # condicional para checar se o número é zero
    if num == 0:
        print("O numero digitado é zero.") # informa que o numero é zero
    else: # informa que o numero é positivo
        print(f"o numero {num} é positivo.")
 # se o if for falso, entra no else e , informa que o  numero é negativo
else:
    print(f"O numero {num} é negativo.")