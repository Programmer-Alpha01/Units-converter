def length(From, To, Value):
    length = { 
        # Metric
        "pm": 0.000000000001, # picometer
        "nm": 0.000000001, # nanometer
        "um": 0.000001, # micrometer
        "mm": 0.001,    # millimeter
        "cm": 0.01,     # centimeter
        "dm": 0.1,      # decimeter
        "m": 1,         # meter
        "km": 1000,     # kilometer
        # Imperial
        "in": 0.0254,   # inch
        "ft": 0.3048,   # foot
        "yd": 0.9144,   # yard
        "fath": 1.8288, # fathom
        "ch": 20.1168,  # chain
        "fur": 201.168, # furlong
        "mi": 1609.344, # mile
        # Nautical
        "au": 149597870700, # astronomical unit
        }
    
    return Value * length[From] / length[To]
    