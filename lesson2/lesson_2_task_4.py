def fizz_buzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", "\n")
        elif i % 3 == 0:
            print("Fizz", "\n")
        elif i % 5 == 0:
            print("Buzz", "\n")
        else:
            print(i, "\n")
n = int(input("Введите число: "))
fizz_buzz(int(n))
