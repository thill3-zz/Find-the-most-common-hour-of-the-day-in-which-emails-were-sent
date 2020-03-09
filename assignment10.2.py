while True:
    try:
        fName = input('File Name: ')
        fHandle = open(fName, 'r')
        #print('Handle opened')
        break
    except:
        print('File not found.  Input a file name for a file that exists.')
        continue

counts = {}
for line in fHandle:
    if line.startswith("From ") :
        splitLine = line.split()
        timeOfDay = splitLine[5]
        timeComponents = timeOfDay.split(':')
        hour = timeComponents[0]
        counts[hour] = counts.get(hour, 0) + 1

sortedCounts = sorted(counts.items())
for k,v in sortedCounts:
    print(k,v)
