'''galera=[['Rafael',35],['Fernanda',33],['Alicia',5],['Kita',27]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos!')'''
galera=list()
dado=list()
totmai=totmen=0
for c in range(0,3):
    dado.append(str(input('Nome:')))
    dado.append(int(input('Idade:')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1]>18:
        print(f'{p[0]} é maior de idade!')
        totmai+=1
    elif p[1]<18:
        print(f'{p[0]} é menor de idade!')
        totmen+=1
print(f'Tivemos na lista {totmai} pessoa(s) maior de idade e {totmen} pessoa(s) menor de idade!')






