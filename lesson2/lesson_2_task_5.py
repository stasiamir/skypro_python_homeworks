def month_to_season(a):
    if a == 1 or a == 2 or a == 12:
        return ("зима")
    elif a == 3 or a == 4 or a == 5:
        return("весна")
    elif a == 6 or a == 7 or a == 8:
        return("лето")
    elif a == 9 or a == 10 or a == 11:
        return("осень")
    else:
        return("укажите правильный номер месяца")
print(month_to_season(int(input('введите номер месяца '))))