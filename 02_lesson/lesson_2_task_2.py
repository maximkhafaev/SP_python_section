def is_year_leap(year):
    if year % 4 == 0:
        return True
    else: return False
    
yr = int(input('Введите год: '))
is_leap = is_year_leap(yr)
print(f'Год {yr}: {is_leap}')