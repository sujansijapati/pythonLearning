#3. Find the sum of numbers from 1 to N using a for loop.

n = int (input ( "Enter the number: "))
sum = 0
i = 1
while(i <= n):
    sum += i
    i= i+1 
    print(sum)