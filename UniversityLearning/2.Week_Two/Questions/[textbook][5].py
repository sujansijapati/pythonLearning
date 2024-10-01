# [textbook][5] Modify the program of question 4 (above) to compute the area of a triangle. Issue the appropriate prompts for the triangle’s base and height, and change the names of the variables appropriately. Then, use the formula 1/2 * base * height to compute the area. Test the program from an IDLE window. 

b = int(input("Enter the base: "))
h = int(input("Enter the height: "))
triangle = 0.5*b*h
print(f"The area of rectangle is: {triangle}")