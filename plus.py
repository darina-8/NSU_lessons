def plus_one(m):
    n = len(m)
    for i in range(n - 1, -1, -1):
        if m[i] < 9:
            m[i] += 1
            return m
        else:
            m[i] = 0
    return [1] + m
