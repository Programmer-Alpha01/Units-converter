def length(From, To, Value):
    length = { 
        # Metric
        "ym": 1*10**-24, # yoctometer
        "zm": 1*10**-21, # zeptometer
        "am": 1*10**-18, # attometer
        "fm": 1*10**-15, # femtometer
        "pm": 1*10**-12, # picometer
        "nm": 1*10**-9,  # nanometer
        "um": 1*10**-6,  # micrometer
        "cmm": 1*10**-5, # centimicron
        "dmm": 1*10**-4, # decimicron
        "mm": 0.001,    # millimeter
        "cm": 0.01,     # centimeter
        "dm": 0.1,      # decimeter
        "m": 1,         # meter
        "km": 1000,     # kilometer
        "Mm": 1000000,  # megameter
        "Gm": 1000000000, # gigameter
        "Tm": 1000000000000, # terameter
        "Pm": 1000000000000000, # petameter
        "Em": 1000000000000000000, # exameter
        "Zm": 1000000000000000000000, # zettameter
        "Ym": 1000000000000000000000000, # yottameter

        # Imperial
        "in": 0.0254,   # inch
        "ft": 0.3048,   # foot
        "yd": 0.9144,   # yard
        "fath": 1.8288, # fathom
        "ch": 20.1168,  # chain
        "fur": 201.168, # furlong
        "mi": 1609.344, # mile

        # Other

        "mil": 2.54*10**-5, # mil
        "thou": 2.54*10**-5, # thou

        "lp": 1.62*10**-35, # Planck length

        "au": 149597870700, # astronomical unit
        "ls": 299792458, # light second
        "lm": 17987547480, # light minute
        "lh": 107925284800, # light hour
        "ly": 9460730472580800, # light year
        "pc": 30856775814671900, # parsec

        "nmi": 1852,    # nautical mile
        }
    
    return Value * length[From] / length[To]
    