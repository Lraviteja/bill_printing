'''
remove any number from a list
'''

a = [12,24,35,24,88,120,155]
print('Before:',a)
i = int(input('Enter any number:'))
j=i
for i in a:
    if i == j:
        a.remove(j)
print(a)
