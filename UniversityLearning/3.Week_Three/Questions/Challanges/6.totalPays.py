#textbook][10] An employee’s total weekly pay equals the hourly wage multiplied by the total number of regular hours plus any overtime pay. Overtime pay equals the total overtime hours multiplied by 1.5 times the hourly wage. Write a program that takes as inputs the hourly wage, total regular hours, and total overtime hours and displays an employee’s total weekly pay. 


HW = float(input("Enter hourly wage: "))   # Hourly Wages
RH = float(input("Enter total regular hours: ")) # Regular Hour
OTR = float(input("Enter total overtime hours: ")) # OverTime Hour

OR = 1.5 * HW

TWP = (RH * HW) + (OTR * OR) # Total Weekly Pays

print(f"Total weekly pay is: {round(TWP, 2)} pounds")