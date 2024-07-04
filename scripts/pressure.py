def pressure(From, To, Value):
    pressure = { 
        "Pa": 1, # Pascal

        "bar" : 100000, # bar
        "atm" : 101325, # atmosphere
        "torr" : 133.322, # torr
        "psi" : 6894.76, # psi

        "at" : 98066.5, # technical atmosphere

        'planck': 4.63309*(10**113)
        }
    
    return Value * pressure[From] / pressure[To]
    