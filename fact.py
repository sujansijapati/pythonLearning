#1. Find the factorial of a number using a `for` loop.

n = int(input("Enter the number: "))
fact = 1
i = 1
if n < 0:
    print("We can't calculate the factorial of negative number!!")
elif n==0:
    print("The factorial of 0 is 1")
else:
    while i <= n:
        fact = fact * i
        i = i + 1
    print(f"The Factorial of {n} is {fact}")