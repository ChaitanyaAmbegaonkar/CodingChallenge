fil = open("./FUNDA_gvkey_cik_2015.txt","r")
count = 0
for i in fil:
    i = i.split("    ")
    try:
        if i[3] == '':
            print i[0]
            count += 1
    except:
        count = count

print(count)