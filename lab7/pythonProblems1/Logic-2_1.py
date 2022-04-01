def lucky_sum(a, b, c):
  if a==b==c==13 or a==c==13 or a==b==13:
    return 0
  if b==c==13:
    return a
  if a==13:
    return c
  if b==13:
    return a
  if c==13:
    return a+b
  return a+b+c