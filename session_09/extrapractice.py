#!/usr/bin/env python3

#Make a dictionary called my_dict where the keys are confusion, recording, organization, complaints, soup and the values are True, No, 57, [1, 2, 3], alphabet, respectively.
dict2 = {'confusion':True, 'recording':'No', 'organization':57, 'complaints':[1,2,3], 'soup':'alphabet'}

#Print the key corresponding the recording.
print(dict2['recording'])

#Add the key and value set catastrophe and False, respectively.
dict2["catastrophe"] = False
print(dict2['catastrophe'])

#Delete the recording entry and its corresponding value.
del(dict2['recording'])
print(dict2)

#Check if "soup" is in the dictionary.
check1 = "soup" in dict2
print(check1)

#Print all the keys in the dictionary.
print(dict2.keys())

#Print all the values in the dictionary.
print(dict2.values())

#Make a list containing the following: Balalaika, Bouqet, Outlook, Petticoat, Summit, Chime, Labourer, Patty, Persimmon, Sample.
my_list = ["Balalaika", "Bouqet", "Outlook", "Petticoat", "Summit", "Chime", "Labourer", "Patty", "Persimmon", "Sample"]
print(my_list)

#Turn the list into a set called my_set1.
my_set1 = set(my_list)
print(my_set1)

#Add Nucleotidase to the set.
my_set1.add("Nucleotidase")
print(my_set1)

#Remove Summit from the set.
my_set1.remove("Summit")
print(my_set1)

#Check if Violin is in the set.
check2 = "Violin" in my_set1
print(check2)

#Make another set called my_set2 containing the following: Alias, Assist, Belfry, Sideboard, Soap, Balalaika, Persimmon.
my_set2 = {'Alias', 'Assist', 'Belfry', 'Sideboard', 'Soap', 'Balalaika', 'Persimmon'}
print(my_set2)

#Find the elements that intersect the two sets.
intersect1 = my_set1 & my_set2
print(intersect1)

#Find the elements unique to my_set2.
print(f'{my_set2.difference(my_set1)}')

#Combine my_set1 and my_set2.
combined_set = my_set1.union(my_set2)
print(combined_set)

#Assign a = 16653509 and b = 2448111 and determine if the values are equal.
a = 16653509
b = 2448111
print(f'The variable a and b are equal: {a == b}')

#Use a comparison or logic operator to determine which is greater.
print(a < b)
print(f'The variable a is greater than b: {a > b}')