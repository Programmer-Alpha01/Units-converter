def force(From, To, Value):
    force = { 
        "N": 1, # Newton

        "dyn": 1*10**-5, # dyne
        "kp": 9.80665, # kilopond
        "lbf": 4.44822, # pound-force
        "pdl": 0.138255, # poundal


        }
    
    return Value * force[From] / force[To]
    