student = {
    'name':'john',
    'age':20,
    'course':'python'
}
print(type(student))
print(student)
print(student.keys())
print(student.values())
print(student.items())
# if you want to add 
# student.update({'grade':'A'})
# print(student)
# student.popitem() #this removes the last item
# print(student)
# student.pop('name')# this remove specify item
# print(student)
# #method 2
# del student ['age']
# print(student)
student['name']='peter'# this is how to change a key value
print(student)
