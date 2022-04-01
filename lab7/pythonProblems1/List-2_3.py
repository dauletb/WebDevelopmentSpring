def sum13(nums):
    s=0
    pr=0
    for x in nums:
        if x!=13 and pr!=13:
            s=s+x
        pr=x
    return s 
