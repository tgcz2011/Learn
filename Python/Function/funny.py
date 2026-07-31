def collatz(number):
    try:
        number = int(number)
    except ValueError:
        print("Please enter a number")
        return ValueError
    print(number)
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = number*3 + 1
        print(number)
    return None