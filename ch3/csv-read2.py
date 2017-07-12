import csv, codecs
filename = "list-sjis.csv"
fp = codecs.open(filename, "r", "shift_jis")

reader = csv.reader(fp, delimiter=",", quotechar='"')
for cells in reader:
	print(cells[1], cells[2])