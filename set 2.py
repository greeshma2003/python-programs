a={6,3,7,1,8}
print(a)
print(type(a))
print(len(a))
b={2,4,7,8,9}
print(b)
for i in a:
    print(i)
a.add(4)
print(a)
a.update(b)
print(a)
a.remove(3)
print(a)
a.discard(4)
print(a)
a.discard(7)
print(a)
a.pop()
print(a)
# a.clear()
# print(a)
# del a
# print(a)
c=a.union(b)
print(c)
d=a.intersection(b)
print(d)
e=a.difference(b)
print(e)
