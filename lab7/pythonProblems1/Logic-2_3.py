def make_chocolate(small, big, goal):
  if small+big*5<goal:
    return -1
  if big*5>=goal:
    if small>=goal%5:
      return goal%5
    else:
      return -1
  if big*5<goal:
    if small>=goal-big*5:
      return goal-big*5
    else:
      return -1