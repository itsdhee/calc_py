#attempting to create a calculator

print("Pyhton Calculator Demo")
print("Pick an option, depending on the operation you want to carry out;")
print("1, for addition operations")
print("2, for subtraction operations")
print("3, for multiplication operations")
print("4, for division operations")

try:
    option = int(input("Pick an option: "))
    num1 = float(input("Enter value 1: "))
    num2 = float(input("Enter value 2: "))
    if option == 1:
        sum = num1 + num2
        print(f"{num1} + {num2} = {sum}.")
    elif option == 2:
        sub = num1 - num2
        print(f"{num1} - {num2} = {sub}.")
    elif option == 3:
        multi = num1 * num2
        print(f"{num1} * {num2} = {multi}.")
    elif option == 4:
        if num2 != 0:
            div = num1/num2
            print(f"{num1}/{num2} = {div}.")
        else:
            print("Division by 0 is not allowed.")
    else:
        print("Input valid option.")
except ValueError:
    print("Invalid input.")