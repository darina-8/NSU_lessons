def number_of_unique_characters(s):
    c = {}
    for i in s:
        if i in c.keys():
            c[i] += 1
        else:
            c[i] = 1

    unique = len(c)
    return unique