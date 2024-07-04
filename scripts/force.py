def force(From, To, Value):
    force = { 
        "N": 1, # Newton

        "dyne": 1*10**-5, # dyne
        "kp": 9.80665, # kilopond
        "lbf": 4.44822, # pound-force
        "pdl": 0.138255, # poundal

        'planck':1.21031359*(10**44)    # Planck Force
        }
    
    return Value * force[From] / force[To]
    
