import sys

def solve(years, time):
    diffs = [y - x for x,y in zip(years,years[1:])]
    diffs.sort()
    
    #print diffs
    val = len(years)

    for x in diffs:
        if(x <= time):
            time-=x
            val-=1
        else:
            break
    
    return val



if __name__ == '__main__':
    fin = open(sys.argv[1])
    loop = int(fin.readline())
    for loopy in range(loop):
        line = fin.readline().strip().split(' ')
        time = int(line[1])
        years = [int(x) for x in fin.readline().strip().split(' ')]
        print solve(years,time)
