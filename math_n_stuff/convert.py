def distance(a: str, b: str, num: int or float) -> int or float:
    """Converts distance between units (metric).
    The units must be input in the "a" and "b" variables, "a" is the original and "b" the unit of the return,
    the units have to be input as a string in the formation of the list below.
    Accepted units: mm,cm, dm, m, dam, hm, km"""
    conv_mm = {
        "mm": 1,
        "cm": 0.1,
        "dm": 0.01,
        "m": 0.001,
        "dam": 0.0001,
        "hm": 0.00001,
        "km": 0.000001}
    conv_cm = {
        "mm": 10,
        "cm": 1,
        "dm": 0.1,
        "m": 0.01,
        "dam": 0.001,
        "hm": 0.0001,
        "km": 0.00001}
    conv_dm = {
        "mm": 100,
        "cm": 10,
        "dm": 1,
        "m": 0.1,
        "dam": 0.01,
        "hm": 0.001,
        "km": 0.0001}
    conv_m = {
        "mm": 1000,
        "cm": 100,
        "dm": 10,
        "m": 1,
        "dam": 0.1,
        "hm": 0.01,
        "km": 0.001}
    conv_dam = {
        "mm": 10000,
        "cm": 1000,
        "dm": 100,
        "m": 10,
        "dam": 1,
        "hm": 0.1,
        "km": 0.01}
    conv_hm = {
        "mm": 100000,
        "cm": 10000,
        "dm": 1000,
        "m": 100,
        "dam": 10,
        "hm": 1,
        "km": 0.1}
    conv_km = {
        "mm": 1000000,
        "cm": 100000,
        "dm": 10000,
        "m": 1000,
        "dam": 100,
        "hm": 10,
        "km": 1}

    units = ["mm", "cm", "dm", "m", "dam", "hm", "km"]

    if a not in units or b not in units:
        raise TypeError(f"Either {a} or {b} are not identified units.")

    match a:
        case "mm":
            for i, j in conv_mm.items():
                if i == b:
                    return num * j
        case "cm":
            for i, j in conv_cm.items():
                if i == b:
                    return num * j
        case "dm":
            for i, j in conv_dm.items():
                if i == b:
                    return num * j
        case "m":
            for i, j in conv_m.items():
                if i == b:
                    return num * j
        case "dam":
            for i, j in conv_dam.items():
                if i == b:
                    return num * j
        case "hm":
            for i, j in conv_hm.items():
                if i == b:
                    return num * j
        case "km":
            for i, j in conv_km.items():
                if i == b:
                    return num * j


def weight(a: str, b: str, num: int or float) -> int or float:
    """Converts weight between units (metric).
    The units must be input in the "a" and "b" variables, "a" is the original and "b" the unit of the return,
    the units have to be input as a string in the formation of the list below.
    Accepted units: mg, g, kg, t"""
    conv_mg = {
        "mg": 1,
        "g": 0.001,
        "kg": 0.000001,
        "t": 0.000000001}
    conv_g = {
        "mg": 1000,
        "g": 1,
        "kg": 0.001,
        "t": 0.000001}
    conv_kg = {
        "mg": 1000000,
        "g": 1000,
        "kg": 1,
        "t": 0.001}
    conv_t = {
        "mg": 1000000000,
        "g": 1000000,
        "kg": 1000,
        "t": 1}

    units = ["mg", "g", "kg", "t"]

    if a not in units or b not in units:
        raise TypeError(f"Either {a} or {b} are not identified units.")

    match a:
        case "mg":
            for i, j in conv_mg.items():
                if i == b:
                    return num * j
        case "g":
            for i, j in conv_g.items():
                if i == b:
                    return num * j
        case "kg":
            for i, j in conv_kg.items():
                if i == b:
                    return num * j
        case "t":
            for i, j in conv_t.items():
                if i == b:
                    return num * j


