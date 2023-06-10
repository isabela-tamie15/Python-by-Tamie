"""
1) Dada a lista: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15].

Exibir as seguintes listas, derivadas da lista acima:
"""
lista=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# a) Intervalo de 1 a 9
print(lista[1:10])
# RESULTADO 
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# b) Intervalo de 8 a 13
print(lista[8:14])
# RESULTADO 
# [8, 9, 10, 11, 12, 13]

# c) Números pares
print(lista[2:16:2])
# RESULTADO 
# [2, 4, 6, 8, 10, 12, 14]

# d) Números ímpares
print(lista[1:16:2])
# RESULTADO 
# [1, 3, 5, 7, 9, 11, 13, 15]

# e) Todos os múltiplos de 2, 3 e 4
print(lista[2:16:2])
print(lista[3:16:3])
print(lista[4:16:4])
# RESULTADO 
"""
[2, 4, 6, 8, 10, 12, 14]
[3, 6, 9, 12, 15]
[4, 8, 12]
"""

# f) Lista reversa
lista.reverse()
print(lista)
# Primero reverte a lista, depois dá print.
# RESULTADO 
# [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# g) Soma do intervalo de 10 a 15
lista.reverse()
print(lista)
soma = sum(lista[10:16])
print(soma)
# RESULTADO 
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# 75

# h) Uma lista com um novo elemento
lista.append(50)
print(lista)
# RESULTADO
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 50]

# i) Substituir o elemento com índice 6
lista[6]="cadeira"
print(lista)
# RESULTADO
# [0, 1, 2, 3, 4, 5, 'cadeira', 7, 8, 9, 10, 11, 12, 13, 14, 15, 50]
