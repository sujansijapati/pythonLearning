
print("""Please Select the options: 
      1. Addition
      2. Subtraction
      3. Multiplication
      4. Division""")

option = input("Enter the option: ")
if option == "1" or option == "2" or option == "3" or option == "4" or option <= "0" or option > "4":
    if option == "1":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        add = num1 + num2
        print(f"The sum of {num1} and {num2} is {add}.")

    elif option == "2":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        sub = num1 - num2
        print(f"The difference between {num1} and {num2} is {sub}.")

    elif option == "3":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        mul = num1 * num2
        print(f"The product of {num1} and {num2} is {mul}.")

    elif option == "4":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        if num2 != 0:
          div = num1/num2
          print(f"The quotient of {num1} and {num2} is {div}.")
        else:
            print("Error! Division by Zero is not allow")

    elif option == "0" or option > "4":
        print("The option is Invalid. Please select the valid operation")