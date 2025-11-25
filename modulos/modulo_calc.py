# Importando seletivamente
# from calculadora import soma, div


'''
Aqui estamos importando todos as funções do arquivo calculadora
Evitando também de inicializar a função logo abaixo, enxugando o código
'''

# Importando todas as funções de forma desestruturada
from package.calculadora import *

print(soma(3, 5))

print(div(3, 5))

print(mult(3, 5))

print(sub(3, 5))