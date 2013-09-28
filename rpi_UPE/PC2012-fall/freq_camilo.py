#!/usr/bin/env python

import pdb

def freq(s):
    d = {}
    for i in range(len(s)-1):
        if not d.has_key(s[i:i+2]): d[s[i:i+2]] = 0
        d[s[i:i+2]] = d[s[i:i+2]] + 1

    d = sorted(d.items(), key=lambda x: x[1],reverse=1)
    nd = []
    t = [d[0]]
    ctr = 1
    for i,j in d[1:]:
        if j==t[-1][1]: t.append([i,j])
        else:
            nd.extend(sorted(t,key=lambda x: x[0]))
            t = [[i,j]]
            ctr = ctr + 1
            if ctr>4: break
    nd.extend(sorted(t,key=lambda x: x[0]))
    return nd[:3]

din = [i[:-1] for i in open('freq.in').readlines()[2::2]]

for s in din:
    for i,n in freq(s): print i,n
    print '---'

