# point = (5, 0)

# match point:
#     case (0, 0):
#         print("Origin")
#     case (x, 0):
#         print(f"Point on X-axis at x={x}")
#     case (0, y):
#         print(f"Point on Y-axis at y={y}")
#     case (x, y):
#         print(f"Point at x={x}, y={y}")

num1= int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case '+':
        result = num1 + num2
        print("The result is "+str(result)+".")

    case '-':
        result = num1 - num2
        print("The result is "+str(result)+".")
    case '*':
        result = num1 * num2
        print("The result is "+str(result)+".")

    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1/num2
            print("The result is "+str(result)+".")
    case _:
        print("Only valid operation")