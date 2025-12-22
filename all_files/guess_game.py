# Comp chooses a random number within the range, you guess continuously until you get it right.
# Fun fact, there's a puzzle on this I just can't remember very well, I think
# it goes The minimum number of times you need to get the number right. 
min_value = int(input("Enter the lowest number you want to guess: "))
max_value = int(input("Enter the highest number you want to guess: "))
from random import randint
try:
    while True:
        print("Type nothing to quit")
        number = int(input("Guess: "))
        guess = randint(min_value, max_value)
        print(guess)
        if number > guess:
            print("Too high")
        elif number < guess:
            print("Too low")
        
        else:
            print("Correct")
            break
except ValueError:
    pass
print("You escaped!")
