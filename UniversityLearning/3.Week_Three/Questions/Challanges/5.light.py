#[textbook][8] Light travels at 3 * 10^8 meters per second. A light-year is the distance a light beam travels in one year. Write a program that calculates and displays the value of a light-year. 


speedOfLight = 3 * 10**8 
secondsInYear = 365 * 24 * 60 * 60  

distanceTravelled = speedOfLight * secondsInYear

print(f"The distance light travels in one year is {distanceTravelled} meters.")