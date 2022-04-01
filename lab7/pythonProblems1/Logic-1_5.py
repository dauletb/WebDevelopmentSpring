def in1to10(n, outside_mode):
  if (n<11 and n>0 and not outside_mode) or ((n<2 or n>9) and outside_mode) :
    return True
  return False