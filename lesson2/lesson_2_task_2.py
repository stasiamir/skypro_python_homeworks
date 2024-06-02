def is_year_leap(year):
    if year % 4 == 0:
        return True
    if year % 100 == 0:
        return False
    else:
        return False
year = int(input("Введите год: "))
print("Год ", year, is_year_leap(year))