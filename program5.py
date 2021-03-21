from sys import argv

# a) From the above statement your program should receive arguments and print them each of them.
print('The command line arguments are')
for val in argv[1:]:
    print(val)

# b) Find the biggest of three numbers, where three numbers are passed as command line arguments.

max=0
for val in argv[1:]:
    if val.isdigit():
        if int(val)>max:
            max=int(val)
print('Biggest of three numbers',max)



