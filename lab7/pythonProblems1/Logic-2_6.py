def round_sum(a, b, c):
  return round10(a)+round10(b)+round10(c)
  
def round10(num):
  if num%10>4:
    num=num+10-num%10
  else:
    num=num-num%10
  return num