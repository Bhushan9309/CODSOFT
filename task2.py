#Python program to make a simple calculator for two input numbers
print('two numbers below:')
a=int(input('enter first number:'))
b=int(input('enter second number:'))
ch=0
while  ch<5:
    print('Calculator Menu')
    print('1.Add')
    print('2.Subtract')
    print('3.Multiply')
    print('4.Divide')
    ch=int(input('Enter Your Choice:'))
    if ch==1:
        c=a+b;
        print('Sum:',c)
    elif ch==2:
        c=a-b
        print('Difference:',c)
    elif ch==3:
        c=a*b
        print('Product:',c)
    elif ch==4:
        c=a/b
        print('Quotient:',c)
    else:
        print('Invalid Option')
