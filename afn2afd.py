
nom_arquivos = input("Digite o nome do arquivo de entrada e em seguida o de saida:\n")

qt_espaco = nom_arquivos.count(' ')

if qt_espaco == 0:
    nom_arq1 = nom_arquivos
    list1 = nom_arq1.split('.')
    nom_arq2 = list1[0]+'.afd'
else:
    list2 = nom_arquivos.split(' ')
    nom_arq1 = list2[0]
    nom_arq2 = list2[1]

arq_entrada = open(nom_arq1,'r')
arq1_conteudo = arq_entrada.read()


print(arq1_conteudo) 

input("press")



