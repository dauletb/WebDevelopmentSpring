def no_teen_sum(a, b, c):
  def fix_teen(n):
    l=[13,14,17,18,19]
    if n in l:
      return 0
    return n
  a=fix_teen(a)
  b=fix_teen(b)
  c=fix_teen(c)
  return a+b+c