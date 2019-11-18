def solution(S,E):
    chairs = 0
    checked = [True] * len(S)
    for i,st in enumerate(S):
        for j in range(len(E)):
            if i != j and (checked[i] or checked[j]) and ((st >= S[j] and st < E[j]) or (E[i] > S[j] and E[i] <= E[j])):
                checked[i] = False
                checked[j] = False
                chairs += 1
    return chairs


s = [1,2,6,5,3]
e = [5,5,7,6,8]

def solutions(S,E):
    ti = []
    for i,st in enumerate(S):
        ti.append((st,E[i]))
    ti.sort()
    chairs = 0
    checked = [True] * len(S)
    for i,ft in enumerate(ti):
        for j,st in enumerate(ti):
            if i != j and (checked[i] or checked[j]) and ((ft[0] >= st[0] and ft[0] < st[1]) or (ft[1] > st[0] and ft[1] <= st[1])):
                checked[i] = False
                checked[j] = False
                chairs += 1
    return chairs

print str(solutions(s,e))