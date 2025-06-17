from datetime import datetime, timedelta, date

def get_upcoming_birthdays(users):
    today = date.today()
    upcoming_birthdays = []
    for user in users:
        try:
            birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
            birthday_this_year = birthday_date.replace(year=today.year)
            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            delta_days = (birthday_this_year - today).days
            if 0 <= delta_days <= 7:
                congratulation_date = birthday_this_year
                if congratulation_date.weekday() >= 5:  # 5 = Saturday, 6 = Sunday
                    congratulation_date += timedelta(days=(7 - congratulation_date.weekday()))
                upcoming_birthdays.append({
                    "name": user["name"],
                    "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
                })
        except ValueError:
            continue  # Пропустити користувача з некоректною датою
    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.06.23"},
    {"name": "Jane Smith", "birthday": "1990.06.27"}
]

upcoming_bdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_bdays)
