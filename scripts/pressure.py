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

        # Copper units of pressure
        "cPa" : 1.33322, # centipascal
        "mPa" : 133.322, # millipascal
        "uPa" : 133.322, # micropascal
        "nPa" : 133.322, # nanopascal
        "pPa" : 133.322, # picopascal
        "fPa" : 133.322, # femtopascal
        "aPa" : 133.322, # attopascal
        "daPa" : 133.322, # decapascal
        "hPa" : 1333.22, # hectopascal
        "kPa" : 13332.2, # kilopascal
        "MPa" : 133322000, # megapascal
        'planck': 4.63309*(10**113)
        }
    
    return Value * pressure[From] / pressure[To]
    