"""
7) Elaborar um programa que lê duas notas (P1 e P2). Caso a média seja maior igual a 5 
deve exibir a mensagem “APROVADO”. Caso a média seja menor que 5 e maior igual a 3 
deve exibir a mensagem “EXAME”. Caso contrário, exibir a mensagem “REPROVADO”. 
Caso esteja de exame, o programa deve solicitar a nota de exame e verificar se o aluno 
está aprovado ou não e exibir o resultado na tela. 
Esse programa deve-se repetir para 30 alunos.
"""
for n in range (1,3):
    p1 = float(input("Digite a nota: "))
    p2 = float(input("Digite a nota: "))   
    media = (p1+p2)/2
    if media >= 5:
        print("Aprovado")
    elif media >=3 and media < 5:
        print ("Exame")
    notaEx = float(input("Digite a nota do exame: "))
    media2 = (media + notaEx) /2
    if media2 >=5:
        print("Aprovado")
    else:
        print ("Reprovado")

#RESULTADO
"""
Digite a nota: 4
Digite a nota: 2
Exame
Digite a nota do exame: 10
Aprovado
Digite a nota: 1
Digite a nota: 1
Digite a nota do exame: 2
Reprovado
""" 