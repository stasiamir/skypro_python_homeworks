def bank(a,time):
    for each_year in range(time):
        a = (a * 1.1)
    return a

print(bank(1000000, 3))
