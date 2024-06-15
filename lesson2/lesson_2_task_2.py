def is_year_leap(year):
    if year % 4 == 0:
        return True
    if year % 100 == 0:
        return False
    else:
        return False


year_to_check = int(input("Введите год: "))
print(f'Год {year_to_check}: {is_year_leap(year_to_check)}')
