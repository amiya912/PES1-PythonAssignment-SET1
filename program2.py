# Write a program to find biggest of three numbers (use if condition)

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))
if a > b and a > c:
    print('Biggest number is %d' % a)

elif b > a and b > c:
    print('Biggest number is %d' % b)

else:
    print('Biggest number is %d' % c)