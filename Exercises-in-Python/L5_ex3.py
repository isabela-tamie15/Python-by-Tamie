"""
3) Elaborar um programa que lê 20 números inteiros e para cada número inserido exibir 
se é par ou ímpar.
"""
lista=[]
for n in range(1,3):
    num = int(input("Digite o número: "))
    lista.append(num)
    if num%2 == 0:
        print("O número é par")
    else:
        print("O número é impar")

# RESULTADO
"""
Digite o número: 1
O número é impar
Digite o número: 2
O número é par
"""