m={4,7,2,1,9}
print(m)
print(type(m))
print(len(m))
n=set((3,7,9,5,8))
print(n)
for i in m:
    print(i)
m.add(3) 
print(m) 
m.update(n)
print(m)
m.discard(4)
print(m)
m.discard(0)
print(m)
m.pop()
print(m)
x=m.union(n)
print(x)
y=m.intersection(n)
print(y)
z=m.difference(n)
print(z)