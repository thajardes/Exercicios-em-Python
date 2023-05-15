#Exercicio  3.2
#a)
'''
idade = eval(input('Informe sua idade'))
if idade > 62:
     print('Você pode obter benefícios de pensão')
'''
#b)
'''
def maiores_jogadores ():
    lista_jogadores = ['Musial', 'Aaron', 'Willians', 'Gehrig', 'Ruth']
    jogador = input('Informe o nome do jogador: ')
    if jogador in lista_jogadores:
        print('Um dos 5 maiores jogadores de beisebol de todos os tempos !')

maiores_jogadores()
'''
#c)
'''
golpes = eval(input('Insira o valor do golpe: '))
defesas = eval(input('Insira o valor da defesa:'))
if golpes > 10 and defesas == 0:
    print('Você está morto!')
'''
#d)
'''
norte = True
sul = False
leste = True
oeste = False

direção = input('Informe o ponto cardeal em que você está: ')
if norte or sul or leste or oeste == True:
    print('Você pode escapar')
'''
#Exercicio 3.3
#a)
'''
ano = eval(input('Informe quantos dias tem o ano: '))
if ano % 4 == 0:
    print('Pode ser um ano bissexto.')

else:
    print('Definitivamente não é um ano bissexto')
'''
#b)
'''
bilhete = eval(input('Informe o numero de seu bilhete:'))
loteria = 60
if bilhete == loteria:
    print('Você ganhou!')
else:
    print("Melhor sorte da próxima vez!")
'''
#Exercicio 3.4
'''
def valida_usuario():
    nome = input('Digite seu nome:')
    lista = ['Joe', 'Sue', 'Hani', 'Sophie']
    if nome in lista:
        print('Login:',nome)
        print('Você entrou!')

    else:
        print('Login:',nome)
        print('Usuário desconhecido.')

    print('Fim.')

valida_usuario()
'''
#Exercicio 5.1
'''
def meu_IMC():
    altura = eval(input('Informe sua altura em metros:'))
    peso = eval(input('Informe seu peso em quilos: '))
    imc = peso / altura**2

    if imc < 18.5:
        print('Abaixo do peso.')

    elif 18.5 <= imc < 25:
        print('Normal.')

    elif imc >= 25:
        print('Sobrepeso.')

meu_IMC()
'''














