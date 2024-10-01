#Iterating over range 
i = 0
for i in range(1, 11):
    print(i)


     #iterating over a list
names = ["Sujan", "Alima", "Aashutosh", "Aayushma"]
for name in names:
    print(name)


    #Iterating over string
myName = "SujanSijapati"
for letter in myName:
    print(letter)

    #Break and Continuous statement
'''Break Statement
It is used to exit the loop permanently when a certain condition is met'''
for i in range(1, 10):
    if i==6:
        break
    print(i)


'''Continuous Statement
It is used to skips the current iteration and moves to the next one'''
for i in range(1, 11):
    if i==6:
        continue #It will skip 6 and continue the program
    print(i)