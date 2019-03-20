
"""
creating a class for family members
"""

class family_members:
    def __init__(self):

        self.list=[{'Name':' ','Age':' ','Gender':' ','id':' '}]

    def add_familyMember(self,name,age,gender,id):

        dict={'Name':name,'Age':age,'Gender':gender,"id":id}
        self.list.append(dict)
        return dict
#finding total members in a family
    def total_members(self):   
        return len(self.list)
#removing a family member by id
    
    
    def remove(self,index):
        a = self.list.pop(index)
        return a

    def remove_mem(self,id):
        for b,d in enumerate(self.list):
            if d.get("id",id) == id:
                del self.list[b]
                return ''
        
f= family_members() # creating an object for a class


"""
add a member to a family
"""
print(f.add_familyMember("mark",50,'male',121))
print(f.add_familyMember("tena",20 ,'female',155))
print(f.add_familyMember("paul",39,'male',154))
print(f.add_familyMember("mark",30,'female',122))
print("total numbers in a family : ", f.total_members())
print(f.remove_mem(121))
print(f.list)
