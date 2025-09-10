# 3. classificação por idade
# faça um programa que leia a idade de uma pessoa e classifique-a em:
# criança : menor que 12 anos
# adolescente: entre 12 a 17 anos
# adulto: maior ou igual a 18 anos
# utilize a estrutura de condicional aninhada
idade= int(input("Digite a sua idade:"))
if idade > 0:
    if idade >= 18:
        print(f"voce tem {idade} anos e é adulto.")
    elif 12 <= idade<=17:
        print(f"voce tem {idade} e é adolescente.")
    else:
        print(f"voce tem {idade} e é uma criança.")
else:
        print("Idade nao pode ser negativa, digite uma iade valida.")