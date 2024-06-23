weight = input('weight:  ')
print(weight)
option = input('l(bs) or k(g)  ')
print(option)
try:
    if option == 'l' :
        calculation = int(weight) * 0.45
        unit = 'kilograms'
    elif option == 'k' :
        calculation = int(weight)/0.45
        unit = 'pounds'
    print(f'you are {calculation} {unit}')
except ValueError:
    print("value can't be a letter(s)")
for name in ['bola','sola','tola']:
    print(name)
numbers = [5,2,5,2,2]
for number in numbers:
    print('*' * number)