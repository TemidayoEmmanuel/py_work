names = ['john']
print(type(names))
items = ['phone', 'laptop','bag']
toby = ['watch', 'car', 'mansion']
friends = ['max','tunde', 'john','david']

# indexing: this help to alter a value on the list.

friends[0] = 'james'
friends[3] = 'mike'
print(friends)

# len:counts the number of a value in list
print(len(friends))
print(toby)
print(items)

# .append:this helps to add an value to the end of the list
friends.append('abraham')
print(friends)

# pop : remove from the end of the value
friends.pop()
print(friends)

# insert:is use to add to the a specify part of a list
friends.insert(2,'samuel')
print(friends)
