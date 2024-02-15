def both(number1, number2):
    if (number1 <= 0 and number2 <= 0) or (number1 >= 0 and number2 >=0):
        print(True)
    else:
        print(False)
    return


number1 = int(input("Enter number1: "))
number2 = int(input("Enter number2: "))
print(both(number1, number2))

