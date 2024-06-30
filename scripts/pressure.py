def pressure(From, To, Value):
    pressure = { 
        "Pa": 1, # Pascal

        "bar" : 100000, # bar
        "atm" : 101325, # atmosphere
        "torr" : 133.322, # torr
        "psi" : 6894.76, # psi

        "at" : 98066.5, # technical atmosphere

        }
    
    return Value * pressure[From] / pressure[To]
    