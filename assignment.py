# letter = ['a','b','c','d','e''f' 'g' 'h' 'i' 'j' 'k' 'l' 'm' 'n' 'o' 'p' 'q' 'r' 's' 't' 'u' 'v' 'w' 'x' 'y' 'z']
# print(type(letter))
# print(letter)

# results =input('what is your name:').capitalize() #THIS HELP THE USER MAINTAIN A LOWERCASE WHEN INPUTING 

# if results =='Toby':
#     toby_grade = int(input('input your grade:'))
#     # this what i did wrong
#     if toby_grade >= 80 and toby_grade <= 100: 
#             print('A')
    
#     elif  toby_grade in range(70-79):
#         print('B')

#     elif toby_grade in range(60-69):
#         print('C')

#     elif toby_grade in range(50-59):
#         print('D')
  
#     elif  toby_grade in range (49-40):
#             print('E')
    
#     else:
#          print('He never came for class')
       
            



# elif Todo_list =='Mike':
#     print('meetings')


# elif Todo_list=='John':
#       print('go for classes')


# else :
#     print('result not found')

# ......answers,.........


# letters = 'ABCDEFGHIJKLBNOPQRSTUVWXYZ'
# New_list = []
# for i in letters :
#       New_list.append(i)
# print(New_list)

student = input('input your name: ')
grade = int(input(' please input your grade: '))
if grade >= 80 and grade <= 100:
      print(f'{student} you grade is A')
elif grade >= 70 and grade <=79:
      print(f'{student} you grade is B')
elif grade >= 60 and grade <=69:
      print(f'{student} you grade is C')
elif grade >= 50 and grade <=59:
      print(f'{student} you grade is D')
elif grade >= 40  and grade <=69:
      print(f'{student} you grade is E')
else:
    print(f'{student} have you  been in class')