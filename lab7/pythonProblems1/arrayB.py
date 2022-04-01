x=int(input())
s=input()
l=s.split()
for i in l:
    if int(i)%2==0:
        print(i, end=" ")