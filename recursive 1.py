def add(k):
    if k>0:
        res=k+add(k-1)
        print(res)
    else:
        res=0
    return res
add(5)