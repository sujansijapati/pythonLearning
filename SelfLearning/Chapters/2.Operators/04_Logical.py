"""
1.AND (and) 
   - Returns True if both statements are True.
   - Example: (5 > 3) and (8 > 6) results in True because both conditions are True.

2.OR (or) 
   - Returns True if at least one of the statements is True.
   - Example: (5 > 10) or (8 > 6) results in True because the second condition is True.

3.NOT (not) 
   - Reverses the result: True becomes False, and False becomes True.
   - Example: not (5 > 10) results in True because (5 > 10) is False, and not makes it True.
"""
#Truth table of "and" operator
# Both conditions need to be true
print("True and True is: ",True and True)
print("True and False is: ",True and False)
print("False and True is: ",False and True)
print("False and False is: ",False and False)

#Truth table of "or" operator
# At least one condition needs to be true
print("True or True is: ",True or True)
print("True or False is: ",True or False)
print("False or True is: ",False or True)
print("False or False is: ",False or False)

#Truth table of "NOT" operator
# Reverse the result of the condition
print("True not True is: ", not(True))


a = 10
b = 5
c = 15
# AND operator
result_and = (a > b) and (c > a)
print("(a > b) and (c > a):", result_and)

# OR operator
result_or = (a < b) or (c > b)
print("(a < b) or (c > b):", result_or) 

# NOT operator
result_not = not (a < b)
print("not (a < b):", result_not)