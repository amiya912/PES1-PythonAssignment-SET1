'''
Write program to find the biggest and Smallest of N numbers.
PS: Use the functions to find biggest and smallest numbers.
'''
N=int(input('enter the number N: '))
num=[]
for i in range(N):
    val=int(input('enter a num: '))
    num.append(val)
def calc(num):
    num.sort()
    big=num[len(num)-1]
    small=num[0]
    return(big,small)

big,small=calc(num)
print(f'biggest num is {big} and smallest num is {small}')
