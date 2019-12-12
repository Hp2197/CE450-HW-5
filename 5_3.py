def most_frequent(lst): 
    a=list(set(lst))
    b={i:lst.count(i) for i in lst}
    m = len(a)
    n = b[a[0]]
    k=0
    for j in range(0,m):       
        if n < b[a[j]]:
            n = b[a[j]]
            k=j
    return a[k]
