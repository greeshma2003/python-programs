sum=0
for i in range(1,11):
    sum+=i
print(sum)

i=1
sum=0
while(i<=20):
    if(i%2==0):
        sum=sum+i
    i=i+1
print(sum)

i=5
fact=1
while(i>0):
    fact=fact*i
    i=i-1
print(fact)

x=int(input("enter the number of terms"))
sum=0
for i in range(1,10+1):
    sum+=(i*i)
print(sum)

a=5
count=0
if a>1:
    for i in range(1,a+1):
        if(a%i)==0:
            count=count+1
    if count==2:
        print("number is prime")        



