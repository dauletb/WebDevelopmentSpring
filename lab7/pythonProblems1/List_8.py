import re


def sum2(a):
    if len(a)==1:
        return a[0]
    if len(a)==0:
        return 0
    else:
        return a[0]+a[1]