list=[]
s=input()
l=s.split()
for i in l:
    list.append(i)
x=list[0]
for i in list:
    if x>i:
        x=i
print(x)