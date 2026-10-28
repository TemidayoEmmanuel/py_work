results =input('what is your name:').capitalize() #THIS HELP THE USER MAINTAIN A LOWERCASE WHEN INPUTING 

if results =='Toby':
    toby_grade = int(input('input your grade:'))
    # this what i did wrong
    if toby_grade >= 80 and toby_grade <= 100: 
            print('A')
    
    elif  toby_grade >= 70 and toby_grade <= 79:
        print('B')

    elif toby_grade >= 60 and toby_grade <= 69: 
        print('C')

    elif toby_grade >= 50 and toby_grade <= 59: 
        print('D')
  
    elif toby_grade >= 40 and toby_grade <= 49: 
            print('E')
    
    else:
         print('He never came for class')
       
            



elif results =='Mike':
    mike_grade = int(input('input your grade:'))
    # this what i did wrong
    if mike_grade >= 80 and mike_grade <= 100: 
            print('A')
    
    elif  mike_grade >= 70 and mike_grade <= 79:
        print('B')

    elif mike_grade >= 60 and mike_grade <= 69: 
        print('C')

    elif mike_grade >= 50 and mike_grade <= 59: 
        print('D')
  
    elif mike_grade >= 40 and mike_grade <= 49: 
            print('E')
    
    else:
         print('He never came for class')


elif results =='John':
    john_grade = int(input('input your grade:'))
    # this what i did wrong
    if john_grade >= 80 and john_grade <= 100: 
            print('A')
    
    elif  john_grade >= 70 and john_grade<= 79:
        print('B')

    elif john_grade >= 60 and john_grade <= 69: 
        print('C')

    elif john_grade >= 50 and john_grade <= 59: 
        print('D')
  
    elif john_grade >= 40 and john_grade <= 49: 
            print('E')
    
    else:
         print('He never came for class')

else :
    print('result not found')