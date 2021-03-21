'''
Using loop structures print even numbers between 1 to 100.
a) By using For loop, use continue/ break/ pass statement to skip odd numbers.
    i)Break the loop if the value is 50
    ii) Use continue for the values 10,20,30,40,50

b) By using while loop, use continue/ break/ pass statement to skip odd numbers.
    i)Break the loop if the value is 90
    ii) Use continue for the values 60,70,80,90
'''
print('i)Break the loop if the value is 50')
for i in range(1,101):
    if i==50:
        break
    else:
        if i%2==0:
            print(i)
        else:
            pass

print('ii) Use continue for the values 10,20,30,40,50')
for j in range(1,101):
    if j not in [10,20,30,40,50]:
        if j%2==0:
            print(j)
        else:
            pass
    else:
        continue

print('using while loop')
print('i)Break the loop if the value is 90')
k=1
while(k<=100):
    if k==90:
        break
    else:
        if k%2==0:
            print(k)
        else:
            pass
    k+=1
print('ii) Use continue for the values 60,70,80,90')
l=1
while(l<=100):
    if l in [60,70,80,90]:
        l+=1
        continue
    else:
        if l%2==0:
            print(l)
        else:
            pass
    l+=1