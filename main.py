'''
Austin Franks
Student Id Number
'''
import Manifest
import DistanceService
from Manifest import package_hash
from datetime import date, datetime, time, timedelta

#startFinal is used to compare the beginning of the day with times to assume status and is not altered.
startFinal = datetime.combine(date.today(), time(8, 0,0))

#start keeps track of truck1's running time as it delivers packages. This is used for both truck1 and truck3 as they
# are the same truck just that truck3 is truck1's second trip.
start = datetime.combine(date.today(), time(8, 0,0))

#trip2Start is the start time of truck1's second trip and is calculated after truck1 finishes it's first trip and is back
# at the hub.
trip2Start = datetime.combine(date.today(), time(8, 0,0))

#start2 keeps track of truck2's delivery time.
start2 = datetime.combine(date.today(), time(8, 0,0))


#This function takes a packageId and a time as input. The packageId is used to find the package in the hash map. The
# time is used to compare against the delivery time to assume the status of the package at the given time.
def getPackageDetailsForUser( packageId, askTime ):
    msg = 'Package [' + str(packageId) + '] status is: '

    try:
        package = package_hash.search(packageId)
        status = package[1][10]
        statusList = status.split(" ")
        #print("Status List: " + str(statusList))
        timeSplit = statusList[2].split(":")
        pTime = time(hour=int(timeSplit[0]), minute=int(timeSplit[1]), second=int(timeSplit[2]))
        #print(pTime)
        #print(statusList)

        if packageId in Manifest.truck1_list or packageId in Manifest.truck2_list:
            if askTime <= startFinal.time():
                msg = msg + 'At Hub'
            elif askTime < pTime:
                msg = msg + 'En Route'
            else:
                msg = msg + ' Delivered ' + str(pTime)
            #print("In first truck")
        else:
            if askTime <= trip2Start.time():
                msg = msg + 'At Hub'
            elif askTime < pTime:
                msg = msg + 'En Route'
            else:
                msg = msg + ' Delivered ' + str(pTime)
            #print("On truck1 second trip")
    except:
        print()
    return msg

#This function displays all the packages for all trucks at a given time. O(3n)
def getAllPackageStatusForTime( askTime ):
    for pac in truck1:
        print(getPackageDetailsForUser(pac[0], askTime))
    for pac in truck2:
        print(getPackageDetailsForUser(pac[0], askTime))
    for pac in truck3:
        print(getPackageDetailsForUser(pac[0], askTime))

#This function returns a package from the hash map for a given packageId.
def getPackageDetails( packageId ):
    return package_hash.search(packageId)

#Speed is 18 mph when traveling.
speed = 18

truck1 = Manifest.truck1_loaded()
truck2 = Manifest.truck2_loaded()
truck3 = Manifest.truck3_loaded()

truck1Route = []
i = 0
miles = 0.0
totalTime = 0.0
visitedList = []

