def sum67(nums):
  b=True
  s=0
  for x in nums:
    if x==6:
      b=False
    if b:
      s=s+x
    if x==7:
      b=True
  return s