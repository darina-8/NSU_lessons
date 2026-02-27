def format_number(n):
    n = round(n, 3)
    integ = int(n)
    frac = n - integ
    fracstr = f"{frac:.3f}"[2:]
    intstr = f"{integ:,}".replace(',', ' ')
    res = f"{intstr} .{fracstr}"
    return res.center(30, '*')

print(format_number(123488482390.28174))