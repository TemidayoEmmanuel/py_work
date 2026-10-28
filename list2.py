
# proper use of append 
# info = []
# name = input('enter your name:')
# email = input('enter your gmail:')
# info.append(name)
# info.append(email)
# print(info)

#slice is  used to cut a part of a value of a list
friends = ['john','james',['cat','dog'], 'abraham']
# print(friends[0:2])
# print(friends[2:4])
# print(friends[-1:])
# print(friends[1:2]) 
# print(friends[2][0]) # this is to print the cat
# print(friends[2][1]) # this is to print the dog 



#extend joins to lists together 
# num = [1,2,3,4]
# num2 = [5,6,7,8]
# num.extend(num2)
# print(num)


schoolFriends = ['max','tunde','john','david']
courseMate = ['joy','Ebube','gift','oscar']
schoolFriends.extend(courseMate)
print(schoolFriends)


#copy
people = schoolFriends.copy()
print(people) 
#method2
people = schoolFriends[:]
print(people)

#empty
# schoolFriends.clear()
# print(schoolFriends)

