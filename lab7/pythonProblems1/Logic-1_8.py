def squirrel_play(temp, is_summer):
  if (temp>59 and temp<91 and not is_summer) or (temp>59 and temp<101 and is_summer):
    return True
  else:
    return False