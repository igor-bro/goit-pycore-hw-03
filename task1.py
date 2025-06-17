from datetime import datetime, date

def get_days_from_today(date_str):
    try:
        target_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        today = date.today() 
        delta = today - target_date
        return delta.days 
    except ValueError:
        return "Невірний формат дати, використовуйте РРРР-ММ-ДД"
    
print("Пошук різниці в днях між сьогоднішньою та датою пошуку")    
date_str = input(str("Введіть дату пошуку >>> ")) 
result = get_days_from_today(date_str)
print("Результат:", result)