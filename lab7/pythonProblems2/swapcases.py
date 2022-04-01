def swap_case(s):
    newS=s.swapcase()
    return newS

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)