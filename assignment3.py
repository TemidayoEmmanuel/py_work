results =int(input('what is your value:'))
con= (input('Add: +, -, *, /:'))
numb= int(input('what is your number:'))

if con == '+':
    print(f'Your result is: {results+numb}')
elif con == '-':
    print(f'Your result is: {results-numb}')
elif con == '*':
    print(f'Your result is: {results*numb}')
elif con == '/':
    print(f'Your result is: {results/numb}')
else:
    print('Invalid operator')