"""
1. Addition (+)  
   - Adds two values.
   - Example: 5 + 3 results in 8.

2. Subtraction (-)  
   - Subtracts the second value from the first.
   - Example: 10 - 4 results in 6.

3. Multiplication (*)  
   - Multiplies two values.
   - Example: 6 * 7 results in 42.

4. Division (/)  
   - Divides the first value by the second and gives the result as a float.
   - Example: 8 / 2 results in 4.0.

5. Floor Division (//)  
   - Divides the first value by the second and gives the result as an integer (rounded down).
   - Example: 9 // 2 results in 4.

6. Modulus (%) 
   - Returns the remainder after division.
   - Example: 10 % 3 results in 1.

7.Exponentiation (**)  
   - Raises the first value to the power of the second.
   - Example: 2 ** 3 results in 8."""

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
add = num1 + num2
print(f"The sum of {num1} and {num2} is {add}.")