'''
This iterates through truck1's packages and delivers each one starting at the hub. When deciding on what package to 
deliver next I used the Nearest Neighbor algorithm to determine what the fastest route would be. When the truck is at
a location it uses that as its starting point and adds that to its visitedList, it adds the remaining packages
to a list and sends it to DistanceService.getNextLocation()

DistanceService.getNextLocation uses the starting location and iterates through the remaining packages. For every cycle 
of the loop the package location is used to get the location mileage map for that package location, that location map
is used to find the distance between the starting location and that packages location. This loop runs through all 
remaining packages comparing the starting location to the package location. At the end of the loop the lowest mileage
location is chosen. This occurs every time a package is delivered.

This same process is used for all trucks and trips and runs in O(n^2)
'''
for pac in truck1:

    x = i + 1
    tempList = []
    while x < len(truck1):
        tempList.append(truck1[x])
        x += 1
    #print(tempList)
    if i < len(truck1):
        if i == 0:
            #print(pac)
            startLoc = DistanceService.getlocationDataByName('4001 South 700 East')
            visitedList.append(startLoc[0])
            nextStop = DistanceService.getNextLocation(startLoc, tempList, visitedList)
            #DistanceService.getlocationDataByName(pac[2])
            dis = DistanceService.getDistanceBetween(startLoc[2], nextStop[2])
            #print("Distance: " + dis)
            travel = float(dis)/speed
            miles = miles + float(dis)
            totalTime = totalTime + travel
            start = start + timedelta(minutes=(travel*60))
            trip2Start = trip2Start + timedelta(minutes=(travel * 60))
            #print("Travel: " + str(travel*60))
            #print("Start: " + str(start))
            pac[10] = 'Delivered ' + str(start)
            #print("Time elapsed: " + str(travel*60))
        else:
            if i < len(truck1)-1:
                startLoc = DistanceService.getlocationDataByName(pac[2])
                visitedList.append(startLoc[0])
                nextStop = DistanceService.getNextLocation(startLoc, tempList, visitedList)
                #DistanceService.getlocationDataByName(truck1[i+1][2])
                dis = DistanceService.getDistanceBetween(startLoc[2], nextStop[2])
                miles = miles + float(dis)
                travel = float(dis) / speed

                totalTime = totalTime + travel
                start = start + timedelta(minutes=(travel * 60))
                trip2Start = trip2Start + timedelta(minutes=(travel * 60))
                # print("Travel: " + str(travel*60))
                # print("Start: " + str(start))
                pac[10] = 'Delivered ' + str(start)
                #print("Time elapsed: " + str(travel * 60))
                #print("Distance: " + str(dis))
                #print("Location: " + startLoc[2])
                #print("Package Id: " + str(pac[0]))
                #print("i = " + str(i))
            if i == len(truck1)-1:
                #print("Adding return time")
                startLoc = DistanceService.getlocationDataByName(pac[2])
                nextStop = DistanceService.getlocationDataByName('4001 South 700 East')
                dis = DistanceService.getDistanceBetween(startLoc[2], nextStop[2])
                dis = DistanceService.getDistanceBetween(startLoc[2], nextStop[2])
                miles = miles + float(dis)
                travel = float(dis) / speed

                totalTime = totalTime + travel
                start = start + timedelta(minutes=(travel * 60))
                trip2Start = trip2Start + timedelta(minutes=(travel * 60))
                pac[10] = 'Delivered ' + str(start)
                #print("Last Package:")
                #print(pac)


        package_hash.insert(pac[0], pac)
        #print("Current Miles: " + str(miles))
        #print()
    else:
        print("All packages Delivered")
        print("Miles: " + str(miles))
        result = '{0:02.0f}:{1:02.0f}'.format(*divmod(totalTime * 60, 60))
        print(result)
    i += 1

print("Truck 1 trip 1 start at 8:00 and finished at " + str(start.time()))
print("Truck 1 mileage was " + str(miles) + " miles")
print()

j = 0
miles2 = 0.0
totalTime2 = 0.0
visitedList2 = []

for pac in truck2:
    x = j + 1
    tempList = []
    while x < len(truck2):
        tempList.append(truck2[x])
        x += 1
    #print(tempList)
    if j < len(truck2):
        if j == 0:
            startLoc = DistanceService.getlocationDataByName('4001 South 700 East')
            visitedList2.append(startLoc[0])
            nextStop = DistanceService.getNextLocation(startLoc, tempList, visitedList2)
            #DistanceService.getlocationDataByName(pac[2])
            dis = DistanceService.getDistanceBetween(startLoc[2], nextStop[2])
            #print("Distance: " + dis)
            travel = float(dis)/speed
            miles2 = miles2 + float(dis)
            totalTime2 = totalTime2 + travel
            #print("Time elapsed: " + str(travel*60))
            start2 = start2 + timedelta(minutes=(travel * 60))
            # print("Travel: " + str(travel*60))
            # print("Start: " + str(start))
            pac[10] = 'Delivered ' + str(start2)
        else:
            if j < len(truck2)-1:
                startLoc = DistanceService.getlocationDataByName(pac[2])
                nextStop = DistanceService.getNextLocation(startLoc, tempList, visitedList)
                #DistanceService.getlocationDataByName(truck2[j+1][2])
                dis = DistanceService.getDistanceBetween(startLoc[2], nextStop[2])
                miles2 = miles2 + float(dis)
                travel2 = float(dis) / speed

                totalTime2 = totalTime2 + travel2
                #print("Time elapsed: " + str(travel2 * 60))
                #print("Distance: " + str(dis))
                #print("Location: " + startLoc[2])
                start2 = start2 + timedelta(minutes=(travel * 60))
                # print("Travel: " + str(travel*60))
                # print("Start: " + str(start))
                pac[10] = 'Delivered ' + str(start2)
                #print("i = " + str(j))
            elif j == len(truck2)-1:
                pac[10] = 'Delivered ' + str(start2)

        package_hash.insert(pac[0], pac)
        #print("Current Miles: " + str(miles2))
        #print()
    else:
        #print("All packages Delivered")
        #print("Miles: " + str(miles2))
        result = '{0:02.0f}:{1:02.0f}'.format(*divmod(totalTime2 * 60, 60))
        #print(result)
    j += 1

