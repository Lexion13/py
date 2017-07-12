import openpyxl

#open excel file
filename = "population.xlsx"
book = openpyxl.load_workbook(filename)

sheet = book.worksheets[0]

data = []
for row in sheet.rows:
	data.append([
		row[0].value,
		row[2].value
	])

#waste first rows
del data[0]

#sort for population
data = sorted(data, key=lambda x:x[1])

for i, a in enumerate(data):
	if (i >= 5): break
	print(i+1, a[0], int(a[1]))
