'''
Create a list with at least 10 elements having integer values in it;
Print all elements
Perform slicing operations
Perform repetition with * operator
Perform concatenation with other list.
'''
list1=[]
while len(list1)<10:
    val=input('enter an element: ')
    if val.isdigit():
        list1.append(val)

print('printing the numbers in the list')
for i in list1:
    print(i)



print('performing slicing operations')
print('printing the first half of the list')
for i in list1[:int(len(list1)/2)]:
    print(i)

print('printing the second half of the list')
for i in list1[int(len(list1)/2):]:
    print(i)

print('performing repetition')
list2=list1*5
print(list2)

print('concatenation')
list3=[100,99,98,97]
print(list1+list3)



