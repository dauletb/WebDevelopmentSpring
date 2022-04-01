a=int(input())
if a==1:
    print("YES")
    quit()
if a==0:
    print("NO")
    quit()
y=a
x=2
b=True
while y>1:
    if y%x==1:
        b=False
        print("NO")
        break
    y=y/2
if b:
    print("YES")