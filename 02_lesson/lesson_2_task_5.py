def month_to_season(month):
    if month <= 2 or month == 12:
        return 'зима'
    elif month <= 5:
        return 'весна'
    elif month <= 8:
        return 'лето'
    else: return 'осень'

month = int(input("Введите месяц (1-12): "))
print(f'{month} месяц — это {month_to_season(month)}')