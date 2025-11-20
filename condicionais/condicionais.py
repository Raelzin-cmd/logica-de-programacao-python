idade = 87

if idade < 18:
    print(f'Você tem {idade} anos. Você é menor')
elif idade >= 18 and idade < 30:
    print(f'Você tem {idade} anos. Você é jovem')
elif idade >= 30 and idade < 60:
    print(f'Você tem {idade} anos. Você é adulto')
else:
    print(f'Você tem {idade} anos. Você é idoso')