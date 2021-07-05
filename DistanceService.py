import csv
from HashTable import HashTable
import Manifest

discsv = open("./Data/Distance.csv", "r")
disReader = csv.reader(discsv)

loccsv = open("./Data/locations.csv", "r")
locReader = csv.reader(loccsv)

locationTable = HashTable()
locationNameTable = HashTable()
distanceTable = HashTable()

distanceList = []
locationList = []

i = 0
j = 0

for row in disReader:
    #print(row)
    distanceList.append(row)
    #j += 1

#print(distanceList)
for row in distanceList:
    #print(row)
    p = 0
    tempList = []
    for dis in row:
        #print( "Distance:" + str(dis))
        val = ''
        if dis == '':
            #print(distanceList[p])
            #print( "Found missing value: " + str(distanceList[p][0]) )
            val = distanceList[p][j]
        else:
            val = dis
        tempList.append(val)
        p += 1
    #print(tempList)
    #print("Key: " + str(j))
    distanceTable.insert(str(j), tempList)
    j += 1

#print(distanceTable.search('0'))

for row in locReader:
    #print(row)
    locationList.append(row)
    #j += 1

for row in locationList:
    print(row)
    #print(distanceTable.search())
    row.append(distanceTable.search(row[0]))
    locationTable.insert(row[0], row)
    #locationNameTable.insert(row[2],row[0])

print(distanceTable.search('5'))
print(locationTable.search('0'))
print(len(distanceList))

def getDistanceBetween( address1, address2 ):
    loc1 = getlocationDataByName(address1)
    loc2 = getlocationDataByName(address2)

    distance = loc1[3][int(loc2[0])]
    return distance

def getlocationDataByName( address ):
    i = 0
    val = None
    for row in locationList:
        loc = locationTable.search(str(i))
        #print("Compared: " + loc[2])
        #print("Static:   " + address)
        if address in loc[2] or address == loc[2]:
            val = loc
            break
        i += 1
    return val

def getNextLocation( currentAddress, remainingAddressList, visitedList ):
    val = None
    nextStop = None
    print( "Current Address: ")
    print(currentAddress)
    if len(remainingAddressList) != 0:
        for pac in remainingAddressList:
            if pac[10] != 'Delivered':
                print("Val start: " + str(val))
                tempAddress = getlocationDataByName(pac[2])
                if tempAddress[0] != currentAddress[0] and tempAddress not in visitedList:
                    print("Temp Address:")
                    print(tempAddress)
                    dis = getDistanceBetween(currentAddress[2], tempAddress[2])
                    if val == None:
                        #print("Val is None")
                        val = tempAddress[3][int(currentAddress[0])]
                        nextStop = tempAddress
                    else:
                        if float(val) > float(dis):
                            if tempAddress[2] != currentAddress[2]:
                                print("Val " + str(val) + " is Greater Than " + str(dis))
                                print("Address: " + tempAddress[2])
                                val = dis
                                nextStop = tempAddress

    return nextStop








