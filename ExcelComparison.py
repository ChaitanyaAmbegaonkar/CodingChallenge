import csv

def read_sbir_file(file_path):
    pi_and_fn_list = list()
    with open(file_path, 'rU') as csvfile:
        reader = csv.reader(csvfile, dialect='excel', delimiter=';')
        next(reader)
        for row in reader:
            pi_and_fn_list.append(row[0])

    return pi_and_fn_list

original = read_sbir_file("/Users/user/Documents/patent_code/data/temp_res_original.csv")
newFile = read_sbir_file("/Users/user/Documents/patent_code/data/temp_res.csv")
dict = {}
for i in original:
    if i not in dict.keys():
        dict[i] = i

for i in newFile:
    if i not in dict.keys():
        print i