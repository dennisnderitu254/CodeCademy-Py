"""
from random import randrange

random_number = randrange(1, 10)

count = 0
# Start your game!
guess = int(raw_input("Enter a guess:"))
while guess != random_number:
    count += 1
    if count == 3:
        print "OMG! You lose! the answer is", str(random_number) + ", BB!"
        break
    guess = int(raw_input("Guess wrong, %s chance(s) left, enter a guess:" % (3 - count)))
else:
    print "OMG! You win! GB!"


"""

from random import randint

guesses_left = 3
random_number = randint(1,10)

while guesses_left > 0:
    guess = int(raw_input("Your guess:"))
    print random_number
    if guess == random_number:
        print 'You win!'
        break
    guesses_left -= 1
    
else:
    print 'You Lose'