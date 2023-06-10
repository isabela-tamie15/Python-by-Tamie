"""
2) Elaborar um programa que lê 3 valores (A, B e C) e exibe qual é o maior entre eles. 
Esse programa deve-se repetir 20 vezes.
"""
lista=[]
for r in range(1,3):
    for n in range(1,4):
        valor = float(input("Digite um número: "))
        lista.append(valor)
        maior = max(lista) 
    print(lista)  
    print(f"O maior número é {maior}")

# RESULTADO
"""
Digite um número: 1
Digite um número: 2
Digite um número: 3
[1.0, 2.0, 3.0]
O maior número é 3.0
Digite um número: 4
Digite um número: 5
Digite um número: 6
[1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
O maior número é 6.0
"""