rawdata = input('Enter a number:')
try:
        a = int(rawdata)
except:
        a = -1

if a > 0:
        print('Your number is')
        print(a)
else:
        print('Not a number')
