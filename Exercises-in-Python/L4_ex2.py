"""
2) Elaborar um programa que leia uma lista de 6 números inteiros e mostre cada número 
juntamente com a sua posição na lista.
"""
lista=[]
for n in range(1,3):
    valor=int(input("Digite um número: "))
    lista.append(valor)
for n in lista:
    print(f"O índice {lista.index(n)} é igual ao número {n}")

# lista.index(n): busca o índice pelo index dentro da lista.
# n: é o elemento dentro da lista.
# nos 4 luagres precisa ser 'n' para ser parte da lista.

# RESULTADO
"""
Digite um número: 5
Digite um número: 3
O índice 0 é igual ao número 5
O índice 1 é igual ao número 3
"""