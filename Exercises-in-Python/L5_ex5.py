"""
5) Elaborar um programa que solicita 15 temperaturas em graus Celsius. Para cada 
temperatura inserida, o programa deve convertê-la em graus Fahrenheit e mostra-la na tela.
"""
for n in range(1,16):
    C=float(input("Digite a temperatura desejada em ºC: "))
    F= (C*9/5)+32
    print(f"A temperatura convertida em Fahrenheit é {F:.2f}")

# RESULTADO
"""
Digite a temperatura desejada em ºC: 25
A temperatura convertida em Fahrenheit é 77.00
Digite a temperatura desejada em ºC: 40
A temperatura convertida em Fahrenheit é 104.00
... (Repete 16x a conversão) 
"""