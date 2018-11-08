def add_node(a,b):
    rootx = find(a)
    rooty = find(b)
    if rooty == rootx:
        return
    else:
        parent[rootx] = rooty

def find(a):
    if parent[a] == -1:
        parent[a] = a
    if parent[a] != a:
        return find(parent[a])
    return a



def query(a,b):
    count = 0
    while parent[a] != b:
        a = parent[a]
        count += 1
    print(count)

inp = 6
mat = [[0 for i in range(inp)] for j in range(inp)]
parent = [-1 for i in range(inp)]
add_node(0,3)
add_node(3,4)
add_node(4,1)
add_node(1,5)
add_node(5,2)

query(0,3)



