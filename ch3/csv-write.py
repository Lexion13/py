import csv, codecs

with codecs.open("test.csv", "w", "shift_jis") as fp:
	writer = csv.writer(fp, delimiter=",", quotechar='"')
	writer.writerow(["ID", "item_name", "price"])
	writer.writerow(["1000", "fuck", "120"])
	writer.writerow(["1000", "fuck", "120"])
	writer.writerow(["1000", "fuck", "120"])
	writer.writerow(["1000", "fuck", "120"])
	writer.writerow(["1000", "fuck", "120"])
