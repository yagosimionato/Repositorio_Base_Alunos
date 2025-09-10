# 2. paridade e tamanho  do numero

# crie um codigo que receba um numero inteiro e informe:
# - se é par ou ímpar
# - e, ao mesmo tempo, se é maior que 10 ou menor ou igual a 10
# utilize condicionais aninhadas para organizar as verificadas
num = int(input("digite um numero inteiro: "))

if num % 2 == 0 :
  if num >= 10:
   print(f"O numero {num} é par e maior que 10.")
else:
  print(f"o numero {num} é par menor que 10.")
 else:
if num >=10:
   print(f"o  numero {num} é impar e maior que 10")
else:
   print(f"o numero {num} é impar menor que 10")
