#!/usr/bin/env python3

# Set miscellaneous variables to use in expressions
a = 10
b = 5
c = 3
d = -19
e = 2

#Can assign Python code snippets to variables and print them directly
my_add = a + b
print(my_add)

#Can also do within print function

# Find the sum of a and b (use f-string formatting)
print(f'The sum of {a} and {b} is {a + b}')

# Find the difference between a and b
print(f'The difference between {a} and {b} is {a - b}')

# Find the product of a and b
print(f'The product of {a} and {b} is {a * b}')

# Find the quotient of a and b (a divided by b)
print(f'The quotient of {a} and {b} is {a/b}')

# Find the floored quotient of a and c (drops remainder)
print(f'The floored quotient of {a} and {c} is {a//c}')

# Find the remainder of a divided by c
# This is referred to as the modulo
# Gives the numerator of the fraction of the mixed number
print(f'The remainder of {a} divided by {c} is {a % c}')

# Find negative d
print(f'When we negate {d}, we get {-d}')

# Find the absolute value of d
print(f'The absolute value of {d} is {abs(d)}')

# Raise a to the power of c
print(f'{a} to the power of {c} is {pow(a,c)}')

# Try another way to raise a to the power of c
print(f'{a} to the power of {c} is {a ** c}')


#Follows PEMDAS

exp1 = a * e + d
print(exp1)

exp2 = a * (e + d)
print(exp2)

exp3 = a ** e + d - b * c
print(exp3)

# Math example
total_min = 43 + 42 + 57
total_hr = total_min/60
print(total_hr)

# Practice simultaneous math and assignment
# Used to count number of things in data frame: if this value is here, add one to this value and overide the previous value
i = 0
i = i + 1 # fully written out
print(i)

i = 0
i += 1 # shorthand notation
print(i)