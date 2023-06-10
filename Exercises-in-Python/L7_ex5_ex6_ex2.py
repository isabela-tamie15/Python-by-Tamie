"""
6) Elaborar uma função (com retorno) que ao receber um número deve converte em Kelvin e 
exibe o resultado na tela. A fórmula de conversão é: K=C+273,15.
"""
# Questão 06 
def ex06_conversaoK(C):
    K=int(C)+273.15
    return print("A temperatura convertida de Celsius para Kelvin é:",K,"K.") 

teste = input("Digite aqui a temperatura em ºC: ")
print(ex06_conversaoK(teste))

# RESULTADO
# Digite aqui a temperatura em ºC: 35
# A temperatura convertida de Celsius para Kelvin é: 308.15 K.
"""
5) Elaborar uma função (sem retorno) que ao receber um número deve converte em Fahrenheit 
e exibe o resultado na tela. A fórmula de conversão é: F = (9*C+160) / 5.
"""
# Questão 05
def ex05_conversaoF(C):
    F = (9*int(C)+160) / 5
    print("A temperatura convertida de Celsius para Fahrenheit é:",F,"°F.")

teste = input("Digite aqui a temperatura em ºC: ")
print(ex05_conversaoF(teste))

# RESULTADO
# Digite aqui a temperatura em ºC: 20
# A temperatura convertida de Celsius para Fahrenheit é: 68.0 °F.
"""
2) Elaborar uma função (com retorno) que verifica se um número é positivo ou negativo. 
Sendo que o valor de retorno será 1 se positivo, -1 se negativo e 0 se for igual a 0.
"""
# Questão 02
def ex02_positivoNegativo(valor1):
    
    if float(valor1) < 0:
        return -1
    elif float(valor1) == 0:
        return 0
    elif float(valor1) > 0:
        return 1

teste = input("Digite um número: ")
print(ex02_positivoNegativo(teste))    

# RESULTADO
# Digite um número: -4
# -1