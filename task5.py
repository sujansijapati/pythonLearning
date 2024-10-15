#5. Print the multiplication table of a given number using a `for` loop.

n = int(input("Enter the number for the multiplication table you want: "))
for i in range(1,11):
    print(f"{n} * {i} = {i*n}")