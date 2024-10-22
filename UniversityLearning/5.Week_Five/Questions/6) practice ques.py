# #(Challenging- Optional) >>>> Question 6) population total
# Consider the following statement, which creates a list of populations of countries in eastern Asia (China, DPR Korea, Hong Kong, Mongolia, Republic of Korea, and Taiwan) in millions: country_populations = [1295, 23, 7, 3, 47, 21]. Write a program that adds up all the population values and stores them in variable total. The program then prints the total population of these six countries. Develop the solution using: (a) for loop, (b) while loop.

# A sample execution is shown below:

# (Using for loop) The total population of these countries is 1396 million.

# (Using while loop) The total population of these countries is 1396 million.





# (Using while loop) The total population of these countries is 1396 million.

country_populations = [1295, 23, 7, 3, 47, 21]
total = 0
i = 0
while i < len(country_populations):
    total += country_populations[i]
    i += 1
print(f"The total population of these countries is {total} million.")


# (Using for loop) The total population of these countries is 1396 million.

total = 0
country_populations = [1295, 23, 7, 3, 47, 21]

for population in country_populations:

    total += population

    print(f"The total population of these countries is {total} million.")