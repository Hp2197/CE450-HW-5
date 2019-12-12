def rm_first (list, elem):
    
    if list[0]==elem:
        list.pop(0)
        return list
    return rm_first
