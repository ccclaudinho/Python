# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
# Operadores comuns fundamentais>> sem novivdades
#// divisão com piso - arredonda pra baixo Ex:
a=22;
b=5;
c=a//b;
print(c)

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


