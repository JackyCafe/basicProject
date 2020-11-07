import csv
file= "../data/A121151.csv"
new_list = []
with open(file,newline='') as csvfile:
    rows = csv.reader(csvfile)
    # rows = csv.DictReader(csvfile)
    for r in rows:
        new_list.append( r)
    print(new_list)

with open("../data/A121152.csv", "w") as csvfile:
    # for s in new_list:
       writer = csv.writer(csvfile,delimiter = '\t' )
       for r in new_list :
            writer.writerow(r)

