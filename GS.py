import heapq

def findrank(arr,rank):
    li = []
    for k in arr:
        s = 0
        for i in k:
            s += i
        li.append(s)
    heap = []
    for i,val in enumerate(li):
        heapq.heappush(heap,(val,-i))
    heapq.heapify(heap)
    print heap
    large = heapq.nlargest(rank, heap)
    print large
    return -large[rank-1][1]

def stock(dailyprice):
    start = 0
    output = []
    for itr in range(7,len(dailyprice)+1):
        output.append(str(round(float(sum(dailyprice[start:itr]))/7, 2)))
        start += 1
    return output

a = [1,1,1,1,1,1,1,7,7,7,7,7,7,7]
print stock(a)
#print findrank(a,3)

#2