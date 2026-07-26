# Day in the life game

print("Welcome to the Day in the Life Game!")
print("You wake up in the morning and have to make some choices for your day.")

print("What do you want to do?")
print("1) Go to work")
print("2) Stay home and relax")
print("3) Go out with friends")

choice1 = int(input("Enter your choice (1, 2, or 3): "))

if choice1 == 1:
    print("You go to work and have a productive day!")
    print("After work, you can choose to:")
    print("1) Go to the gym")
    print("2) Go home and watch TV")
    
    choice2 = int(input("Enter your choice (1 or 2): "))
    
    if choice2 == 1:
        print("You have a great workout and feel energized!")
    elif choice2 == 2:
        print("You relax at home and enjoy some TV time.")
    else:
        print("Invalid choice. You end up going home and relaxing.")
elif choice1 == 2:
    print("You stay home and relax for the day.")
elif choice1 == 3:
    print("You go out with friends and have a great time!")
else:
    print("Invalid choice. You end up staying home and relaxing.")

