#!/usr/bin/env python3

# fix error in: print('Anthony J. D'Angelo said, "Develop a passion for learning. If you do, you will never cease to grow."')
print('Anthony J. D\'Angelo said, "Develop a passion for learning. If you do, you will never cease to grow."')

# Make the following sentence appear completely uppercase: The door swung open to reveal pink giraffes and red elephants.
original_str = "The door swung open to reveal pink giraffes and red elephants."
upper_str = original_str.upper()
print(upper_str)

# Determine the index of the "a" in "departure."
string_to_index = "departure"
index_a = string_to_index.find("a")
print(index_a)

#Determine the length of the sentence: The tattered work gloves speak of the many hours of hard labor he endured throughout his life
str3 = "The tattered work gloves speak of the many hours of hard labor he endured throughout his life"
length_str3 = len(str3)
print(length_str3)

#Given a variable breed = "Great Dane", use string formatting (e.g. f-string) to print the following sentence: The Great Dane looked more like a horse than a dog.
breed = "Great Dane"
print(f'The {breed} looked more like a horse than a dog.')

#Assign breed to "Mastiff" and reprint the statement.
breed = "Mastiff"
print(f'The {breed} looked more like a horse than a dog.')
