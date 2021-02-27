# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '107061252.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.
target_data = data[:10]

#=======================================
#C0A880, C0F9A0, C0G640, C0R190, C0X260
# Part. 4
#=======================================
# Print result
#========================================

id = ['C0A880','C0F9A0','C0G640','C0R190','C0X260']
number = len(data)

index_n = [[] for i in range(5)]
maxi_n = []

for i in range(number):
    if data[i]['TEMP'] == -99.0 or data[i]['TEMP'] == -999.0:
        data[i]['TEMP'] = 'None'
        print("done")
    for j in range(5):
        if data[i]['station_id'] == id[j]:
            index_n[j].append(i)

for i in range(5):
    k = 0
    for j in range(24):
        p = index_n[i][j]
        if data[p]['TEMP'] != 'None':
            if data[p]['TEMP'] > data[k]['TEMP']:
                k = p
    maxi_n.append(k)

output = [[id[0],data[maxi_n[0]]['TEMP']], [id[1],data[maxi_n[1]]['TEMP']], [id[2],data[maxi_n[2]]['TEMP']], [id[3],data[maxi_n[3]]['TEMP']], [id[4],data[maxi_n[4]]['TEMP']]]
print(output)

"""
for i in range(24):
    k = index_n[0][i]
    print(data[k]['TEMP'])
"""
