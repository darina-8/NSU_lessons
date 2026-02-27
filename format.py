def format_number(n):
    n = round(n, 3)
    i = int(n)
    frac = n - i
    fstr = f"{frac:.3f}"[2:]
    istr = f"{i:,}".replace(',', ' ')
    res = f"{istr} .{fstr}"
    return res.center(30, '*')
