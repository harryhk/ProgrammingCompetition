def f(n):
    if n==1:
        return 1
    if n==2:
        return 1
    return f(n-1)+f(n-2)


d=[-1]*51

def f22(n):
    if d[n]==-1:
        return f2(n)
    else:
        return d[n]

def f2(n):
    s=0
    if n==1:
        d[1]=1
        return 1
    if n==2:
        d[2]=1
        return 1

    s = f22(n-1)+f22(n-2)

    d[n]=s
    return s


print f2(30)
