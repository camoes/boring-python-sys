import random
print ('Hello, what is your namae')
name = input()
secretNumber = random.randint(1, 20)
print ('well ' + name + ' I am thinking of a number between 1 and  20, can you guess it ?')

for guessesTaken in range (1, 10):
    print ('Take a guess')
    guess = int(input())
    if guess < secretNumber:
            print ('Your guess is to low')
    elif guess > secretNumber:
            print ('Your guess is to high')
    else:
        break

if guess == secretNumber:
    print ('Nice' + name + 'You guessed my number in '+ guessesTaken)
else:
    print ('Nope, the number I was thinking was ' + secretNumber)

