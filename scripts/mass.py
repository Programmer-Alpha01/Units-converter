def mass(From,To,value):
    mass={
        # Factor
        'Qg':10**27,
        'Rg':10**24,
        'Yg':10**21,
        'Zg':10**18,
        'Eg':10**15,
        'Pg':10**12,
        'Tg':10**9,
        'Gg':10**6,
        'Mg':10**3,
        'kg':1,
        'hg':10*-1,
        'dag':10*-2,
        'g':10**-3,
        'dg':10**4,
        'cg':10**-5,
        'mg':10**-6,
        'ug':10**-9,
        'ng':10**-12,
        'pg':10**-15,
        'fg':10**-18,
        'ag':10**-21,
        'zg':10**-24,
        'yg':10**-27,
        'rg':10**-30,
        'qg':10**-33,

        # Imperial
        'tonne':1000,
        'pound':0.45359237,
        'oz':0.0283495231,
        'lb':0.453592338,
        'st':6.35029318,

        # Other
        'planck':2.17643424*(10**-8),            # Planck mass
        'da':1.6605390666050*(10**-27),      # Atomic mass unit (AMU)
        'electron':	9.1093835611*(10**-31),  # One electron mass
        'proton':1.6726219236951*(10**-27),  # One Proton mass
        'neutron':1.67492747121*(10**-27),   # One Neutron mass

        'mass-sun':1.98892*(10**30),         # Solar Mass
        'mass-mer':3.3022*(10**23),          # Mercury Mass
        'mass-ven':4.8676*(10**24),          # Venus Mass        
        'mass-earth':5.9722*(10**24),        # Earth Mass
        'mass-moon':7.34767309*(10**22),     # Lunar Mass
        'mass-mars':6.4185*(10**23),         # Mars Mass
        'mass-jup':1.8986*(10**27),          # Jupiter Mass
        'mass-sat':5.6846*(10**26),          # Saturn Mass
        'mass-nep':1.0243*(10**26),          # Neptune Mass
        'mass-pluto':5.6846*(10**26),        # Pluto Mass
        
    }
    
    return value * mass[From] / mass[To]