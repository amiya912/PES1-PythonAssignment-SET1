'''
Write a program to create two list A & B such that List A contains Employee Id, List B contain Employee name (minimum 10 entries in each list) & perform following operation
a) Print all names on to screen
b) Read the index from the user and print the corresponding name from both list.
c) Print the names from 4th position to 9th position
d) Print all names from 3rd position till end of the list
e) Repeat list elements by specified number of times (N- times, where N is entered by user)
f) Concatenate two lists and print the output.
g) Print element of list A and B side by side.(i.e.List-A First element, List-B First element )
'''

listA=[1,2,3,4,5,6,7,8,9,10]
listB=['Amy','Billy','Charlie','Dante','Elliot','Flake','Gally','Harry','Ina','Jose']

print('a.All names on the screen: ')
for name in listB:
    print(name)

print('b.Read the index from the user and print the corresponding name from both list.')
i=int(input('enter the index position between range 0 to 9: '))
print(f'Emp No: {listA[i]}\nName: {listB[i]}')

print('c) Print the names from 4th position to 9th position')
print(listB[3:9])

print('d) Print all names from 3rd position till end of the list')
print(listB[2:])

print('e) Repeat list elements by specified number of times (N- times, where N is entered by user)')
rep=int(input('enter the repetition value: '))
print(listA*rep)
print(listB*rep)

print('Concatenate two lists and print the output.')
concat_list=listA+listB
print(concat_list)

print('Print element of list A and B side by side.(i.e.List-A First element, List-B First element ')
for emp,name in zip(listA,listB):
    print(f'{emp},{name}')
