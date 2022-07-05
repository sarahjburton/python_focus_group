#!/usr/bin/env python3

# Examples of strings
str1 = "Hello world"
str2 = "Spring is coming!"
str3 = "My dog ate 3 slices of my pizza"
str4 = "I can't believe my dog did that"

#Escape Sequences
# \n starts a new line
#\t inserts a tab
#\\ makes the \ get interpreted as a character, thus inserting a \ into the string (this works for quotations as well)
print("Roses are red,\nViolets are blue")
print("Loading \t Done")
print("Python escape sequences use a backslash: \\")
print('I\'m in such a good mood today!')
#raw string
print(r"//*/*//**")

#Manipulating Strings
'''
upper() turns the string uppercase
title() turns the string title case
lower() turns the string lowercase
replace() replaces part of the string
'''
# String operations
original_str = "Viki is teaching me how to code in Python"

upper_str = original_str.upper()
print(upper_str)

title_str = original_str.title()
print(title_str)

lower_str = original_str.lower()
print(lower_str)

replace_str = original_str.replace("Viki", "The internet")
print(replace_str)

#practice
hello_str = "hello"
print(hello_str)

bye_str = hello_str.replace("hello","bye")
print(bye_str)

upper1_str = hello_str.upper()
print(upper1_str)

# Stripping spaces
spaced_out = " M y N a m e I s V i k i "
right_strip = spaced_out.rstrip()
left_strip = spaced_out.lstrip()
removeallspace_str = spaced_out.replace(" ","")

print(right_strip)
print(left_strip)
print(removeallspace_str)



