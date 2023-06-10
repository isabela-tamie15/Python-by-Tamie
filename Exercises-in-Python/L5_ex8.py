"""
8) Elaborar um programa que contem uma lista com 6 elementos. O usuário deve preencher 
essa lista. Após o usuário inserir todos os valores o programa deve exibir cada valor 
com sua posição na lista. 
"""
lista=[]
for n in range(1,7):
    numero=int(input("Digite o número: "))
    lista.append(numero)
print(lista)
for x in lista:
    print("O índice {} é igual ao número {}".format(lista.index(x),x))

# RESULTADO
"""
Digite o número: 78
Digite o número: 54
Digite o número: 32
Digite o número: 14
Digite o número: 93
Digite o número: 100
[78, 54, 32, 14, 93, 100]
O índice 0 é igual ao número 78
O índice 1 é igual ao número 54
O índice 2 é igual ao número 32
O índice 3 é igual ao número 14
O índice 4 é igual ao número 93
O índice 5 é igual ao número 100
"""