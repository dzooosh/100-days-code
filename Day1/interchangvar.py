# Interchanging variables

"""
A situation when you want to change the value of two variables 'a' and 'b'
"""

a = 5
b = 100

# interchange both so that a = 100 and b = 5
"""
Method 1
create an extra value 'c'
c = a
a = b
b = c

print (a, b)
"""

# Method 2
a, b = b, a

print(a, b)
