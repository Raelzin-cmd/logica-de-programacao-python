def saudacao(pessoa, idade, altura):
    return f'Nome: {pessoa}\nIdade: {idade}\nAlturaa: {altura}'

# Argumento misto (Nomeado + Posicional)
# O primeiro argumento deve ser posicional, o restante pode ser nomeados
retorno = saudacao('Rael', altura = 1.74, idade = 26)

print(retorno)