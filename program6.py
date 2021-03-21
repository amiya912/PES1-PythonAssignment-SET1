# Write a program to read string and print each character separately
line=input('Enter a string: ')
print('printing each character separately')
for letter in line:
    print(letter)
print('\n')

# a) Slice the string using slice operator [:] slice the portion the strings to create a sub strings.
sub1=line[:int(len(line)/2)]
sub2=line[int(len(line)/2):]
print('slicing the string into two halves\nsubstring1: %s\nsubstring2: %s '%(sub1,sub2))
print('\n')

# b) Repeat the string 100 times using repeat operator *
print('printing the string 100 times\n',line*100)
print('\n')

#  c) Read string 2 and concatenate with other string using + operator.
line2=input('Please enter string 2: ')
print('concatenation of two string: ',line+line2)