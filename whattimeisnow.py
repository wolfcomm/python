name = input('Как вас зовут? \n')
print('Привет, ', name, '!', sep='')
time = int(input('Который сейчас час, ' + name + '?\n'))
print('Понятно, а я думал, что ', time + 1, end='')
time = a + 1
if time < 0 or time >= 25:
    print(' часов не бывает', name, '!', sep='')
elif time >= 22:
    print(' часа!')
elif time % 10 == 1:
    print(' час!')
else:
    print(' часов!')
