a=input()
l=list(a)
while l[len(l)-1]=="0":
    l.pop()
for i in range(len(l),0,-1):
    print(l[i-1],end="")
