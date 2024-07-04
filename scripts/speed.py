def speed(From,To,value):
    speed={
        'ms':1,                     # Metre per second
        'kmh':3.6,                  # Kilometre per hour
        'mph':2.23693629,           # Miles per hour 
        'knot':0.514444444,         # Knot
        'fps':3.280840,             # Feet per second
        'march':340.29000,          # Speed of sound
        'c':299792458,              # Speed of light 
        'planck':2.99792458*(10**8) # Planck speed
    }

    return value * speed[From] / speed[To]