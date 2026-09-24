import datetime, bday_messages

today = datetime.date.today()
next_birthday = datetime.date(today.year, 9, 12)

time_difference = next_birthday - today

if time_difference.days == 0:
    print(random_message)
else:
    print(f"My next birthday is {time_difference.days} days away!")