x=int(input())
s=input()
l=s.split()
b=0
if len(l)<3:
    print(0)
    quit()
for i in range(1,len(l)-1):
    if int(l[i])>int(l[i-1]) and int(l[i])>int(l[i+1]):
        b=b+1
print(b)