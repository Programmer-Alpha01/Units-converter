

from length import length

def area(From, To, Value):

    # get units from "Form" and "To"
    lengthFrom, lengthTo = From.split("^2"), To.split("^2")
    
    return Value * length(lengthFrom[0], lengthTo[0])**2
    

    
    
    