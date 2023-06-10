"""
1) Elaborar um programa que lê dois valores. Ele deve apresentar a soma desses valores 
e indicar qual é o maior valor entre eles. Esse programa deve-se repetir 5 vezes.
"""
for n in range(1,3):
    n1 = int (input("Digite um valor: "))
    n2 = int (input("Digite um valor: "))
    soma= n1+n2
    print(f"A soma dos valores é {soma}")
    if n1>n2:
        print(f"O número maior é {n1}") 
    else:
        print(f"O número maior é {n2}")

# RESULTADO
"""
Digite um valor: 5
Digite um valor: 5
A soma dos valores é 10
O número maior é 5
Digite um valor: 1
Digite um valor: 9
A soma dos valores é 10
O número maior é 9 
"""