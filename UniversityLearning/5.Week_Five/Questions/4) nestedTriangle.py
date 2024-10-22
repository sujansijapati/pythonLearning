#>>>> Question 4 ) print inverted triangle of stars
# Write a program using nested loops to print the pattern below. The number of lines is input from the user.

# *****

# ****

# ***

# **

# *

lines = int(input("Enter the number of lines: "))
curr = 5
for i in range(lines, 0, -1):

    for j in range(i):
        print("*", end=" ")
        
    print("*")