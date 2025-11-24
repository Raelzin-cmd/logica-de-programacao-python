# Removendo uma fruta da lista

frutas = ['maçã', 'manga', 'mamão', 'uva', 'melancia']

print(frutas)

remover = input('Digite o nome da fruta que deseja remover: ')

existe_fruta = frutas.count(remover)

if existe_fruta == 0:
    print('Essa fruta não existe!')
else:
    for fruta in frutas:
        if fruta == remover:
            frutas.remove(fruta)
            print(f'{remover.upper()} foi removida!')

print(f'lista atual: {frutas}')