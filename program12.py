# Read 10 numbers from user and find the average of all.
# a) Use comparison operator to check how many numbers are less than average and print them
# b) Check how many numbers are more than average.
# c) How many are equal to average.

numbers=[]
while(len(numbers)<10):
    val=input('enter a number: ')
    if val.isdigit():
        numbers.append(int(val))

avg=sum(numbers)/len(numbers)
print('Average: ',avg)
lesser,larger,equal=0,0,0
for i in numbers:
    if i>avg:
        larger+=1
    elif i<avg:
        lesser+=1
    else:
        equal+=1

print('no. of elements less than the average ',lesser)
print('no. of elements greater than the average ',larger)
print('no. of elements equals the average ',equal)


