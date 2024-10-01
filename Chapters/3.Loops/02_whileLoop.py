#While Loop
i = 1
while(i<=10):
    print(i)
    i+=1


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
        continue
    print(i)