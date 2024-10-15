#[TextBook] Question 5)  A local biologist needs a program to predict population growth. The inputs would be the initial number of organisms, the rate of growth (a real number greater than 0), the number of hours it takes to achieve this rate, and a number of hours during which the population grows. For example, one might start with a population of 500 organisms, a growth rate of 2, and a growth period to achieve this rate of 6 hours. Assuming that none of the organisms die, this would imply that this population would double in size every 6 hours. Thus, after allowing 6 hours for growth, we would have 1000 organisms, and after 12 hours, we would have 2000 organisms. Write a program that takes these inputs and displays a pre- diction of the total population.


initialPopulation = int(input("Enter the initial number of organisms: "))
growthRate = float(input("Enter the rate of growth: "))
growthPeriod = int(input("Enter the number of hours to achieve this growth rate: "))
totalHours = int(input("Enter the total number of hours for population growth: "))

numberOfGrowthPeriod = totalHours // growthPeriod

finalPopulation = initialPopulation * (growthRate ** numberOfGrowthPeriod)

print(f"The total population after {totalHours} hours is {finalPopulation}.")