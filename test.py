from mpmath import mp

def round_mpf(number, decimal_places):
    rounded_str = mp.nstr(number, decimal_places + 1)
    return mp.mpf(rounded_str)

number = mp.mpf(725800.1234555)
rounded = round_mpf(number, 0)
print(rounded)