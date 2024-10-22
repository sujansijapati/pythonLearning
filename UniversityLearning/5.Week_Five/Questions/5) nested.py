#>>>> Question 5) Write a program using nested loops to print the pattern below. The number of lines is input from the user.
# 1

# 2 3

# 4 5 6

# 7 8 9 10

# 11 12 13 14 15


    
lines = int(input("Enter the number of lines: "))
curr = 1
for i in range(1, lines + 1):

    for j in range(i):
        print(curr, end=" ")
        curr += 1
        
    print()