print("Truck 2 started at 8:00 and finished at " + str(start2.time()))
print("Truck 2 mileage was " + str(miles2) + " miles")
print()

k = 0
miles3 = 0.0
totalTime3 = 0.0
visitedList3 = []

for pac in truck3:
    x = k + 1
    tempList = []
    while x < len(truck3):
        tempList.append(truck3[x])
        x += 1

    if k < len(truck3):
        if k == 0:
            startLoc = DistanceService.getlocationDataByName('4001 South 700 East')
            nextStop = DistanceService.getNextLocation(startLoc, tempList, visitedList3)
            visitedList3.append(startLoc[0])
            #DistanceService.getlocationDataByName(pac[2])
            dis = DistanceService.getDistanceBetween(startLoc[2], nextStop[2])
            #print("Distance: " + dis)
            travel = float(dis)/speed
            miles3 = miles3 + float(dis)
            totalTime3 = totalTime3 + travel
            #print("Time elapsed: " + str(travel*60))
            start = start + timedelta(minutes=(travel * 60))
            # print("Travel: " + str(travel*60))
            # print("Start: " + str(start))
            pac[10] = 'Delivered ' + str(start)
        else:
            if k < len(truck3)-1:
                startLoc = DistanceService.getlocationDataByName(pac[2])
                visitedList3.append(startLoc[0])
                nextStop = DistanceService.getNextLocation(startLoc, tempList, visitedList3)
                #DistanceService.getlocationDataByName(truck3[k+1][2])
                dis = DistanceService.getDistanceBetween(startLoc[2], nextStop[2])
                miles3 = miles3 + float(dis)
                travel2 = float(dis) / speed

                totalTime3 = totalTime3 + travel2
                start = start + timedelta(minutes=(travel * 60))
                # print("Travel: " + str(travel*60))
                # print("Start: " + str(start))
                pac[10] = 'Delivered ' + str(start)
                #print("Time elapsed: " + str(travel2 * 60))
                #print("Distance: " + str(dis))
                #print("Location: " + startLoc[2])
            elif k == len(truck3)-1:
                pac[10] = 'Delivered ' + str(start)

        package_hash.insert(pac[0], pac)
        #print("Current Miles: " + str(miles3))
        #print()
    else:
        #print("All packages Delivered")
        #print("Miles: " + str(miles3))
        result = '{0:02.0f}:{1:02.0f}'.format(*divmod(totalTime3 * 60, 60))
        #print(result)
    k += 1

print("Truck 1 trip 2 started at " + str(trip2Start.time()) + " and finished at " + str(start.time()))
print("Truck 1 trip 2 mileage was " + str(miles3) + " miles")
print()

print("Total Miles: " + str(miles + miles2 + miles3))
print()

#print(package_hash.search('25'))

#print("Trip 2 Start Time: " + str(trip2Start))

#getAllPackageStatusForTime(time(hour=9, minute=30, second=0))


state = input("To begin, please type 'lookup' to search for a package or "
                  "type 'timestamp' to view delivery status at a give time: ")

while state != 'quit':
    if state == 'timestamp':
        askTimeString = ''
        try:
            askTimeString = input("Enter a time in the format of HH:MM:SS ")
            askTimeArr = askTimeString.split(":")
            print(askTimeArr)
            askTime = time(hour=int(askTimeArr[0]), minute=int(askTimeArr[1]), second=int(askTimeArr[2]))
            getAllPackageStatusForTime(askTime)
        except:
            print("Incorrect format: " + str(askTimeString))
    elif state == 'lookup':
        packageId = input("Please enter the id of the package: ")
        try:
            package = getPackageDetails(str(packageId))
            if package is not None:
                print(package[1])
            else:
                print("Package not found or incorrect ID format for [" + str(packageId) + ']')
        except:
            print("Package not found or incorrect ID format for [" + str(packageId) + ']')
        exit()