import csv

def problem2(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='\n')
        res = ""
        for row in reader:
            x = row[0]
            temp = ""
            for t in x:
                if t != " ":
                    temp += t
            res += temp
    csvfile.close()
    return res

print(problem2("testdata.txt"))