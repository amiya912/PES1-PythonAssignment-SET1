'''
Create a list of 5 names and check given name exist in the List.
a) Use membership operator (IN) to check the presence of an element.
b) Perform above task without using membership operator.
c) Print the elements of the list in reverse direction.
'''
names=['Amy','Billy','Charlie','Dante','Elliot']
search=input('enter the name to be searched: ')
if search in names:
    print('present')
else:
    print('absent')

for name in names:
    if name==search:
        print('present')
        break
else:
    print('not present')

for name in names[::-1]:
    print(name)

