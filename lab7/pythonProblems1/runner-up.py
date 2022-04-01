a=input()
l=a.split()
m=l[0]
for i in l:
    if int(i)>int(m):
        m=i
while m in l:
    l.remove(m)
m=l[0]
for i in l:
    if int(i)>int(m):
        m=i
print(m)

        

