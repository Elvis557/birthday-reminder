import datetime

def birthday_reminder(birthdays):
    today = datetime.date.today()

    for name, birthdate in birthdays.items():
        if today.month == birthdate.month and today.day == birthdate.day:
            print(f"Reminder: It's {name}'s birthday today!")

birthdays = {
    "Alice": datetime.date(1990, 1, 15),
    "Bob": datetime.date(1985, 2, 25),
    "Charlie": datetime.date(2000, 1, 15),
}

birthday_reminder(birthdays)
