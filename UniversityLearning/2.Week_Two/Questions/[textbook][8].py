# [textbook][8] Enter an input statement using the input function at the shell prompt. When the prompt asks you for input, enter a number. Then, attempt to add 1 to that number, observe the results, and explain what happened. 

num = int(input("Enter the number: "))
output = num + 1
print(f"The output after addinng 1 in {num} is {output}")