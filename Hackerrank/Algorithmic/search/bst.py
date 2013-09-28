class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.p= None
        self.data = data

class BST(object):
    def __init__(self):
        self.root =None

    def insert(self, data):
        y = None
        x = self.root
        n = Node(data)
        while x:
            y = x 
            if data <= x.data:
                x= x.left
            else:
                x = x.right
        n.p = y 
        if y == None:
            self.root = n 
        elif n.data <= y.data:
            y.left = n 
        else:
            y.right = n
    
    def search(self, data): # find the node with node.data == data
        x = self.root
        while  x != None and x.data != data:
            if data <= x.data:
                x = x.left
            else:
                x= x.right
        return x
    
    def minimum(self, x) : # find miminum of substree x 
        while x.left != None:
            x = x.left 
        return x
    
    def maximum(self, x):   # find maxinum of subtree x 
        while x.right != None:
            x = x.right
        return x 

    def successor(self, x): # finid successor of x
        if x.right :
            return self.minimum(x.right)
        y = x.p
        while y != None and x == y.right:
            x = y 
            y = y.p
        return y 
    
    def predecessor(self, x): 
        if x.left:
            return self.maximum(x.left)
        y=x.p
        while y !=None and x == y.left:
            x = y 
            y= y.p
        return y 
        

    def transplant(self, u, v): # replace substree at root u with substree at root v 
        if u.p == None:
            self.root = v 
        elif u == u.p.left:
            u.p.left = v 
        else:
            u.p.right = v 
        if v != None:
            v.p = u.p

    def delete(self, n): # delete node n
        if n.left == None:
            self.transplant(n, n.right)
        elif n.right == None:
            self.transplant(n, n.left)
        else:
            y = self.minimum(n.right)
            if y.p != n :
                self.transplant(y, y.right)
                y.right = n.right
                y.right.p = y 
            self.transplant(n, y)
            y.left = n.left
            y.left.p = y
    
    def inorder(self, x):
        if x != None:
            self.inorder(x.left)
            print x.data
            self.inorder(x.right)


def my_print(m):
    if m - int(m) == 0 :
        print '%d' % m 
    else:
        print '%2.1f' % m 

N = int(raw_input())

tree = BST()
total = 0 
median=None
for i in range(N):
    tmp = raw_input()
    a, b = [ xx for xx in tmp.split() ]
    b = int(b)
    
    #pdb.set_trace()
    
    if a == 'a':
        tree.insert(b)
        total += 1
        if total == 1:
            median = tree.root
            my_print(median.data)
            continue
        if  b <= median.data and total % 2 == 0:
            median = tree.predecessor(median)
        if b > median.data and total % 2 ==1:
            median = tree.successor(median)
            
    if a == 'r':
        node = tree.search(b)
        if node == None:
            print "Wrong!"
            continue
        else:
            total -=1 
            if total == 0 :
                print "Wrong!"
                tree.delete(node)
                continue
            if b >= median.data and total % 2 ==0:
                median = tree.predecessor(median)
            if b < median.data and total %2 ==1 :
                median = tree.successor(median)
            if median==node and total % 2 ==1:
                median = tree.successor(median)

            tree.delete(node)

    
    if total % 2 ==0:
        my_print( (median.data + tree.successor(median).data)/2.0 )
    else:
        my_print(median.data)
                

