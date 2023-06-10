"""
6) Elaborar um programa que o usuário tenha que digitar 10 números inteiros. No final, 
o programa deve exibir quantos números são múltiplos de 3, quantos números são menores 
que 45 e maiores que 55, qual é o menor número entre eles e qual a média.
"""
x=0
y=0
lista=[]
for n in range(1,3):
    num=int(input("Digite um número: "))
    lista.append(num)
    if num%3 == 0:
        x=x+1
    if num <45 or num >55:
        y= y+1
menor=min(lista)
media= sum(lista)/len(lista)
print(f"A quantidade de números múltiplos de 3 é: {x}")
print(f"A quantidade de números menor que 45 ou maior 55 é: {y}")
print(f"A média dos números é: {media}")

# RESULTADO5
"""
Digite um número: 60
Digite um número: 40
A quantidade de números múltiplos de 3 é: 1
A quantidade de números menor que 45 ou maior 55 é: 2
A média dos números é: 50.0
"""