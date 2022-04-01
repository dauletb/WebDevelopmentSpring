from posixpath import split

s=input()
l=s.split()
def func(x,y):
    if x==y:
        print(0)
    if x!=y:
        print(1)
func(l[0],l[1])