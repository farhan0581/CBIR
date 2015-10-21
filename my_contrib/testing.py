import csv
fil=open('test.csv','r+')
handle=csv.writer(fil)
handle.writerow(["this","is","car","honda"])
fil.close()
handle2=csv.reader(open('test.csv'))
for row in handle2:
	print row[1]
