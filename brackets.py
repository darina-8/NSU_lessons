def is_correct_brackets_seq(s):
    counter = 0
    for char in s:
        if char == '(':
            counter += 1
        elif char == ')':
            counter -= 1
    if counter < 0:
        return False
    return counter == 0
