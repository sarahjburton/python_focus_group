#!/usr/bin/env python3

# Assign numbers as an integer, float, and string
a = 1 #integer
b = 1.5 #float
c = '1' #string

# Demonstrate type incompatibilities
print(a + b) 

# Store float in d
d = 1.9
print(d, type(d))

# Convert float from d to integer and store that in e
e = int(d)
print(e, type(e))

# Functions for type casting

# Turn the string "3" into an integer
my_int = int("3")
print(my_int, type(my_int))

# Turn the number 53 into a string
my_str = str(53)
print(my_str, type(my_str))

# Turn the integer 7 into a float
my_float = float(7)
print(my_float, type(my_float))

#Turn the string "3" into a float
my_float2 = float("3")
print(my_float2, type(my_float2))

x = something
if x % 5 == 0:
	return True
