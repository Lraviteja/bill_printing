
#creating_a_list
a=['banaba','12','magos','6','apples','20'] #a_defines_list_variable
print('created_list_is  ',a,'\n')

#creating_a_dynamic_list
x = []
n = 10
for x in range(0, n): 
    print('dynamic_ldt_id  ',x,'\n')

#creating_a_list_by_8th_position_is_none
b=list(('ravi','raju','teja','venkat','21','20','22','25','none','class'))
print('8th_position_reeplaced_with_none  ',b,'\n')

#replace_the_7th_position
lst=['string','int','char','dir','doc','variable','comment','data','syntax']
lst[7]=' '
print('7th_positiomn_replaced_with_space ',lst,'\n')

#creating_a_list_with_length_10
my_list=['maths','physics','chemistry','biology','zoologu','social','history','economics','civics','auditing']
print('10_characters_list_is  ',len(my_list),'\n')

#sorting_a_list
bikes=['ninja','royal enfield','fz','r15']
bikes.sort(),print('sorted_looist_is  ',bikes,'\n')

#reversing_a_list
bikes.reverse()
print('reverse_list_is  ',bikes,'\n')

#index_of_list
cls=['name','class','gender','sec','age']
print('index_is  ',cls.index('sec'),'\n')

#remove_nth_elemnt
cls.remove('sec')
print('list_after_removing  ',cls,'\n')

#cloning_a_list
cls1 = cls.copy()
print('cloned_list_is  ',cls1,'\n')

#slice_btwn_two_list
print('sluced_list_is  ',a[3:6],'\n')

#remove_by_index
i = cls.index('age')
print('removed_by_index_element_is ',cls.pop(i),'\n','after_removing_index_list_is  ',cls,'\n')

#joining_of_two_lists
two =bikes+cls
print('after_joining_two_lists  ',two,'\n')

#duplocate_elements_in_a_list
i =[1 ,2, 3, 2, 4 ,3, 1, 5]
print('list_after_removing_duplicate_elemnets  ',set(i))

