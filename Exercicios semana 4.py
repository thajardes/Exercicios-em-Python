#Exercicio 3.1
""""
f = eval(input('Digite a temperatura em graus Fahrenheit:'))
c = 5/9 * (f - 32)

print('A temperatura em graus Celsius é ' + str(c))
"""
#Exercicio 3.8
""""
def media_dois_numeros(x , y):
    'retorna a média de dois números'
    media = (x + y) / 2
    return media

valor_media = media_dois_numeros(2 , 3.5)
print(valor_media)
"""
#Exercicio 3.9
'''
def perimetro(x):
    calcula_perimetro = 2 * 3.14 * x
    return calcula_perimetro

valor_perimetro = perimetro(1)
print(valor_perimetro)
'''
#Exercicio 3.10
'''
def negativos(lst):
    'retorna somente os números negativos da lista'
    for i in lst:
     if i < 0:
      print(i)

lista_negativos = [4, 0,-1,-3, 6, -9]
print(lista_negativos)
negativos(lista_negativos)
print(negativos)

help(negativos)
'''
#Exercicio 3.13
'''
def muda_lugar(lst):
    'Troca o primeiro e ultimo nome da lista'
    lst[0], lst[-1] = lst[-1], lst[0]
    print(lst)

time = ['Ava','Eleanor', 'Clare', 'Sarah']
muda_lugar(time)
print(muda_lugar)
'''
#Exercicio 3.14
def trocaPU(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    print(lst)

ingredientes = ['farinha', 'acúcar', 'manteiga', 'maçãs']
trocaPU(ingredientes)
print(trocaPU)








