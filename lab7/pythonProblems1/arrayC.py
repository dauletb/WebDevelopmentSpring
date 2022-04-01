x=int(input())
s=input()
l=s.split()
b=0
for i in l:
    if int(i)>0:
        b=b+1
print(b)
