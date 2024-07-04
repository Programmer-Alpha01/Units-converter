
def pressure(From, To, Value):
    pressure = { 
        # Pascals
        "Pa": 1,
        "kPa": 1000,
        "MPa": 1000000,
  
        # Bars
        "mbar": 100,
        "bar": 100000,

        # Psi
        "psi": 6894.757,

        # Atmospheres
        "atm": 101325,


        # p=ρgh
        # Torr (mmHg), inHg 
        "Torr": 0.0075006168,
        "mmHg": 0.0075006168,
        "inHg": 0.0075006168 * 25.4,

        # Water
        "mmH2O": 0.10197162,
        }
    
    return Value * pressure[From] / pressure[To]
    

print(pressure("inHg", "mmHg", 1)) # 1 atm = 1.01325 bar
