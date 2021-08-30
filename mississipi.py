def most_frequent():
    wd = 0
wd = input("please enter a string")
m = 0
a = 0
s = 0
p = 0
for i in wd:
    if i == "m":
        m+=1
    if i == "i": 
        a+=1
    if i == "s":
        s+=1
    if i == "p":
        p+=1
print ("i = 0", a)
print ("s = 0", s)
print ("p = 0", p)
print ("m = 0", m)

most_frequent()
