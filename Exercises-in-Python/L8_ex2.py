"""
2) Desenvolva um algoritmo que escreve em disco um arquivo com números ordenados 
decrescentemente de 100 a 1. Cada número deve estar em uma linha. O arquivo deve 
se chamar “decrescente.txt”.
"""
arquivo = open("decrescente2.txt","w")
lista = []
for n in range(100,0,-1):
    lista.append(str(n) + ";" + "\n")
arquivo.writelines(lista)
arquivo.close()

# RESULTADO
# Não saiu nada no terminal, mas o arquivo foi aberto como resposta ao comando.
# Abri um arquivo com o nome crescente.txt, e nele escrevi a linha abaixo:
"""
100;
99;
98;
97;
96;
95;
94;
# A lista continuou do 93 ao 8, só cortei para facilitar a visualização do arquivo.
... 
7;
6;
5;
4;
3;
2;
1;
"""
