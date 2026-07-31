import random
guessed=random.randint(1,100)
print('I guess a number between 1 and 100')
if int(guessed/4)<5:
    times=5
else:
    times=int(guessed/4)
i=0
while True:
    if i==times:
        print(f'Game Over.You Guessed {i} times.The number is {guessed}')
        break
    try:
        guess=int(input('Guess it'))
    except ValueError:
        print('Please enter a number')
        continue
    i=i+1
    if guess > guessed:
        print('Your guess is too high')
    elif guess < guessed:
        print('Your guess is too low')
    else:
        print(f'You guessed it in {i} times,the number is {guess}')
        break
