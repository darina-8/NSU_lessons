def number_of_unique_characters(a):
    s = {}
    for i in a:
        if i in s.keys():
            s[i] += 1
        else:
            s[i] = 1

    unique = len(s)
    return unique
