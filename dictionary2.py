x={"class":"6","subject":"social","mark":"48"}
print(x)
print(type(x))
print(len(x))
y=dict(colour="blue",fruit="apple",vehicle="car")
print(y)
print(x["class"])
print(x.get("subject"))
print(x.keys())
print(x.values())
print(x.items())
print("class" in x)
print("class" not in x)
x["mark"]=49
print(x)
x.update({"mark":47})
print(x)
x["age"]="12"
print(x)
x.pop("subject")
print(x)
x.popitem()
print(x)
del x ["class"]
print(x)
for i in x:
    print(i)
for i in y:
    print(i) 
for i in y.keys():
    print(i)
for i in y.values():
    print(i)
for i in y.items():
    print(i)
z=y.copy()
print(z)




