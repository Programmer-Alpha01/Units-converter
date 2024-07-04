# Unit-Converter

A simple unit converter package for Python. It was designed for scientific research and engineering calculation.

## To build the package

```bash
python setup.py sdist
```

or

```bash
python setup.py bdist_wheel
```

## To install the package

```bash
pip install dist/unit_converter-X.X.X.tar.gz
```

or

```bash
pip install dist/unit_converter-X.X.X-py3-none-any.whl
```


### Supported Units and Categories
| Category    | Units                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Angles of Circles | radians (rad), degrees (deg)                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Temperature       | Celsius (C), Fahrenheit (F), Kelvins (K)                                                                                                                                                                                                                                                                                                                                                                                                 |
| Distance          | Metric distances: attometer (am), femtometer (fm), picometer (pm), nanometer (nm), micrometer (μm), milimeter (mm), centimeter (cm), decimeter (dm), meter (m), decameter (dam), hectometer (hm), kilometer (km), megameter (Mm), gigameter (Gm), terameter (Tm), petameter (Pm), exameter (Em) Imperial distances: thou (th), inch (in), link (li), foot (ft), yard (yd), rod (rod), chain (ch), furlong (fur), mile (mi), league (lea) |
| Volume            | Metric volumes: attoliter (al) to exaliter (El) Imperial volumes: fluid ounce (floz), gill (gi), pint (pt), quart (qt), gallon (gal)                                                                                                                                                                                                                                                                                                     |
| Mass and Weight   | Metric mass: attoggram (ag) to Exagram (Eg) Imperial mass: grain (gr), drachm (dr), ounce (oz), pound (lb), stone (st), quarter (qtr or qr), hundredweight (cwt), ton (t)                                                                                                                                                                                                                                                                |
| Time              | yocotosecond (ys), zeptosecond (zs), attosecond (as), femtosecond (fs), picosecond (ps), nanosecond (ns), microsecond (µs), milisecond (ms), cs, ds, second (s), minute (min), kilosecond (ks), hour (hr), day (day), week (wk), megasecond (Ms), month (mo), year (yr), gigasecond (Gs), terasecond (Ts), petasecond (Ps), exasecond (Es), Zs, Ys                                                                                       |
| Pressure          | pascal (pa), torr (torr), pounds per square inch (psi), bar (bar), technical atmosphere (at), atmosphere (atm)                                                                                                                                                                                                                                                                                                                           |
| Energy            | watt (w), joule (j), horsepower (hp), Calorie (cal), British thermal unit (btu)                                                                                                                                                                                                                                                                                                                                                          |
| Speed             | kilometers per hour (kph), miles per hour (mph), knots (kt)                                                                                                                                                                                                                                                                                                                                                                              |
| Force             | Newton (N), dyne (dyn), Kilogram-Force (kp), Poundal (pdl)                                                                                                                                                                                                                                                                                                                                                                               |
| Digital Storage   | bit (bit), byte (byte), kilobyte (kB), megabyte (MB), gigabyte (GB), terabyte (TB), petabyte (PB), exabyte (EB), zettabyte (ZB), yottabyte (YB)       
