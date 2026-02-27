def two_sum(a, n):
    for i in range(len(a)):
        ost = n - a[i]
        last = a[i + 1:]
        if ost in last:
            return [i, last.index(ost) + i + 1]

def two_sum_sorted(a, t):
    l, r = 0, len(a) - 1
    while l < r:
        s = a[l] + a[r]
        if s == t:
            return [l, r]
        elif s < t:
            l += 1
        else:
            r -= 1
    return []
