def angle(From, To, Value):
    angle = { 
        "rad": 1, # radian
        "turn" : 6.28319, # turn
        "deg" : 0.0174533, # degree
        "grad" : 0.0157079, # gradian

        }
    
    return Value * angle[From] / angle[To]
    