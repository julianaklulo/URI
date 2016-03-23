n = int(input())

numbers = []

for i in range(0, n):
    numbers.append(int(input()))

for i in range(0, n):
    if numbers[i] > 0:
        if (numbers[i] % 2 == 0):
            print("EVEN POSITIVE")
        else:
            print("ODD POSITIVE")
    elif (numbers[i] < 0):
        if (numbers[i] % 2 == 0):
            print("EVEN NEGATIVE")
        else:
            print("ODD NEGATIVE")
    elif (numbers[i] == 0):
        print("NULL")
