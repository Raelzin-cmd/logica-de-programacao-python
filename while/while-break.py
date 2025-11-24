# Cadastro de pessoas 

pessoas = []

while True:
    nome = input('Digite o nome da pessoa: ')
    if nome.isnumeric() and int(nome) == 0: #Se o nome for numerico e 0, encerra o loop
        break
    pessoas.append(nome)    # Adiciona o nome na lista
    print(pessoas)
