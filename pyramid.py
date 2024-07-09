limit=int(input("enter the limt: "))
for i in range(1,limit+1):
    for j in range(0,i):
        print("*", end=' ')
         print()  

n=int(input("emter the number of raws: "))
for i in range(5):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()