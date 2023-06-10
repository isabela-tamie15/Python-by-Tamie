"""
1) Desenvolva um algoritmo que escreve em disco um arquivo com números ordenados 
crescentemente de 1 a 100. Cada número deve ser separado por “;”. O arquivo deve 
se chamar “crescente.txt”.
"""
arquivo = open("crescente.txt","w")
lista = []
for n in range(1,101):
    lista.append(str(n)+";")
arquivo.writelines(lista)
arquivo.close()

# RESULTADO
# Não saiu nada no terminal, mas o arquivo foi aberto como resposta ao comando.
# Abri um arquivo com o nome crescente.txt, e nele escrevi a linha abaixo:
"""
1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;29;30;31;32;33;34;35;36;37;38;39;40;41;42;43;44;45;46;47;48;49;50;51;52;53;54;55;56;57;58;59;60;61;62;63;64;65;66;67;68;69;70;71;72;73;74;75;76;77;78;79;80;81;82;83;84;85;86;87;88;89;90;91;92;93;94;95;96;97;98;99;100; 
"""