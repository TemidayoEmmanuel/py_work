text= [1,'a',2,3,4,'b','c','d','e',10,20]
num=[]
txt=[]
for i in text:
    if type(i)==int:
        num.append(i)
    else: 
        txt.append(i)
print(num, txt)




print('******2*********')

step= [2,3,4,6,]
new_step = []
incase = 3
for k in step:
    new_step.append(k*incase)
print(new_step)


print('*********3***********')
products= {
    'phone':800000,
    'car':3000000,
    'house': 50000000,
    'laptop':150000
}
discount={}
incase = 0.05
for k,v in products.items():
    if v >= 2000000:
        discount.update({k:v-(v*incase)})
    else: 
        print(v) 
print(discount)
    

