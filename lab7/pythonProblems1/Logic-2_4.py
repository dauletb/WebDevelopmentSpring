def make_bricks(small, big, goal):
  if small+big*5<goal:
    return False
  if big*5>=goal:
    if small>=goal%5:
      return True
    else:
      return False
  if big*5<goal:
    if small>=goal-big*5:
      return True
    else:
      return False