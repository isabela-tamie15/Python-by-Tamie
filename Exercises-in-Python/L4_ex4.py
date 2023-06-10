"""
4) Elaborar um programa que leia uma lista que contenha 20 números inteiros e em seguida o
programa deve exibir o maior e o menor número.
"""
lista=[]
for r in range(1,5):
    numero = int(input("Digite um número: "))
    lista.append(numero)
print(lista)
x=max(lista)
y=min(lista)
print(f"O maior número é {x}")
print(f"O menor número é {y}")

# RESULTADO
"""
Digite um número: 5
Digite um número: 2
Digite um número: 6
Digite um número: 10
[5, 2, 6, 10]
O maior número é 10
O menor número é 2
"""
