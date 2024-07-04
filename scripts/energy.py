def energy(From,To,value):
    energy={
        'j':1,                  # Joule
        'watt':1,               # watt
        'kj':0.001,             # Kilo Joule
        'kwh':3.6*(10**6),      # Kilowatt-hour
        'cal':4.184,            # Calorie
        'btu':1055,             # British Thermal Unit
        'quad':1055*(10**15),   # Quad
        'therm':100000*1055,    # Therm
        'mcf':10.27*100000*1055,# One thousand cubic feet of gas
        'planck':1.96*(10**-9)  # Planck energy
    }

    return value * energy[From] / energy[To]