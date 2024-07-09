def printname():
    print("hello")
printname()
def sum():
    a=3
    b=6
    print(a+b)
sum()

def add(x,y):
    print(x+y)
add(4,5)
# arbitrary arg
def subtract(* x):
    print(x[2]-x[1])
subtract(20,40,60,80)
# keyword arg
def multiply(x,y,z):
    print(x*y*z)
multiply(x=3,y=5,z=7)
# arb-key arg
def sum(**x):
    print(x["i"]+x["j"])
sum(i=25,j=35,k=45,l=55)
# default
def mycountry(c="india"):
    print("iam from "+c)
mycountry("usa")
mycountry("canada")
mycountry()
def name(x):
    for i in x:
        print(i)
y=["greeshma","arathi","aswathy","gokul"]
name(y)

def numbers(x):
    return 10+x
print(numbers(20))
def add():
    pass

y=lambda x:x+5
print(y(10))
z=lambda x,y:x+y
print(z(4,8))





    