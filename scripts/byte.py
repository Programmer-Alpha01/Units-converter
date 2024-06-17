def byte(From, To, Value):
    byte=['b','kb','mb','gb','tb','pb','eb','eb','zb','yb']
    return unit * (1024 ** (byte.index(From)-byte.index(To)))