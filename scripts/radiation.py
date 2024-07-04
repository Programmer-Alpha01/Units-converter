def radiation(From,To,value):
    radiation={
        'rad':1,            # radiation unit
        'gy':0.01,          # Gray
        'jkg':0.01,

        'drad':1*(10**-1),  # decirad
        'crad':1*(10**-2),  # centirad 
        'mrad':1*(10**-3),  # millirad
        'urad':1*(10**-6),  # microrad
        'nrad':1*(10**-9),  # nanorad
        'prad':1*(10**-12), # picorad
        'frad':1*(10**-15), # femtorad	
        'arad':1*(10**-18), # attorad
        'zrad':1*(10**-21), # zeptorad
        'yrad':1*(10**-24), # yoctorad
        'rrad':1*(10**-27), # rontorad
        'qrad':1*(10**-30), # quectorad
        'darad':1*(10**1),  # decarad
        'hrad':1*(10**2),   # hectorad
        'krad':1*(10**3),   # kilorad
        'Mrad':1*(10**6),   # megarad
        'Grad':1*(10**9),   # gigarad
        'Trad':1*(10**12),  # terarad
        'Prad':1*(10**15),  # petarad
        'Erad':1*(10**18),  # exarad
        'Zrad':1*(10**21),  # zettarad
        'Yrad':1*(10**24),  # yottarad
        'Rrad':1*(10**27),  # ronnarad
        'Qrad':1*(10**30)   # quettarad

    }

    return value * radiation[From] / radiation[To]