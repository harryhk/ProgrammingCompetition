import sys

def solve(line):
    solution = []
    for i in range(len(line)):
        max_val = line[i]
        for j in range(i):
            if(max_val < solution[j]+line[i] and line[i] < line[j]):
                max_val = solution[j]+line[i]

        solution.append(max_val)
        #print solution

    return max(solution)

if __name__ == "__main__":
    fin = open(sys.argv[1])
    loop = int(fin.readline())
    for loopy in range(loop):
        ignore = fin.readline()
        line = fin.readline().strip().split(' ')
        line = [int(x) for x in line]
        print solve(line)

