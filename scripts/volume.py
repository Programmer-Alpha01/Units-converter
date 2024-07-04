def volume(From,To,value):
    volume={
        'l':1       # Litre
        'cubic':1000# Cubic metre
        'gallon':3.785411784 # Gallon
        'pint':0.473176473 # Pint
    }

    return value * volume[From] / volume[To]