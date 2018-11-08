file_path = "./input.txt"
inputfile = open(file_path, 'r')
outputfile = open("output.txt", 'w')
dict = {}
for i in inputfile:
    i = i.split(" ")
    if i[0] not in dict.keys():
        dict[i[0]] = 1
    else:
        dict[i[0]] = dict[i[0]] + 1

for i in dict.keys():
    outputfile.write(""+i+" "+str(dict[i])+"\n")

# s = "I like cheese"
# t = "like"
#
# ss = s.split(" ")
# ts = t.split(" ")
#
# ip = 0
# jp = 0
# while ss[ip] != ts[jp]:

