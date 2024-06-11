def temperature(From,To,value):
    if To =="c": # Convert to Celsius
        if From =="f"   :return (value-32)*(5/9)
        elif From =="k" :return value-273.15
        elif From =="r" :return (value-491.67)*(5/9)
        elif From =="de":return 100-(value*(2/3))
        elif From =="n" :return value*(100/33)
        elif From =="re":return value*(5/4)
        elif From =="ro":return (value-7.5)*(40/21)

    elif To =="f": # Convert to Fahrenheit
        if From =="c"   :return (value*(9/5))+32
        elif From =="k" :return (value*(9/5))-459.67
        elif From =="r" :return value-459.67
        elif From =="de":return 212-(value*(6/5))
        elif From =="n" :return (value*(60/11))+32
        elif From =="re":return (value*(9/4))+32
        elif From =="ro":return ((value-7.5)*(24/7))+32

    elif To =="k":  # Convert to Kelvin
        if From =="c"   :return value+273.15
        elif From =="f" :return (value+459.67)*(5/9)
        elif From =="r" :return value*(5/9)
        elif From =="de":return 373.15-(value*(2/3))
        elif From =="n" :return 273.15+(value*(100/33))
        elif From =="re":return (value*(5/4))+273.15
        elif From =="ro":return (value-7.5)*(40/21)+273.15

    elif To =="r":  # Convert to Rankine	
        if From =="c"   :return (value+273.15)*(9/5)
        elif From =="f" :return value+459.67
        elif From =="k" :return value*(9/5)
        elif From =="de":return 671.67-(value*(6/5))
        elif From =="n" :return (value*(60/11))+491.67
        elif From =="re":return (value*(9/4))+491.67
        elif From =="ro":return ((value-7.5)*(24/7))+491.67

    elif To =="de": # Convert to Delisle
        if From =="c"   :return (100-value)*(3/2)
        elif From =="f" :return (212-value)*(5/6)
        elif From =="k" :return (373.15-value)*(3/2)
        elif From =="r" :return (671.67-value)*(5/6)
        elif From =="n" :return (33-value)*(50/11)
        elif From =="re":return (80-value)*(15/8)
        elif From =="ro":return (60-value)*(20/7)

    elif To =="n":  # Convert to Newton
        if From =="c"   :return value*(33/100)
        elif From =="f" :return (value-32)*(11/60)
        elif From =="k" :return (value-273.15)*(33/100)
        elif From =="r" :return (value-491.67)*(11/60)
        elif From =="de":return 33-(value*(11/50))
        elif From =="re":return value*(33/80)
        elif From =="ro":return (value-7.5)*(22/35)

    elif To =="re": # Convert to Réaumur
        if From =="c"   :return value*(4/5)
        elif From =="f" :return (value-32)*(4/9)
        elif From =="k" :return (value-273.15)*(4/5)
        elif From =="r" :return (value-491.67)*(4/9)
        elif From =="de":return 80-(value*(8/15))
        elif From =="n" :return value*(80/33)
        elif From =="ro":return (value-7.5)*(32/21)

    elif To =="ro": # Convert to Rømer
        if From =="c"   :return (value*(21/40))+7.5
        elif From =="f" :return ((value-32)*(7/24))+7.5
        elif From =="k" :return ((value-273.15)*(21/40))+7.5
        elif From =="r" :return ((value-491.67)*(7/24))+7.5
        elif From =="de":return 60-(value*(7/20))
        elif From =="n" :return (value*(35/22))+7.5
        elif From =="re":return (value*(21/32))+7.5
