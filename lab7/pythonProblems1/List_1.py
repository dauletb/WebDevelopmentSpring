def same_first_ch(a):
    if len(a)<2:
        return False
    if a[0]==a[len(a)-1]:
        return True