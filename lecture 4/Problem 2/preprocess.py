#!/usr/bin/python3.6m

# read the data file to rawData
f = open('raw.txt', 'r')
rawData = f.read()
f.close()
# cut the data
rawData = rawData.split(' ')
# remove the last ' '
rawData.pop()

# remove the misplaced '\n'
data = [x.strip('\n') for x in rawData]
# adding the new end of line at the fourth column
# and space the other colums
LENGTH = len(data)
for i in range(LENGTH):
    if i % 4 == 3:
        data[i] += '\n'
    else:
        data[i] += ' '

# write the cleaned data to another file
f = open('data.txt', 'a')
for x in data:
    f.write(x)
f.close()
