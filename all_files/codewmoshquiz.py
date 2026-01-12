
# =========================================================================================================
# QR code generator!
# import qrcode
# link = input("Link of the place you want your qrcode to point to: ")
# qr = qrcode.QRCode()
# qr.add_data(link)
# qr.make(fit=True)
# img = qr.make_image(fill_color="black", back_color='blue')
# img.save('outputqr.png')
# print('Saved!')



# =========================================================================================================

# rock paper scissors game!
import random
def rockpaperscissors():
	computer, person = 0, 0
	r, p, s = "🪨", "📃", "✂️"
	while computer + person < 5:
		c_choice = random.choice([r, p, s])
		while True: # Checks if it's r, p or s, then assigns them to the emoji.
			choice = input("r/p/s: ").lower()
			if choice == 'r':
				choice = r
				break
			elif choice == 'p':
				choice = p
				break
			elif choice == 's':
				choice = s
				break
			else:
				continue
		
		# Checks who the winner is and adds one to their score.
		print(f'You chose {choice}, computer chose {c_choice}')
		winning_rules = {r: s, p: r, s: p} 

		if choice == c_choice:
			print('Draw')
		elif winning_rules[choice] == c_choice: # If whatever "choice" beats is computer's choice then the person wins.
			person += 1
			print('You win this round!')
		else:
			computer += 1
			print('Computer wins this round!')
		
		# check is the user wants to play again.
		try:
			decide = input("Press 'n' to stop, any key continue: ")
			if decide == 'n':
				break
			else:
				continue
		except:
			continue
	
	print("Game Over!")
	print(f'You won {person} times, computer won {computer} times!')
	if person > computer:
		print("Congrats! You win!")
	elif person == computer:
		print("Draw!")
	else:
		print('Computer wins!')
# =========================================================================================================

# Write a function to recursively reverse a nested list.
# reverse_nested([1, [2, [3, 4], 5]])  # Output: [ [5, [4, 3], 2], 1 ]
def reverse_nested(lst):
    if isinstance(lst, list):
        return [reverse_nested(item) for item in reversed(lst)]
    else:
        return lst

# =========================================================================================================

# Write a function that returns True if a string is a palindrome, ignoring:
# - case
# - spaces
# - punctuation !"#$%&'()*+,-./:;<=>?@[\\]^_{|}~.
# is_palindrome("A man, a plan, a canal: Panama")  # True
# is_palindrome("No lemon, no melon")              # True

# =========================================================================================================

# Number guessing game!
import random
def guess():
	lst = []
	while True:
		try:
			a = int(input("Minimum number you want: "))
			b = int(input("Maximum number you want: "))
		except ValueError:
			print("Not an integer!")
			continue
		randnum = random.randint(a, b)
		counter = 0
		while counter < 10:
			guess = int(input("Guess: "))
			if guess > randnum:
				counter += 1
				print("Too high!")
				continue
			if guess < randnum:
				counter += 1
				print("Too low!")
				continue
			if guess == randnum:
				lst.append(counter)
				print(f"You are correct! You guessed the number in {counter} attempts!")
				break
		if counter > 9:
			print(f"You have failed 10 times, the answer was {randnum}!")
		while True:
			try_again = input("Would you like to try again(Y/N) ").lower()
			if try_again == "y":
				break
			if try_again == "n":
				print(f"Minimum tries to get it right was {min(lst, default=0)}")
				return
			else:
				continue

# =========================================================================================================
