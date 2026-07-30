# Write code below 💖

menu = [
  "🍔 Cheeseburger", 
  "🍟 Fries", 
  "🥤 Soda", 
  "🍦 Ice Cream", 
  "🍪 Cookie"
  ]

def get_item(x):
  if x == 1:
    return ("🍔 Cheeseburger")
  elif x == 2:
    return ("🍟 Fries")
  elif x == 3:
    return ("🥤 Soda")
  elif x == 4:
    return ("🍦 Ice Cream")
  elif x == 5:
    return ("🍪 Cookie")
  else:
    return ("Not on menu!")

def welcome():
  print("Welcome to the drive thru!")
  print(menu)

welcome()

option = int(input('What would you like to order? '))
print(get_item(option))
