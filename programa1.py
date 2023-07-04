# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
# Operadores comuns fundamentais>> sem novivdades
#// divisão com piso - arredonda pra baixo Ex:
a=22;
b=5;
c=a//b;
print(c) #imprime 4

#para exponenciação, usar **

#para módulo, usar %

#Ordem de precedência >> PEMMDAS >> P-Parenteses, E-Exponenciação, Multiplicação, Módulo e Divisão ( na ordem que aparecer da esq. pra direita), A- Adição e S- Subtração#
#Operadores de comparação >> sem novivdades, mas é importante observar que em Python, diferente é != Ex:
var1=5
var2=6
teste = var1 != var2
print (teste)

#Operadores lógicos >> And, Or e Not - Sem novidades

# Operadores de associação são usados para saber se um conjunto de operadores está presente em um objeto Ex: 

Times_cariocas= "Flamengo","Fluminense", "Vasco", "Botafogo"

verifica="São paulo" in Times_cariocas

print(verifica) #falso

verifica="Vasco" in Times_cariocas

print (verifica) #verdadeiro

#Funções em Python >> usamos def para definir uma função que é um bloco de código que é executado apenas quando é invocado Ex:
# sintaxe: def NomeDaFunção(argumentos):

def escreveBomdia(nome):
   print ("Bom dia,", nome+"!")
   
escreveBomdia("Cláudio")

def soma(num1,num2):
    resultado =num1+num2;
    print ("A soma entre os números", num1,"e", num2, "é", resultado)

soma(8,9)

#Funções lambdas - São pequenas funções anônimas. Ex:>>

potenciacao =lambda x,y: x**y

print(potenciacao(10,2))# retornará 100, pois 10²=100

#Tipos de comentários
''' Comentário '''
""" Comentário""" 
#Usando algumas funções nativas do Python
# capitalize() converte o primeiro caractere em Maiúscula
nome = "cláudio"
print(nome.capitalize())

#find() e index() Retornam a posição da primeira ocorrência de um valor em uma string, caso não exista, find() retornará -1, já index() retornará mensagem de erro. Ex>>
trecho = "Uma vez flamengo, sempre flamengo"
print(trecho.find("Uma")) #retorna 0
print(trecho.find("uma"))#retorna -1

print(trecho.index("Uma")) #retorna 0
"""print(trecho.index("uma")) da erro """ 

#len() Retorna o tamanho da string Ex>>

var="Vasco";
print("A palavra", var, "tem",len(var), "letras");

#split() Divide substrings encontradas a partir de um separador especificado e retorna uma lista. Ex>>
print(trecho)

print (trecho.split(","))

#strip() Remove espaços das extremidades da string

varTeste=" Hermanoteu na terra de Godah  "
print(varTeste)
var_sem_espaco= varTeste.strip()
print(var_sem_espaco)

#declarando duas variáveis simultaneamente ex:

nome, idade="cláudio", 33

print("Olá,",nome.capitalize(),"sua idade é:", idade)

#Python é case sensitive

teste = "Flamento" =="flamento"
print(teste) #resultado é False

_var=5;
print(_var)#Uma variável pode começar com _

teste=bool(0)
print(teste) #Imprime false

time="Flamengo"
jogador="Rogério Ceni"

teste=time[7]==jogador[1]
print(teste)#Imprime True

#Tipos de dados -Tópico muito relevante para concursos e Análise de dados >>
#Listas Coleção de valores ordenados, mutáveis, indexados que pode conter valores duplicados, separados por colchetes
listaFrutas=['maça', 'banana','mamão','laranja','melancia', 'limão', 'abacaxi',"pera"]

#print(listaFrutas[2*2])
print("Lista de frutas:")
for x in listaFrutas:
    print(x)
    
print(listaFrutas)

listaFrutas[1]='manga'# altera um elemento da lista

print(listaFrutas[-1])#mostra o último elemento da lista

print(listaFrutas[1:3])#mostra posição 1 e 2, mas não a 3

#Funções com listas>>

# del - remove um item ou a lista inteira

del listaFrutas[0]#remove o primeiro item da lista > maça

print(listaFrutas) #mostra a lista sem o item recém deletado

#clear() Função utilizada para limpar uma lista. Ex>>

listateste=['1','2','3','4','5','6','7','8','9','0']

print(listateste.clear())

# len() serve para informar quantos itens tem numa lista

print(len(listaFrutas)) # Retorna 07

#Para adicionar itens, temos as funções append() e insert() >>

listaFrutas.append("morango") #adiciona moranto a lista, no final da lista

print(listaFrutas)#mostra a lista atualizada com o 'morango'


listaFrutas.insert(0,"ameixa")#Essa função permite inserir um item em uma posição específica.

print(listaFrutas)

#Para remover itens da lista temos as funções remove() e pop()

#remove() é utilizado para remover a primeira ocorrência de um item na lista

familia= ['Junior', 'Ligia','Maria','Cláudio','Maria']

familia.remove('Maria')#remove o elemento 2 da lista Família

print(familia)#mostra a lista atualizada

#pop() Remove item especificado ou o primeiro da PILHA

familia.pop() #remove Maria

print (familia)

familia.pop(0) # remove Junior- primeiro item da lista

print(familia)# mostra a lista sem "Junior"

#copy() Função utilizada para copiar uma lista qualquer

lista_nova=familia.copy()
print(lista_nova)

#Função count() usada para informar a quantidade de vezes que determinado item aparece numa lista >> ex
Letras= ['a','b','c','d','e','a','a']

print("a letra a aparece", Letras.count('a'), 'vezes')

#reverse() função utilziada para inverter a ordem dos itens da lista

lista1=['um','dois','três']
lista1.reverse()
print (lista1)

#sort() função utilizada para ordenar os elementos da lista

lista=['a', 'd','b','c']

lista.sort(reverse=True)

print(lista)

#extend() Função utilizada para acrescentar uma lista no final da outra
abc=['a','b','c']
d_ef=['d','e','f']

abc.extend(d_ef) #anexa as listas

print(abc)#mostras as listas anexadas

#index() retorna a posição da primeira ocorrência de um det. elemento
print(abc.index('c'))#mostra o número 2

#range() utilizada para criar listas numéricas de forma fácil.

#Tupla - Representada por parênteses.

tupla=('maça','banana',True,'bola')

print(tupla)
# tupla[1]='limão' essa operação não é suportada pela tupla, da erro!

lista_tupla=list(tupla) #tupla convertida em Lista
print(lista_tupla) #Exibe a lista 

#set  - representado entre chaves{} - mutável, não ordenado
#dicionário - É uma coleção de valores desordenador, mutáveis e indexáveis. >> delimitados por chaves {} como o set, porém no dicionário as chaves delimitam um conjunto chave: valor
carro={'marca':'ford','modelo':'escort','ano':1984}

print(carro['marca'])

carro['ano']=1992 #atualiza o ano do escortinho

print(carro)

carro['cor']='prata' # Acrescenta nova chave e valor no dicionário
print(carro)

