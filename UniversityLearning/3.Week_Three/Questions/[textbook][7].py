#[textbook][7] Write a program that calculates and prints the number of minutes in a year. 

totalDaysInAYear = 365
hoursInADay = 24
minInAHour = 60
SecondInAHour = 60

totalMinInAYear = hoursInADay * minInAHour * SecondInAHour

totalSecondInAYear = totalDaysInAYear * hoursInADay * minInAHour * SecondInAHour

print(f"The total Minutes in a Year is {totalMinInAYear}")
print(f"The total second in a Year is {totalSecondInAYear}")