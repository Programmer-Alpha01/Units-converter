def temperature(From,To,value):

    # In case of same 
    if From == To:return value
    
    # Convert value to K
    if From =="c"   :   value=value+273.15
    elif From =="f" :   value=(value+459.67)*(5/9)
    elif From =="r" :   value=value*(5/9)
    elif From =="de":   value=373.15-(value*(2/3))
    elif From =="n" :   value=273.15+(value*(100/33))
    elif From =="re":   value=(value*(5/4))+273.15
    elif From =="ro":   value=(value-7.5)*(40/21)+273.15
    elif From =="planck":   value=value*(1.41678416*(10**32))

    # Convert value(K) to destination
    if To =="c"   :return value-273.15
    elif To =="f" :return (value*(9/5))-459.67
    elif To =="r" :return (value*(9/5))
    elif To =="de":return (373.15-value)*(3/2)
    elif To =="n" :return (value-273.15)*(33/100)
    elif To =="re":return (value-273.15)*(4/5)
    elif To =="ro":return ((value-273.15)*(21/40))+7.5
    elif To =="planck":return value/(1.41678416*(10**32))
    elif To =="k":return value
