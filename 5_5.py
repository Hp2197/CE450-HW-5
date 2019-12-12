def common_keys(D0,D1):
    d = {i:D0[i] for i in D0 if i in D1}
    return d