def area(a: str, b: str, num: int or float) -> int or float:
    """Converts area between units (metric).
    The units must be input in the "a" and "b" variables, "a" is the original and "b" the unit of the return,
    the units have to be input as a string in the formation of the list below.
    Accepted units: mm2, cm2, dm2, m2, dam2, hm2, ha, ac, km2"""
    conv_mm2 = {
        "mm²": 1,
        "cm²": 0.01,
        "dm²": 0.0001,
        "m²": 1e-6,
        "dam²": 1e-10,
        "hm²": 1e-12,
        "ha": 1e-8,
        "ac": 2.47105e-9,
        "km²": 1e-12}
    conv_cm2 = {
        "mm²": 100,
        "cm²": 1,
        "dm²": 0.01,
        "m²": 1e-4,
        "dam²": 1e-8,
        "hm²": 1e-10,
        "ha": 1e-6,
        "ac": 2.47105e-7,
        "km²": 1e-10
    }
    conv_dm2 = {
        "mm²": 10000,
        "cm²": 100,
        "dm²": 1,
        "m²": 0.01,
        "dam²": 1e-6,
        "hm²": 1e-8,
        "ha": 1e-4,
        "ac": 2.47105e-5,
        "km²": 1e-8
    }
    conv_m2 = {
        "mm²": 1e6,
        "cm²": 10000,
        "dm²": 100,
        "m²": 1,
        "dam²": 0.01,
        "hm²": 0.0001,
        "ha": 1e-4,
        "ac": 2.47105e-4,
        "km²": 1e-6
    }
    conv_dam2 = {
        "mm²": 1e8,
        "cm²": 1e6,
        "dm²": 10000,
        "m²": 100,
        "dam²": 1,
        "hm²": 0.0001,
        "ha": 0.01,
        "ac": 0.00247105,
        "km²": 1e-6
    }
    conv_hm2 = {
        "mm²": 1e10,
        "cm²": 1e8,
        "dm²": 1e6,
        "m²": 1e4,
        "dam²": 100,
        "hm²": 1,
        "ha": 1,
        "ac": 2.47105,
        "km²": 0.01
    }
    conv_ha = {
        "mm²": 1e8,
        "cm²": 1e6,
        "dm²": 10000,
        "m²": 10000,
        "dam²": 0.01,
        "hm²": 1,
        "ha": 1,
        "ac": 2.47105,
        "km²": 1e-2
    }
    conv_ac = {
        "mm²": 4.04686e7,
        "cm²": 404686,
        "dm²": 4046.86,
        "m²": 4046.86,
        "dam²": 0.00404686,
        "hm²": 0.000404686,
        "ha": 0.404686,
        "ac": 1,
        "km²": 4.04686e-4
    }
    conv_km2 = {
        "mm²": 1e12,
        "cm²": 1e10,
        "dm²": 1e8,
        "m²": 1e6,
        "dam²": 1e-4,
        "hm²": 0.01,
        "ha": 100,
        "ac": 247.105,
        "km²": 1
    }

    units = ["mm2", "cm2", "dm2", "m2", "dam2", "hm2", "ha", "ac", "km2"]

    if a not in units or b not in units:
        raise TypeError(f"Either {a} or {b} are not identified units.")

    match a:
        case "mm2":
            for i, j in conv_mm2.items():
                if i == b:
                    return num * j
        case "cm2":
            for i, j in conv_cm2.items():
                if i == b:
                    return num * j
        case "dm2":
            for i, j in conv_dm2.items():
                if i == b:
                    return num * j
        case "m2":
            for i, j in conv_m2.items():
                if i == b:
                    return num * j
        case "dam2":
            for i, j in conv_dam2.items():
                if i == b:
                    return num * j
        case "hm2":
            for i, j in conv_hm2.items():
                if i == b:
                    return num * j
        case "ha":
            for i, j in conv_ha.items():
                if i == b:
                    return num * j
        case "ac":
            for i, j in conv_ac.items():
                if i == b:
                    return num * j
        case "km2":
            for i, j in conv_km2.items():
                if i == b:
                    return num * j


