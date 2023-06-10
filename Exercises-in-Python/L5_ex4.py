"""
4) Elabore um programa que leia um nº inteiro e mostre uma mensagem indicando se 
este número é múltiplo de 3 e se é positivo ou negativo. 
Esse programa deve-se repetir 10 vezes.
"""
for n in range(1,3):
    n1=int(input("Digite um número: "))
    
    if n1%3==0 and n1>0:
        print("Número positivo e múltiplo de 3")
    elif n1%3==0 and n1<0:
        print("Número negativo e múltiplo de 3")
    elif n1%3 != 0 and n1>0:
        print("Número positivo e não múltiplo de 3")
    elif n1%3 != 0 and n1<0:
        print("Número negativo e não múltiplo de 3")

# RESULTADO
"""
Digite um número: -3
Número negativo e múltiplo de 3
Digite um número: 3
Número positivo e múltiplo de 3
""" 