def frequencies(L):
    a=list(set(L))
    b={i:L.count(i) for i in L}
    return b
