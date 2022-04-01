def caught_speeding(speed, is_birthday):
  if is_birthday:
    speed=speed-5
  if speed<=60:
    return 0
  if speed<81 and speed>60:
    return 1
  else:
    return 2