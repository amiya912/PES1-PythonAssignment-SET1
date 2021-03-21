'''
Create a tuple with at least 10 elements having integer values in it;
Print all elements
Perform slicing operations
Perform repetition with * operator
Perform concatenation with other tuple.
'''
tup1=(1,2,3,4,5,6,7,8,9,10)
print('printing all the elements')
for i in tup1:
    print(i)

print('performing slicing operations')
print('first half')
for i in tup1[:int(len(tup1)/2)]:
    print(i)
print('second half')
for j in tup1[int(len(tup1)/2):]:
    print(j)

print('performing repetition')
tup2=tup1*3
print(tup2)

print('performing concatenation')
tup3=(11,22,33,44,55,66)
print(tup1+tup3)



