def acceleration(u,v,t):
    """
    acceleration (acc/mps2 ) = (final speed (v/kmph) - initial speed (kmph) ) * (10/36) / time (t/s)
    """
    acc = round(((v-u)*(10/36)/t),2)
    return acc

def speed(d,t):
    """
    speed (v/kmph) = distance (d/km) / time (t/h)
    """
    s = round((d/t),2)
    return s

def gforce(acc):
    """
    gforce (g) = acceleration (acc/mps2) / 9.8 (mps2)
    """
    gf = round((acc/9.8),2)
    return gf
