#comparison operator
# == != > >= < <= not
# name ='John'
# print(name=='john')
# print(name=='John')

# age=20
# print(age==19)
# print(age!=20)

# var = 6
# var2 = 7
# print(var != var2)
# print(var > var2)
# print(var < var2)
# print(var<=var2)
# print(var >=var2)


# logical operator 'AND'/'OR'

name = 'John'
age = 20

print('.......AND......')
print(name=='John'and age==20)
print(name=='james'and age==20)
print(name=='John'and age==19)
print(name=='James'and age==19)
# in AND operator the statement can only be true ie both
#  condition are true

name = 'John'
age = 20

print('.......OR......')
print(name=='John' or age==20)
print(name=='james' or age==20)
print(name=='John' or age==19)
print(name=='James' or age==19)
# OR will be true if one of the condition is true 

# assignment operator
# +=, -=, *=, /=, //=, %=

y=10
y=y+1
print(y)

x=10
x += 1
print(x)

x -= 2
print(x)

x *= 2
print(x)

x //= 2
print(x)

x /= 2
print(x)

x %= 2
print(x)


print(4.5%2)