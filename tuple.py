#tuple is a data collection that is use to create a unmutated data type
#  (this are data type that can't be changed )
# it activiated with()
family = ('abraham','wealth','chiendu','james')
print(family[0])
print(len(family))

print(type(family))
family = list(family)#tuple convation
print(type(family))
family[0]='mike'
print(family)