def build_successors_table(tokens):
    a = {}
    n = '.'
    for i in tokens:
        if n not in a:
            a[n] = []
        a[n] += [i]
        n = i
    return a
