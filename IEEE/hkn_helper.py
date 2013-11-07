#!/usr/bin/env python 



def fixPal(binaryPal, fixlen, totalBinPal):
    
    tmp = [ '0'+ i + '0'  for i in binaryPal[fixlen-1] ]

    tmp = tmp + [ '1'+ i + '1'  for i in binaryPal[fixlen-1] ]

    totalBinPal += [  int(i,2) for i in tmp  ]


    binaryPal[fixlen] = tmp


binaryPal={}

binaryPal[1]=['0','1']
binaryPal[2]=['00','11']


totalBinPal = [0, 1, 3]

for i in range(3,33):
    fixPal(binaryPal, i, totalBinPal)


print len(totalBinPal)
