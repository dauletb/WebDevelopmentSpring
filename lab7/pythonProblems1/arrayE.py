x=int(input())
s=input()
l=s.split()
b=True
for i in range(1,len(l)):
    if (int(l[i])>=0 and int(l[i-1])>=0) or (int(l[i])<0 and int(l[i-1])<0):
        b=False
        print("YES")
        break
    
if b:
    print("NO")
