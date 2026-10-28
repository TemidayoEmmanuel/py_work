# python has two categories of data type 
# premitive data type 
# data collcetion 


# exmple of premitive data type
# stray
# integer
# boolean

# exmples of  data collection
# list 
# tuple
# dictionary 
# set


# learn = 'we are learning'
# print(type(learn))
# school = "Gskills"
# print(type(school))
# test = "'we are learning cybersecurity for the future'"
# print(type(test))
# # a Type classify an item this example showed str


# # len count the number of a value 
# info = 'we are learning how to protect system'
# print (len(info))

# #slice is  used to cut a part of a value of a list
# print(info [0:2])
# print(info [7:15])
# print(info[-6:])
# print(info[:15])
# print(info[-14:])


# #list method 
# print(info.upper())
# print(info.lower())
# print(info.title()) # this capitalize the first letter of every character
# print(info.capitalize())



# input for a user
# name = input ('please input your name:')
# print(name)

# # concatination means join to thing together
# course=input('which course are u doing ')
# print(course)
# print('toby '+'learning')
# print(name +' is learning '+ course)

# # strings formating
# print(f'{name} is learning {course}')


name = input ('please input your name:')
age = input('how old are you:')
course = input('what do you want to study:')
gender = input('gender:')
skill = input('do yu have any skill:')
status = input('are you married:')
print(f'''user name:{name}\n, user is {age}\n, 
user wants to study {course}\n, user is a 
{gender}\n, user has {skill}skils\n, user is {status}\n''')