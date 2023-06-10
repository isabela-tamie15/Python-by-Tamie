"""
9) Elaborar um programa para ler uma lista A de 15 elementos e um valor X. O programa deve 
copiar para a lista B somente os elementos de A que são maiores que X. 
Exibir no final a lista B. 
"""
lisA=[]
lisB=[]
for r in range(0,4):
    lisA.append(float(input("Informe um número: ")))
    x=float(input("Informe o valor de x: "))
for c in lisA:
    if (c >x):
       lisB.append(c)
print("lista B", lisB)

# RESULTADO
"""
Informe um número: 8
Informe o valor de x: 2
Informe um número: 6
Informe o valor de x: 1
Informe um número: 98
Informe o valor de x: 5
Informe um número: 7
Informe o valor de x: 3
lista B [8.0, 6.0, 98.0, 7.0]
"""