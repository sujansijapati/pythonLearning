#[textbook][1] The tax calculator program of the case study above outputs a floating-point number that might show more than two digits of precision. Use the round function to modify the program to display at most two digits of precision in the output number. 
'''Hint: You can call the round function and use it as shown below 
round(incomeTax, 2)'''

GI = float(input("Enter the Gross Income: "))  #Gross Income
TR = float(input("Enter the Tax Rate: ")) #Tax Rate
IT = GI * TR    #Income Tax
print(f"The Income Tax is {round(IT, 2)}")