#manipulação de strings

#varivel
Nome= "Kauan"
print(Nome)

#contar quantos caracteres tem no texto 
qtdcarac= len(Nome)
print(qtdcarac)

#contar quantas vezes um determinado caractere se repete 
qtdAzinho = Nome.count('a')
qtdAzao = Nome.count("A")

#transformar o texto todo em maiusculo 
nomezao = Nome .upper ()
print(nomezao)

#transformar o texto todo em minusculo 
nomezinho = Nome.lower()
print(nomezinho)

#trocar todas as letras A por U 
nomezaotrocado = nomezao.replace("A", "U")
print(nomezaotrocado)
nomezaotrocado = nomezao.replace("U","A")
print(nomezaotrocado)
nomezinhotrocado= nomezao.replace("n","m")
print(nomezinhotrocado)
nometrocado = Nome.replace("gabriel")
print(nometrocado)

#splint > dividir o texto 
sobremesa = "pudim não é tão bom quanto falam que é" 

#para separar as palavras, a barra de espaço será contada como cacartere 
palavras = sobremesa.split(" ")
print(palavras)
print(palavras[0])
print(palavras[1])
print(palavras[2])
print(palavras[3])
print(palavras[4])
print(palavras[5])
print(palavras[6])
print(palavras[7])
print(palavras[8])

#sera exibido 9 palavras do texto, por que a primeira começa do 0

contpalavras = len(palavras)
print(contpalavras)

#atividade 1 
#contador de vogais 
#contar quantas e espaços tem em uma frase que o usuario vai digitar 

def contvogais():
    frase=input("digite uma frase")
    qtdespaco = frase.count(" ")
    qtda = frase . count("a")+frase.count("A")
    qtde = frase . count("e")+frase.count("E")
    qtdi = frase . count("i")+frase.count("I")
    qtdo = frase . count("o")+frase.count("O")
    qtdu = frase . count("u")+frase.count("U")
    
    print("quantidade de espaço",qtdespaco)
    print("quantidade de A",qtda)
    print("quantidade de e",qtde)
    print("quantidade de i",qtdi)
    print("quantidade de o",qtdo)
    print("quantidade de u",qtdu)
    