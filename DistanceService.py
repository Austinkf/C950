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

'''
Reads the distance CSV into a list for further data manipulation.
'''
for row in disReader:
    #print(row)
    distanceList.append(row)
    #j += 1

'''
Creates a hash map for the distance chart. Missing values are filled based on what the index of the missing value is, 
and is retrieved from the current distanceList. The distance data, once complete, is added to a hash map using its index
as its key.
Runs in O(n^2)
'''
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
'''
Reads the location CSV into a list for further data manipulation.
'''
for row in locReader:
    #print(row)
    locationList.append(row)
    #j += 1


'''
Iterates through locationList to add the location data and its related distance data to a hash map for retrieval later.
runs in O(n)
'''
for row in locationList:
    #print(row)
    #print(distanceTable.search())
    row.append(distanceTable.search(row[0]))
    locationTable.insert(row[0], row)
    #locationNameTable.insert(row[2],row[0])

#print(distanceTable.search('5'))
#print(locationTable.search('0'))
#print(len(distanceList))

'''
Gets the distance data based on each address' distance list. The location data is retrieved from the locationTable for
each address. The second location's id is used as the index to retrieve the distance data from the first address'
distance list.
'''
def getDistanceBetween( address1, address2 ):
    loc1 = getlocationDataByName(address1)
    loc2 = getlocationDataByName(address2)

    distance = loc1[3][int(loc2[0])]
    return distance

'''
Retrieves the location data for a given address. The locationTable is searched using the given address as the key.
Runs in O(n)
'''
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

'''
DistanceService.getNextLocation uses the starting location and iterates through the remaining packages. For every cycle 
of the loop the package location is used to get the location mileage map for that package location, that location map
is used to find the distance between the starting location and that packages location. This loop runs through all 
remaining packages comparing the starting location to the package location. At the end of the loop the lowest mileage
location is chosen. This occurs every time a package is delivered.

Runs in O(n)
'''
def getNextLocation( currentAddress, remainingAddressList, visitedList ):
    val = None
    nextStop = None
    #print( "Current Address: ")
    #print(currentAddress)
    if len(remainingAddressList) != 0:
        for pac in remainingAddressList:
            if pac[10] != 'Delivered':
                #print("Val start: " + str(val))
                tempAddress = getlocationDataByName(pac[2])
                if tempAddress[0] != currentAddress[0] and tempAddress not in visitedList:
                    #print("Temp Address:")
                    #print(tempAddress)
                    dis = getDistanceBetween(currentAddress[2], tempAddress[2])
                    if val == None:
                        #print("Val is None")
                        val = tempAddress[3][int(currentAddress[0])]
                        nextStop = tempAddress
                    else:
                        if float(val) > float(dis):
                            #if tempAddress[2] != currentAddress[2]:
                                #print("Val " + str(val) + " is Greater Than " + str(dis))
                                #print("Address: " + tempAddress[2])
                            val = dis
                            nextStop = tempAddress

    return nextStop