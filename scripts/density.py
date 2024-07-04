
from mass import mass
from volume import volume

def density(From, To, Value):

    # Density units are mass/volume
    # use mass function to convert mass units
    # use volume function to convert volume units

    # get mass and volume units from "Form" and "To"
    massFrom, volumeFrom = From.split("/")
    massTo, volumeTo = To.split("/")

    m = mass(massFrom, massTo, 1)
    v = volume(volumeFrom, volumeTo, 1)

    return Value * m / v
    

    
    
    
    