def volume(a: str, b: str, num: int or float) -> int or float:
    """Converts volume between units (metric).
    The units must be input in the "a" and "b" variables, "a" is the original and "b" the unit of the return,
    the units have to be input as a string in the formation of the list below.
    Accepted units: mm3, cm3, dm3, m3, dam3, hm3, km3"""
    conv_mm3 = {
        "mm³": 1,
        "cm³": 0.001,
        "dm³": 1e-6,
        "m³": 1e-9,
        "dam³": 1e-12,
        "hm³": 1e-15,
        "km³": 1e-18
    }
    conv_cm3 = {
        "mm³": 1000,
        "cm³": 1,
        "dm³": 1e-3,
        "m³": 1e-6,
        "dam³": 1e-9,
        "hm³": 1e-12,
        "km³": 1e-15
    }
    conv_dm3 = {
        "mm³": 1e6,
        "cm³": 1000,
        "dm³": 1,
        "m³": 1e-3,
        "dam³": 1e-6,
        "hm³": 1e-9,
        "km³": 1e-12
    }
    conv_m3 = {
        "mm³": 1e9,
        "cm³": 1e6,
        "dm³": 1000,
        "m³": 1,
        "dam³": 1e-3,
        "hm³": 1e-6,
        "km³": 1e-9
    }
    conv_dam3 = {
        "mm³": 1e12,
        "cm³": 1e9,
        "dm³": 1e6,
        "m³": 1e3,
        "dam³": 1,
        "hm³": 1e-3,
        "km³": 1e-6
    }
    conv_hm3 = {
        "mm³": 1e15,
        "cm³": 1e12,
        "dm³": 1e9,
        "m³": 1e6,
        "dam³": 1e3,
        "hm³": 1,
        "km³": 1e-3
    }
    conv_km3 = {
        "mm³": 1e18,
        "cm³": 1e15,
        "dm³": 1e12,
        "m³": 1e9,
        "dam³": 1e6,
        "hm³": 1e3,
        "km³": 1
    }

    units = ["mm3", "cm3", "dm3", "m3", "dam3", "hm3", "km3"]

    if a not in units or b not in units:
        raise TypeError(f"Either {a} or {b} are not identified units.")

    match a:
        case "mm3":
            for i, j in conv_mm3.items():
                if i == b:
                    return num * j
        case "cm3":
            for i, j in conv_cm3.items():
                if i == b:
                    return num * j
        case "dm3":
            for i, j in conv_dm3.items():
                if i == b:
                    return num * j
        case "m3":
            for i, j in conv_m3.items():
                if i == b:
                    return num * j
        case "dam3":
            for i, j in conv_dam3.items():
                if i == b:
                    return num * j
        case "hm3":
            for i, j in conv_hm3.items():
                if i == b:
                    return num * j
        case "km3":
            for i, j in conv_km3.items():
                if i == b:
                    return num * j


def speed(a: str, b: str, num: int or float) -> int or float:
    """Converts speed between units (metric).
    The units must be input in the "a" and "b" variables, "a" is the original and "b" the unit of the return,
    the units have to be input as a string in the formation of the list below.
    Accepted units: mm/s, cm/s, dm/s, m/s, dam/s, hm/s, km/h"""
    conv_mm_s = {
        "mm/s": 1,
        "cm/s": 0.1,
        "dm/s": 0.01,
        "m/s": 0.001,
        "dam/s": 0.0001,
        "hm/s": 0.00001,
        "km/h": 0.0036
    }
    conv_cm_s = {
        "mm/s": 10,
        "cm/s": 1,
        "dm/s": 0.1,
        "m/s": 0.01,
        "dam/s": 0.001,
        "hm/s": 0.0001,
        "km/h": 0.036
    }
    conv_dm_s = {
        "mm/s": 100,
        "cm/s": 10,
        "dm/s": 1,
        "m/s": 0.1,
        "dam/s": 0.01,
        "hm/s": 0.001,
        "km/h": 0.36
    }
    conv_m_s = {
        "mm/s": 1000,
        "cm/s": 100,
        "dm/s": 10,
        "m/s": 1,
        "dam/s": 0.1,
        "hm/s": 0.01,
        "km/h": 3.6
    }
    conv_dam_s = {
        "mm/s": 10000,
        "cm/s": 1000,
        "dm/s": 100,
        "m/s": 10,
        "dam/s": 1,
        "hm/s": 0.1,
        "km/h": 36
    }
    conv_hm_s = {
        "mm/s": 100000,
        "cm/s": 10000,
        "dm/s": 1000,
        "m/s": 100,
        "dam/s": 10,
        "hm/s": 1,
        "km/h": 360
    }
    conv_km_h = {
        "mm/s": 277777.78,
        "cm/s": 27777.78,
        "dm/s": 2777.78,
        "m/s": 277.778,
        "dam/s": 27.7778,
        "hm/s": 2.77778,
        "km/h": 1
    }

    units = ["mm/s", "cm/s", "dm/s", "m/s", "dam/s", "hm/s", "km/h"]

    if a not in units or b not in units:
        raise TypeError(f"Either {a} or {b} are not identified units.")

    match a:
        case "mm/s":
            for i, j in conv_mm_s.items():
                if i == b:
                    return num * j
        case "cm/s":
            for i, j in conv_cm_s.items():
                if i == b:
                    return num * j
        case "dm/s":
            for i, j in conv_dm_s.items():
                if i == b:
                    return num * j
        case "m/s":
            for i, j in conv_m_s.items():
                if i == b:
                    return num * j
        case "dam/s":
            for i, j in conv_dam_s.items():
                if i == b:
                    return num * j
        case "hm/s":
            for i, j in conv_hm_s.items():
                if i == b:
                    return num * j
        case "km/h":
            for i, j in conv_km_h.items():
                if i == b:
                    return num * j


