import sys, collections
import pdb


debug=0

f = open(sys.argv[1])
N = int(f.readline())

def could_open(sk):
    tmp= []
    for i in sk:
        try:
            if sk[i] > 0:
                tmp += keystoChests[i]
        except KeyError:
            pass

    return sorted(tmp)


def still_possible(new_startkey, new_path):
    key_types = set([i for i in new_startkey if new_startkey[i]>0 ] )
    chest_left = [ i for i in chests if i not in new_path ]
    
    def openable(i):
        return chests[i].keyToOpen in key_types

    openable_chests = filter( openable, chest_left )
    
    if debug:
        pdb.set_trace()

    while openable_chests:
        for i in openable_chests:
            key_types |= set([ _ for _ in  chests[i].keys ])
            chest_left.remove(i)
        openable_chests = filter(openable, chest_left)

    if len(chest_left) ==0 :
        return True
    else:
        return False



def explore(startkey, path):
    if len(path) == nChests:
        return path

    for i in could_open(startkey):
        if i not in path:
            new_path = path[:]
            new_path.append(i)

            new_startkey = startkey.copy()
            new_startkey[chests[i].keyToOpen] -= 1
            new_startkey.update( chests[i].keys )

            if still_possible(new_startkey, new_path):

                s = explore(new_startkey, new_path)
                if s != None:
                    return s
    
    return None


def solve():
    # check global constraint
    tmp = startkeys.copy()
    for i in chests:
        tmp.update(chests[i].keys)
    for i in keystoChests:
         if len( keystoChests[i] ) > tmp[i]:
            return None

    return explore(startkeys, [])


class Chest(object):
    def __init__(self, line):
        line = map( int, line.split() ) 
        self.keyToOpen = line[0]
        self.keys = collections.Counter( line[2:] ) 

    def __repr__(self):
        return "{%s : %s}" %(repr(self.keyToOpen), repr(self.keys))

for case in range(N):
    
    nKeys, nChests = map(int , f.readline().split())

    startkeys = collections.Counter(map( int, f.readline().split() ) )
    chests = {}
    for i in range(1, nChests+1):
        chests[i] = Chest(f.readline())
        
    keystoChests={}
    for i in chests:
        try:
            keystoChests[chests[i].keyToOpen].append(i)
        except KeyError:
            keystoChests[chests[i].keyToOpen]= [i]
            
    if debug:
        if case == 8:
            pdb.set_trace()

    solution = solve()
    if solution == None:
        solution = "IMPOSSIBLE"
    else:
        solution = ' '.join(map(str, solution) )

    print "Case #%d: %s" % (case+1, solution)
