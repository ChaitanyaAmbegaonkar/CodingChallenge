source = "Hello World"
dest = "llldk"

dict = {}

for i in source:
    try:
        dict[i] = dict[i]+1
    except:
        dict[i] = 1

total = 0
for d in dest:
    try:
        total += dict[d]
        dict[d] = 0
    except:
        continue

print(total)