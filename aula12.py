nome=str(input('Qual é o seu nome?')).upper().strip()
if nome=='RAFAEL':
    print('Que nome bonito!')
elif nome=='PAULO'or nome=='ANTONIO'or nome=='JOÃO':
    print('Seu nome é bem popular no Brasil!')
elif nome in'ANA FERNANDA ALICIA JULIANA':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal.')
print('Tenha uma bom dia, {}!'.format(nome))






