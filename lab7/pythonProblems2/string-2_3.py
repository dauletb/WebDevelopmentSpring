import re
def count_code(a):
    x=re.findall("co.e",a)
    return len(x)