count = 0
def find_parent(parent,x,y):
    global rank
    rootx = find(parent, x)
    rooty = find(parent, y)

    if rootx == rooty:
        return
    else:
        parent[rootx] = rooty

def find(parent,x):
    if parent[x] == -1:
        parent[x] = x
    if parent[x] != x:
        return find(parent,parent[x])
    return x


def check_set(a):
    parent = list(-1 for i in range(len(a)*len(a)))
    n = len(a)
    for j,row in enumerate(a):
        for k,cell in enumerate(row):
            if cell == 1 and j + 1 < n:
                find_parent(parent,j,k)
            if cell == 1 and j - 1 >= 0:
                find_parent(parent, j, k)
            if cell == 1 and k - 1 >= 0:
                find_parent(parent, j, k)
            if cell == 1 and k + 1 < n:
                find_parent(parent, j, k)
            if cell == 1 and j - 1 >= 0 and k - 1 >= 0:
                find_parent(parent, j, k)
            if cell == 1 and j + 1 < n and k - 1 >= 0:
                find_parent(parent, j, k)
            if cell == 1 and j + 1 < n and k - 1 < n:
                find_parent(parent, j, k)
            if cell == 1 and j - 1 >= 0 and k - 1 < n:
                find_parent(parent, j, k)
    dict = {}
    count = 0
    for i in parent:
        if i not in dict.keys() and i != -1:
            dict[i] = 1
            count += 1
    print count

            # This code is contributed by Neelam Yadav
a = ((1, 1, 1, 1, 1), (0, 1, 0, 0, 1),(1, 0, 0, 1, 1), (0, 0, 0, 0, 0), (1, 0, 1, 0, 1))
rank = list(-1 for i in range(len(a)*len(a)))
check_set(a)
