def pressure(From, To, Value):
    pressure = { 
        "Pa": 1, # Pascal

        "kPa" : 1000, # kilopascal
        "MPa" : 1000000, # megapascal
        "GPa" : 1000000000, # gigapascal
        "TPa" : 1000000000000, # terapascal

        "Ba" : 100, # barye

        "bar" : 100000, # bar
        "atm" : 101325, # atmosphere
        "torr" : 133.322, # torr
        "psi" : 6894.76, # psi

        "at" : 98066.5, # technical atmosphere

        # Centimetre or millimetre of water
        "cmH2O" : 98.0665, # centimetre of water
        "mmH2O" : 9.80665, # millimetre of water


        
        'planck': 4.63309*(10**113)
        }
    
    return Value * pressure[From] / pressure[To]
    
