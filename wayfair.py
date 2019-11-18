def solution(A):
    sum = 0
    for i in A:
        sum += i
    if(sum > len(A)-sum):
        return (len(A)-sum)
    else:
        return sum
length = 0
longest = []
def dfs(visit, input, arr):
    for i, el in enumerate(input):
        if not visit[i]:
            print()

def check():
    input = ((1,6),(3,4),(2,6),(3,5),(5,6))
    visit = [False for i in range(len(input))]
    dfs(visit,input,[])

# A = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# map = {}
# for i in range(len(A)):
#     if A[i:i+10] in map.keys():
#         if map[A[i:i+10]] == 1:
#             print A[i:i+10]
#         else:
#             map[A[i:i+10]] += 1
#     else:
#         map[A[i:i+10]] = 1




check()