def saudacao(pessoa, idade = 26, altura = 1.74):
    return f'Nome: {pessoa}\nIdade: {idade}\nAlturaa: {altura}'

'''
Podemos declarar valores no próprio parâmetro, mas ao declarar um, todos os que 
vem depois devem ser declarados também.

Os valores declarados nos parâmetros serão substituídos pelos valores declarados
nos argumentos.
'''

retorno = saudacao('Rael')

print(retorno)