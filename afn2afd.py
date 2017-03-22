
nom_arquivos = input("Digite o nome do arquivo de entrada e em seguida o de saida:\n")

 if nom_arquivos.count(' ') == 0:
	nom_arq1 = nom_arquivos
	list1 = nom_arq1.split('.')
	nom_arq2 = list[0]+'.afd'
	print(nom_arq2) 
else:
	list2 = nom_arquivos.split(' ')
    nom_arq1 = list2[0]
    nom_arq2 = list2[1]

print(nom_arq1) 
print(nom_arq2) 

arq_entrada = open(nom_arq1,'r')
arq1_conteudo = arq_entrada.read()

print(arq1_conteudo) 


input("press")