def time(a: str, b: str, num: int or float) -> int or float:
    """Converts time between units (metric).
    The units must be input in the "a" and "b" variables, "a" is the original and "b" the unit of the return,
    the units have to be input as a string in the formation of the list below.
    Accepted units: ms, s, min, h, d, wk, mo, yr"""
    conv_ms = {
        "ms": 1,
        "s": 0.001,
        "min": 1.66667e-5,
        "h": 2.77778e-7,
        "d": 1.15741e-8,
        "wk": 1.65344e-9,
        "mo": 5.68812e-11,
        "yr": 1.90258e-12
    }
    conv_s = {
        "ms": 1000,
        "s": 1,
        "min": 0.0166667,
        "h": 0.000277778,
        "d": 1.15741e-5,
        "wk": 1.65344e-6,
        "mo": 5.68812e-8,
        "yr": 1.90258e-9
    }
    conv_min = {
        "ms": 60000,
        "s": 60,
        "min": 1,
        "h": 0.0166667,
        "d": 0.000694444,
        "wk": 9.92063e-5,
        "mo": 3.125e-6,
        "yr": 1.04167e-7
    }
    conv_h = {
        "ms": 3.6e6,
        "s": 3600,
        "min": 60,
        "h": 1,
        "d": 0.0416667,
        "wk": 0.00595238,
        "mo": 0.000114155,
        "yr": 3.1688e-6
    }
    conv_d = {
        "ms": 8.64e7,
        "s": 86400,
        "min": 1440,
        "h": 24,
        "d": 1,
        "wk": 0.142857,
        "mo": 0.0328767,
        "yr": 0.00273973
    }
    conv_wk = {
        "ms": 6.048e8,
        "s": 604800,
        "min": 10080,
        "h": 168,
        "d": 7,
        "wk": 1,
        "mo": 0.230137,
        "yr": 0.0191781
    }
    conv_mo = {
        "ms": 2.628e9,
        "s": 2.628e6,
        "min": 43800,
        "h": 730,
        "d": 30.44,
        "wk": 4.34524,
        "mo": 1,
        "yr": 0.0833333
    }
    conv_yr = {
        "ms": 3.154e10,
        "s": 3.154e7,
        "min": 525600,
        "h": 8760,
        "d": 365.25,
        "wk": 52.1775,
        "mo": 12,
        "yr": 1
    }

    units = ["ms", "s", "min", "h", "d", "wk", "mo", "yr"]

    if a not in units or b not in units:
        raise TypeError(f"Either {a} or {b} are not identified units.")

    match a:
        case "ms":
            for i, j in conv_ms.items():
                if i == b:
                    return num * j
        case "s":
            for i, j in conv_s.items():
                if i == b:
                    return num * j
        case "min":
            for i, j in conv_min.items():
                if i == b:
                    return num * j
        case "h":
            for i, j in conv_h.items():
                if i == b:
                    return num * j
        case "d":
            for i, j in conv_d.items():
                if i == b:
                    return num * j
        case "wk":
            for i, j in conv_wk.items():
                if i == b:
                    return num * j
        case "mo":
            for i, j in conv_mo.items():
                if i == b:
                    return num * j

        case "yr":
            for i, j in conv_yr.items():
                if i == b:
                    return num * j
