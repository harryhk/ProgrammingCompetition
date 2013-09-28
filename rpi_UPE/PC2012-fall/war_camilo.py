import numpy, pdb

din = [int(i) for i in open('war.in').readlines()]

n = din[1]
cases = [[]]
for line in din[2:]:
    if n==0:
        n = line
        cases.append([])
    else:
        cases[-1].append(line)
        n = n-1


def solve(case):
    res = numpy.ones(len(case)).astype('int')
    case = numpy.array(case).astype('int')
    order = numpy.argsort(case)
    N = len(case)
    for i in order:
        c = case[i]
        if i>0: p = case[i-1]
        else: p = 9999999
        if i<N-1: n = case[i+1]
        else: n = 9999999
        if c>n:
            if res[i]<=res[i+1]: res[i] = res[i+1] +1
        if c>p:
            if res[i]<=res[i-1]: res[i] = res[i-1] +1
    return sum(res)

for case in cases: print solve(case)

