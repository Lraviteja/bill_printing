"""
here i am going to give the explanation about dictionaries
and key words used in dictionaries
"""

"""
1.find all keys and values in dictionary
"""
people = {
    'name':'ravi',
    'age':21,
    'gender':'male'
}
a=people.keys() #.key()_returns_key_in_a_dilisctionary
b=people.values() #.value()_returns_values_in_a_dictionary
print(a,'\n',b)

"""
2.converting tuple to dictionary and dictionary to tuple
"""
#tuple_into_dictionary
a=((1,2),(3,4))
print(dict(a))

#dictionary_to_tuple
print(tuple(people))

"""
3.list of dicticts
"""
b=[{'name':'ravi','course':'python'},{'company':'team247'}]
print(b)

"""
4.sort key of dictionary
"""
print(sorted(people)) #sorted_key_word_is_used_to_sort_the_elements

"""
5.finding no.of keus in a dictionary
"""

print(len(people.keys())) #len_key_word_is_used_to_find_the_length
print(list(people.keys())) #list_key_word_is_used_to_find_keys_in_a_dict

"""
6.nested dictionaries
"""
nested = {'fruits':{'apple','banana','mango','orange','grapes',},
          'number':{10,25,6,12,40}}
print(nested)

"""
7.read a value from dict
"""

print(people["name"])

"""
8.about copy()
"""

persons = people.copy()
print(persons)
