def end_other(a,b):
    al=a.lower()
    bl=b.lower()
    if al.endswith(bl):
        return True
    if bl.endswith(al):
        return True
    return False