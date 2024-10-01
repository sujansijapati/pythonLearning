# [textbook][6] Write and test a program that computes the area of a circle. This program should request a number representing a radius as input from the user. It should use the formula 3.14 * radius ** 2 to compute the area and then output this result suitably labeled. 

radius = int(input("Enter the radius: "))
area = 3.14*radius**2
print(f"The area of circle is: {area}")