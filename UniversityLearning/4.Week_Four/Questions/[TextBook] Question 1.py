#[TextBook] Question 1) Write a program that accepts the lengths of three sides of a triangle as inputs. The program output should indicate whether or not the triangle is an equilateral triangle. 

sideOne = int(input("Enter the side: "))
sideTwo = float(input("Enter the side: "))
sideThree = float(input("Enter the side: "))

if sideOne == sideTwo and sideOne == sideThree:
    print("It is an equilateral Triangle")
else:
     print("It is not an equilateral Triangle",sideOne)