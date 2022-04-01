x=int(input())
s=input()
l=s.split()
b=True
for i in l:
    if b:
        print(i, end=" ")
    b=not b