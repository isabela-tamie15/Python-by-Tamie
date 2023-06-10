"""
3) Elaborar um programa que leia uma lista com 4 números reais, em seguida o programa deve
exibir as notas e a média.
"""
lista=[]
for r in range(1,5):
    nota=float(input("Digite a nota: "))
    lista.append(nota)
media = sum(lista)/len(lista)
print(f"As notas são {lista} e a média é {media:.2f}")

# RESULTADO
"""
Digite a nota: 5.5
Digite a nota: 6.8
Digite a nota: 7.3
Digite a nota: 9.2
As notas são [5.5, 6.8, 7.3, 9.2] e a média é 7.20
"""