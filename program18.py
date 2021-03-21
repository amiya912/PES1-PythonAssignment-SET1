'''
Using loop structures print numbers from 1 to 100. and using the same loop print numbers from 100 to 1 (reverse printing)
a) By using For loop
b) By using while loop
c) Let mystring ="Hello world"

print each character of mystring in to separate line using appropriate loop structure
'''

numbers=range(1,101)
for num in numbers:
    print(num)
    print(numbers[-num])

print('\n\nusing while loop\n\n')
pos=0
while(pos<len(numbers)):
    print(numbers[pos])
    print(numbers[len(numbers)-1-pos])
    pos+=1

for letter in 'mystring':
    print(letter)