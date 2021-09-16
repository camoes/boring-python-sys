print('How many cats do you have')

numCats = input()
try:
    if int(numCats) >= 4:
        print ('that is a lot of cats')
    else:
        print('meh')
except ValueError:
    print ('You did not enter a number')
    