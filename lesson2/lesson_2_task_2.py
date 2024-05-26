def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False
year = int(input("Введите год: "))
print("Год ", year, is_year_leap(year))