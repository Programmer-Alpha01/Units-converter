def length(From, To, Value):
    length = { 
        # Metric
        "ym": 1*10**-24, # yoctometer
        "zm": 1*10**-21, # zeptometer
        "am": 1*10**-18, # attometer
        "fm": 1*10**-15, # femtometer
        "pm": 1*10**-12, # picometer
        "nm": 1*10**-9,  # nanometer
        "um": 1*10**-6,  # micrometer
        "cmm": 1*10**-5, # centimicron
        "dmm": 1*10**-4, # decimicron
        "mm": 0.001,    # millimeter
        "cm": 0.01,     # centimeter
        "dm": 0.1,      # decimeter
        "m": 1,         # meter
        "km": 1000,     # kilometer
        "Mm": 1000000,  # megameter
        "Gm": 1000000000, # gigameter
        "Tm": 1000000000000, # terameter
        "Pm": 1000000000000000, # petameter
        "Em": 1000000000000000000, # exameter
        "Zm": 1000000000000000000000, # zettameter
        "Ym": 1000000000000000000000000, # yottameter

        # 市制 (里, 引, 丈, 尺, 寸, 分, 厘, 毫)
        "li": 500,      # 里
        "in": 100/3,    # 引
        "zhang": 10/3,  # 丈
        "chi": 1/3,     # 尺
        "cun": 1/30,    # 寸
        "fen": 1/300,   # 分
        "lii": 1/3000,  # 厘
        "hao": 1/30000, # 毫

        # Imperial
        "in": 0.0254,   # inch
        "ft": 0.3048,   # foot
        "yd": 0.9144,   # yard
        "fath": 1.8288, # fathom
        "ch": 20.1168,  # chain
        "fur": 201.168, # furlong
        "mi": 1609.344, # mile

        # Astronomy
        "au": 149597870700, # astronomical unit
        "ld": 384400000, # lunar distance
        "ls": 299792458, # light second
        "lm": 17987547480, # light minute
        "lh": 107925284800, # light hour
        "ly": 9460730472580800, # light year
        "pc": 30856775814671900, # parsec

        # Natural units
        "planck": 1.61625518*10**-35, # Planck length

        # Others
        "mil": 2.54*10**-5, # mil
        "thou": 2.54*10**-5, # thou

        "nmi": 1852,    # nautical mile

        }
    
    return Value * length[From] / length[To]
    