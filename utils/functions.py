def dim(V):
    a = 0
    if len(V) > 0:
        for v in V:
            a = a + len(v)
        return a
    else: return 0
