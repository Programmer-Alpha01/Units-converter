def volume(From,To,value):
    volume={
        'l':1,       # Litre
        'cubic':1000,# Cubic metre
        'gallon':3.785411784, # Gallon
        'pint':0.473176473, # Pint

        # Metric
        'mm3': 0.000001, # Cubic millimeter
        'mm^3': 0.000001, # Cubic millimeter
        'cm3': 0.001, # Cubic centimeter
        'cm^3': 0.001, # Cubic centimeter
        'm3': 1000, # Cubic meter
        'm^3': 1000, # Cubic meter
        'km3': 1000000000000, # Cubic kilometer
        'km^3': 1000000000000, # Cubic kilometer



    }

    return value * volume[From] / volume[To]
