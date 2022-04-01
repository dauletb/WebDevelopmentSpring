a=input()
c=1
s=0
for i in range(len(a),0,-1):
    s=s+int(a[i-1])*c
    c=c*2
print(s)
