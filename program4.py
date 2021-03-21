# Write a program to find whether a number is prime or not

a = int(input('enter a number: '))
count = 0
for i in range(2, a):
    if a % i == 0:
        count += 1
if count == 0:
    print("Prime")
else:
    print('Not Prime')
