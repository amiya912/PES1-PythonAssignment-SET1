'''Write a program to find the biggest of 4 numbers.
 a)Read 4 numbers from user using Input statement.
 b) extend the above program to find the biggest of 5 numbers.
(PS: Use IF and IF & Else, If and ELIf, and Nested IF) '''

a=int(input('enter the first num: '))
b=int(input('enter the second num: '))
c=int(input('enter the third num: '))
d=int(input('enter the fourth num: '))

if a>b and a>c and a>d:
    print('a:%d is the biggest number'%a)
    max=a
elif b>a and b>c and b>d:
    print('b:%d is the biggest number'%b)
    max=b
elif c>a and c>b and c>d:
    print('c:%d is the biggest number'%c)
    max=c
else:
    print('d:%d is the biggest number'%d)
    max=d

e=int(input('enter the fifth num: '))
if e>max:
    print('e:%d is the new max'%e)
else:
    print('max is still %d',max)