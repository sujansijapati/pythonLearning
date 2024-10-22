#>>>> Question 1 ) Based on what you have learnt about for loop, convert the while loop in example 1) to a for loop? identify the loop control variable in both loops (while and for) for this example. 

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


for i in range(1,6):
    if i < 6 :
      print (i)
      i = i + 1
    else:
      print("i is no longer less than 6")