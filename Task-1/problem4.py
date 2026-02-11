# Num1: 10 || Num2: 5 || Operator: "/"
# (+, -, *, /)
num1 = int(input("Num1: "))
num2 = int(input("Num2: "))
Operator = input("Choose an operator (+, -, *, /) : ")
if Operator == '+':
    print(num1 + num2)

elif Operator == '-':
    choice = int(input(f"Enter \" 1 \" for ({num1} - {num2}), \" 2 \" for ({num2} - {num1}) : "))
    if choice == 1:
        print(num1 - num2)
    if  choice == 2:
        print(num2 - num1)

elif Operator == '*':
    print(num1 * num2)

elif Operator == '/':
    choice = int(input(f"Enter \" 1 \" for ({num1} / {num2}), \" 2 \" for ({num2} / {num1}) : "))
    if choice == 1:
        if num2 == 0:
            print("Math Error!")
        else:
            print(num1 / num2)
    if  choice == 2:
        if num1 == 0:
            print("Math Error!")
        else:
            print(num2 / num1)