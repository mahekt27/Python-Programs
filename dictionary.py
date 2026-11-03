# Dictionary:
'''
print("using item method for both keys and values:")
for i.j in dict1.itmems();
    print(i,":",j)

#copying dictionary to another 
print("Copying dictionary")
cpdict=dict1.copy()
print("copied dictionary=" ,cpdict)
#2nd way
cpdict1=dict(dict1)
print("Using dict method to copy".cpdict1)
'''
print("Nested Dictionaries")
Students = {
            1:{'name':'mahek','age':'21','gender':'male'},
            2:{'name':'janvi','age':'20','gender':'female'}
           }
print(Students)
print(Students[1]['name'])
print(Students[2]['age'])

print("Add another dictionary to the nested dictionary")
Students[3]={'name':'nidhi','age':'19','gender':'female'}
print(Students)

print("Delete elements from the nested dictionary")
del Students[2]['age']
del Students[3]['age']
print(Students)

print("Using loop to access the nested dictionary")
for skey,sdet in Students.items():
    print(skey,sdet)

print("Another way to access nested dictionary")
for skey,sdet in Students.items():
    print("\nStudent Id:" ,skey)
    for key in sdet:
        print(key + ":",sdet[key])

print("Set default when the key is in the dictionary")
Student1={'name':'mahek','age':21}
age=Student1.setdefault('age')
print('Student= ',Student1)
print("Age= ",age)

print("Set default when key is not in the dictionary")
phone=Student1.setdefault('phone')
print('Student= ',Student1)
print("phone= ",phone)

print("Set default when key is not in the dictionary, default vvalue is provided")
class1=Student1.setdefault('class1','MCA SEM I')
print('Student= ',Student1)
print('Class of Student= ',Student1)
