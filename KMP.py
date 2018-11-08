pattern = "abcaby"
text = "abxabcabcaby"

kmpstr = [0 for i in range(len(pattern))]

j = 0
i = 1
while(i < len(pattern)):
    if pattern[i] != pattern[j]:
        if j != kmpstr[j-1]:
            i -= 1
        j = kmpstr[j-1]

    else:
        kmpstr[i] = j + 1
        j += 1
    i += 1
print(kmpstr)
j = 0
i = 0
while(i < len(text)):
    if pattern[j] != text[i]:
        if j != kmpstr[j-1]:
            i -= 1
        j = kmpstr[j-1]
    else:
        j += 1
    i += 1

if j == len(pattern):
    print("True")
else:
    print("False")