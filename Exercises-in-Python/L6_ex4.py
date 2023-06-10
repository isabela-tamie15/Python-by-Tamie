"""
4) Elaborar um programa que solicite ao usuário vários valores inteiros.
Quando o usuário digitar o número 100 o programa deve terminar, mostrando quantos valores 
foram acima de 80, quantos foram abaixo de 10 e mostrar a média de todos os valores 
digitados pelo usuário.
"""
num = int(input("Digite um número inteiro: "))
lnum = []
l80 = []
l10 = []
while (num != 100):
    lnum.append(num)
    if (num > 80):
        l80.append(num)
    if (num < 10):
        l10.append(num)
    num = int(input("Digite um número inteiro: "))
maior80 = len(l80)
menor10 = len(l10)
media = sum(lnum)/len(lnum)
print(f"{maior80} elementos tem valor maior que 80, {menor10} elementos tem valor menor que 10, e a média dos valores digitados é  {media}")

# RESULTADO
"""
Digite um número inteiro: 2
Digite um número inteiro: 6
Digite um número inteiro: 82
Digite um número inteiro: 99
Digite um número inteiro: 101
Digite um número inteiro: 100
3 elementos tem valor maior que 80, 2 elementos tem valor menor que 10, e a média dos valores digitados é  58.
"""