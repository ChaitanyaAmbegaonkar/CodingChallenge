
def totalFruit(tree):
    """
    :type tree: List[int]
    :rtype: int
    """
    first = -1
    second = -1
    fbasket = 0
    sbasket = 0
    fc = 1
    sc = 1
    latest = False
    curmax = 0
    for n,i in enumerate(tree):
        if first == -1:
            first = i
            fbasket += 1
            latest = False
        elif second == -1 and first != i:
            second = i
            sbasket += 1
            latest = True
        else:
            if first == i:
                fbasket += 1
                latest = False
                if tree[n-1] == i:
                    fc += 1
            elif second == i:
                sbasket += 1
                latest = True
                if tree[n-1] == i:
                    sc += 1
            else:
                if curmax < (fbasket + sbasket):
                    curmax = fbasket + sbasket
                if latest:
                    fbasket = 1
                    first = i
                    sbasket = sc
                    sc = 1
                    latest = False
                else:
                    sbasket = 1
                    second = i
                    fbasket = fc
                    fc = 1
                    latest = True
    if curmax < (fbasket + sbasket):
        curmax = fbasket + sbasket

    print curmax

tr = [1,2,3,2,2]

totalFruit(tr)