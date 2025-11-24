user = {'name': 'Israel', 'idade': 26, 'email': 'rael@email.com'}

# O método items() retorna uma lista de tuplas contendo elementos do dicionário.
for chave, valor in user.items():
    print(f'chave: {chave}; valor: {valor};')