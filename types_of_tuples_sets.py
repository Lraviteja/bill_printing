#creating_a_tuple_with_2*3_matrix
x = ('name',"roll no","class"),("Ravi","5","degree"),("teja","6","degree")
print('tuple_with_2*3_matrix_is :',x[1],'\n')

#tuple_constructor_manner
y = tuple (('name','age')) #double_rounded_brackets_is_must_for_a_constructor
print(y,'\n')

#rtuple_eprasentation_manner
a = 'Ravi'
z = tuple((a))
print('reprasentation_manner_of_a_tuple_is ',z,'\n')

#how_do_u_unpack_a_tuple
b = (1,4,5,4,3,3)
print('unpacked_tuple_is ',*b,'\n') #*_is_used_for_inpacking

#creating_a_dynamic_tuple
c = []
n = 5
for i in range (0,n):
    c.append(i) #append_is_used_to _add_the_values
print('dynamic_tuple_is ',tuple(c),'\n')

#sets
#set_constructor_manner
y = set(('name','age')) #double_rounded_brackets_is_must_for_a_constructor
print(y,'\n')

#set_reprasentation_manner
a1 = 'teja'
set = {a1}
print('reprasentation_manner_of_a_set_is ',set,'\n')

#set_operators(+,-,union,intersection)
fruits = {"banana","apple","mango"}
fruits.add("pineapple") #add_is_used_to_add_any_item(+)
print(fruits,'\n')

fruits.remove("mango") #ramove_is_used_to_remove_an_item(-)
print(fruits,'\n')

veg = {'keera','potato','tomato','banana'}
i = fruits.union(veg) #union_is_used_to_add_two_sets
print('union_of_a_set_is ',i,'\n')

j = fruits.intersection(veg) #intersection_is_used_to_remove_the_common)elements_from_two_sets
print('intersection_of_a_set_is ',j,'\n')

#sub_set
k = {"a,""j","i","c"}
l = {"b","d","e","m"}
print('subset_of_a_set_is ',k.issubset(l)) #subset_is_method_returns_true_or_false_if_the_same_elements_exists_in_the_next_set
print('superset_of_a_set_is ',l.issuperset(k))
