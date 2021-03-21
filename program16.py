'''
Write program to perform following:
i) Check whether given number is prime or not.
ii) Generate all the prime numbers between 1 to N where N is given number.
'''
num=int(input('enter a number: '))
for i in range(2,num):
    if num%i==0:
        print('not prime')
        break
else:
    print('prime')

N=int(input('enter the range N: '))
for check in range(1,N+1):
    if check==1:
        continue
    else:

        for i in range(2,check):
            if check%i==0:
                break
        else:
            print(f'{check} is a prime number')
