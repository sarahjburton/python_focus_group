#!/usr/bin/env python3

# Indexing strings
string_to_index = "Index Arrays"

first_A = string_to_index[6]
print(first_A)

first_word = string_to_index[0:5]
print(first_word)

last_word = string_to_index[6:12]
print(last_word)

last_index = string_to_index[-1]
print(last_index)

# Strides
every_2nd_value = string_to_index[::2]
print(every_2nd_value)

complicated_stride = string_to_index[0:5:2]
print(complicated_stride)

# Length function
string_to_index = "Index Arrays"
print(len(string_to_index))
# gives twelve, not eleven, because includes zero

# Find function
start_index_Arrays = string_to_index.find("Arrays")
print(start_index_Arrays)
#output is six

not_found = string_to_index.find("I'm not here")
print(not_found)
#output is -1 because not found

# Replicating strings
my_bird = "Bird"
total_birds = my_bird * 3
print(total_birds)

# Concatenating strings
first_name = "Viki"
last_name = "Haghani"
full_name = first_name + last_name
print(full_name)

# String formatting
first_name = "Viki"
last_name = "Haghani"
print(first_name, last_name)

# String Formatting methods
txt = "Nucleus"
num = 3/11

# Method 1: printf()
print('%s %.3f' % (txt, num))
print('%s %.3f %d %e' % (txt, num, 2.1, .1))

# Method 2: str.format()
print('{} {}'.format(txt, num))
print('{} {:.3f}'.format(txt, num))

# Method 3: f-strings
first_name = "Viki"
last_name = "Haghani"

my_first_f_string = f'My first name is {first_name} and my last name is {last_name}. That makes my full name {first_name + " " + last_name}'
print(my_first_f_string)

my_first_f_string1 = f'My first name is {first_name} and my last name is {last_name}. That makes my full name {first_name} {last_name}'
print(my_first_f_string1)


# number example
num = 3/11
decimal_manip = f'The value of 3/11 is {num}. If we round to three decimal places, that makes 3/11 = {num:.3f}'
print(decimal_manip)

# more practice
pet = "Stella"
print(f'My pet\'s name is {pet}')


'''
#general format
my_variable = "variable"
f"Some string with my {my_variable}"
f'Some string with my {my_variable}'

#useful to visualize and annotate your code effectively
print(f'My data frame looks like: {data frame}')
'''
