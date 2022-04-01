def near_ten(num):
  m=num%10
  if m<3 or 10-m<3:
    return True
  else:
    return False