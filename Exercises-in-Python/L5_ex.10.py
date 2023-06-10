"""
10) Elaborar um programa que contem uma lista com 5 elementos. O usuário deve preencher 
essa lista. Exibir no final os valores inseridos pelo usuário, porém os valores negativos 
(caso existirem) devem ser substituídos por zero (0).
"""
lista=[]
for i in range(0,5):
    lista.append(float(input("Informe um número: ")))
print("Lista original: ", lista)
for n in lista:
    if n<0:
        lista[lista.index(n)]=0
print("Lista trocando números negativos por zero: ", lista)

# RESULTADO
"""
Informe um número: 5
Informe um número: -5
Informe um número: 6
Informe um número: -6
Informe um número: 7
Lista original:  [5.0, -5.0, 6.0, -6.0, 7.0]
Lista trocando números negativos por zero:  [5.0, 0, 6.0, 0, 7.0]
"""