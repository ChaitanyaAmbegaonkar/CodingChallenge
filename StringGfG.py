def DictCount(s):
    dict = {}
    max = 0
    sol = ""
    for a in s:
        try:
            dict[a] += 1
            if dict[a] > max:
                sol = a
                max = dict[a]
            elif dict[a] == max and a < sol:
                sol = a
        except:
            dict[a] = 1

    print(sol)

def bitArray(s):
    count = 0
    while s > 0:
        if s%2 == 1:
            count += 1
        s = s/2
    print(count)

def binPali(a):
    i = bin(a)
    i = i[2:]
    return i == i[-1::-1]

def MostFrequent():
    from collections import Counter

    data_set = "Welcome to the world of Geeks " \
               "This portal has been created to provide well written well" \
               "thought and well explained solutions for selected questions " \
               "If you like Geeks for Geeks and would like to contribute " \
               "here is your chance You can write article and mail your article " \
               " to contribute at geeksforgeeks org See your article appearing on " \
               "the Geeks for Geeks main page and help thousands of other Geeks. " \

    split_it = data_set.split()

    Counter = Counter(split_it)

    most_occur = Counter.most_common(9)

    print(most_occur)

def division(num,divi):
    d = 0
    out = ''
    for i in num:
        d = d*10 + int(i)
        if d > divi:
            out = out+str(d/divi)
            if d/divi == 0:
                out += '0'
            d = d%divi
        elif out != '':
            out = out + '0'

    print(out)

# num = "1248163264128256512"
# input = 125
# division(num,input)

# Python program to find maximum contiguous subarray

# Function to find the maximum contiguous subarray
from sys import maxint


def maxSubArraySum(a, size):
    max_so_far = -maxint - 1
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


# Driver function to check the above function
a = [13, 12, 5, 7]
#print "Maximum contiguous sum is", maxSubArraySum(a, len(a))

# This code is contributed by _Devesh Agrawal_

from heapq import heappush, heappop, heapify

def MostFrequentHeap():

    data_set = "Welcome to the world of Geeks " \
               "This portal has been created to provide well written well" \
               "thought and well explained solutions for selected questions " \
               "If you like Geeks for Geeks and would like to contribute " \
               "here is your chance You can write article and mail your article " \
               " to contribute at geeksforgeeks org See your article appearing on " \
               "the Geeks for Geeks main page and help thousands of other Geeks. " \

    h = []
    s = data_set.split(".")
    s = s[0].split()
    dict = {}
    for a in s:
        try:
            dict[a] = dict[a] - 1
        except:
            dict[a] = -1
    for i in dict.keys():
        heappush(h,(dict[i],i))
    heapify(h)
    for i in range(3):
        tu = heappop(h)

        print (0 - tu[0] , tu[1])
        heapify(h)


MostFrequentHeap()