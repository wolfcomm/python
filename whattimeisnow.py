name = input('Как вас зовут? \n')
print('Привет, ', name, '!', sep='')
time = int(input('Который сейчас час, ' + name + '?\n'))
print('Понятно, а я думал, что ', time + 1, end='')
time = time + 1
if time < 0 or time >= 25:
    print(' часов не бывает', name, '!', sep='')
elif time >= 22 or time == 2 or time == 3 or time == 4: #время в диапазоне 0-24
    print(' часа!')
elif time == 1 or time == 21: #время в диапазоне 0, 1, 5-21
    print(' час!')
else:
    print(' часов!')
