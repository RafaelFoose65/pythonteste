num=[2,4,5,7,9,35]
num[4]=3
num.append(6)
num.sort(reverse=True)
num.insert(3,0)
if 8 in num:
    num.remove(8)
else:
    print('O número 8 não consta na lista!')
num.pop(3)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
