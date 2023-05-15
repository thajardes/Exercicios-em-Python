#Exercicio 3.5
'''''
listaPalavras = eval(input('Digite a lista de palavras:'))

for palavra in listaPalavras:
    if len(palavra) == 4:
        print(palavra)
'''''
#Exercicio 3.5: Escreva o laço for que exibirá as sequencias de números a seguir, um por linha,
# no shell interativo do Python.

#a) Inteiros de 0 a 9
'''''
for i in range(10):
    print(i)
'''''

#b)Inteiros de 0 a 1
'''''
for i in range(2):
    print(i)
'''''
#3.7 Escreva um laço for que exiba a seguinte sequência de números, um por linha

#a) Inteiros de 3 até 12, inclusive este.
'''''
for i in range(3, 13):
    print(i)
'''''

#b) Inteiros de 0 até (mão não incluindo)9, com um passo de 2 em vez de do padrão 1.
'''''
for i in range(0, 9, 2):
    print(i)
'''''

#c) Inteiros de 0 até (as não incluindo)24, com um passo de 3.
'''''
for i in range(0,24,3):
    print(i)
'''''

#d) Inteiros de 3 até (mas não incluindo) 12, com um passo de 5.
'''''
for i in range(3,12,5):
    print(i)
'''''

'''''
numero = 1
while numero <= 5:
    if (numero == 3):
        numero += 1
        continue
    print(numero)
    numero+= 1
print("Fim")   
'''''
'''''
frase = 'algoritmos'

for c in frase:
    if c not in 'aeiou':
        print('Consoante: ', c)
'''


