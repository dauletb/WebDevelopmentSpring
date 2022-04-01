def has22(nums):
    pr=0
    b=False
    for x in nums:
        if x==2 and pr==2:
            b=True
        pr=x
    return b