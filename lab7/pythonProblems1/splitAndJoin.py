def split_and_join(line):
    l=line.split()
    s=""
    for i in l:
        s=s+"-"+i
    return s[1:len(s)]

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)