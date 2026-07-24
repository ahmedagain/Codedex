# Write code below 💖

guess = 0
tries = 0

while guess != 6 and tries < 5:
  guess = int(input("Guess the number:  "))
  tries += 1


print("You got it!")

# will still print "You got it!" even if the user didn't guess the number correctly. You can fix this by adding an if statement to check if the user guessed the number correctly or not.