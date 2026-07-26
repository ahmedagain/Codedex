import random

rock = 1
paper = 2
scissors = 3
lizard = 4
spock = 5

print("===================")
print("Rock Paper Scissors")
print("===================")

print("1) ✊")
print("2) ✋")
print("3) ✌️")
print("4) 🦎")
print("5) 🖖")

player = int(input("Pick a number: "))
cpu = random.randint(1, 5)

if player == cpu:
    print("It's a tie!")
elif (player == scissors and cpu == paper) or (player == paper and cpu == rock) or (player == rock and cpu == lizard) or (player == lizard and cpu == spock) or (player == spock and cpu == scissors) or (player == scissors and cpu == lizard) or (player == lizard and cpu == paper) or (player == paper and cpu == spock) or (player == spock and cpu == rock) or (player == rock and cpu == scissors):
    print("You win!")
else:
    print("You lose!")

