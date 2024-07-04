def byte(From, To, Value):
    byte=['b','kb','mb','gb','tb','pb','eb','eb','zb','yb','rb','qb']
    return Value * (1000 ** (byte.index(From)-byte.index(To)))

