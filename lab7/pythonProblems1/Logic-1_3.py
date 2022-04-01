def alarm_clock(a, vacation):
  if a>0 and a<6 and not vacation:
    return "7:00"
  if ((a==6 or a==0) and not vacation) or (a>0 and a<6 and vacation):
    return "10:00"
  if (a==6 or a==0) and vacation:
    return "off"