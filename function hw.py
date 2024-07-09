def sum():
    a=20
    b=30
    print(a+b)
sum()
def multiply():
    a=20
    b=30
    print(a*b)
multiply()

# def average():
#     m=30
#     n=100
#     o=2000
#     k=(m+n+o)/3
#     print(k)
# average()

# def sum():
#     m=int(input("enter a number"))
#     sum=0
#     for i in range(1,m):
#         sum+=i
#     print(sum)
# sum()

# def factorial():
#     n=int(input("enter a number"))
#     fact=1
#     while(n>0):
#         fact=fact*n
#         n=n-1
#     print(fact)
# factorial()

# def year():
#     k=int(input("enter a year"))
#     if k%4==0:
#         print("leap year")
#     else:
#         print("not a leap year")
# year()

# def fibonacci(x):
#     a=0
#     b=1
#     print(a)
#     print(b)
#     for i in range(0,x+1):
#         c=a+b
#         a=b
#         b=c
#         print(c)
# fibonacci(5)

def number():
    a=6
    n=0
    if a>1:
         for i in range(1,a+1):
            if(a%i)==0:
                n=n+1
    if n==2:
        print("number is prime")
        return True
    else:
        print("number is not prime")
        return False
number()







    










