import Manifest
import DistanceService
from datetime import date, datetime, time, timedelta

start = datetime.combine(date.today(), time(8, 0,0))
#+ timedelta(minutes=10)
print (start.time())
#13:10:00

#Speed is 18 mph when traveling.
speed = 18
startTime = time(8,0,0)

truck1 = Manifest.truck1_loaded()
truck2 = Manifest.truck2_loaded()
truck3 = Manifest.truck3_loaded()

truck1Route = []
i = 0
miles = 0.0
totalTime = 0.0
visitedList = []

for pac in truck1:
    x = i + 1
    tempList = []
    while x < len(truck1):
        tempList.append(truck1[x])
        x += 1
    #print(tempList)
    if i < len(truck1)-1:
        if i == 0:
            startLoc = DistanceService.getlocationDataByName('4001 South 700 East')
            visitedList.append(startLoc[0])
            nextStop = DistanceService.getNextLocation(startLoc, tempList, visitedList)
            #DistanceService.getlocationDataByName(pac[2])
            dis = DistanceService.getDistanceBetween(startLoc[2], nextStop[2])
            #print("Distance: " + dis)
            travel = float(dis)/speed
            miles = miles + float(dis)
            totalTime = totalTime + travel
            #print("Time elapsed: " + str(travel*60))
        else:
            startLoc = DistanceService.getlocationDataByName(pac[2])
            visitedList.append(startLoc[0])
            nextStop = DistanceService.getNextLocation(startLoc, tempList, visitedList)
            #DistanceService.getlocationDataByName(truck1[i+1][2])
            dis = DistanceService.getDistanceBetween(startLoc[2], nextStop[2])
            miles = miles + float(dis)
            travel = float(dis) / speed

            totalTime = totalTime + travel
            #print("Time elapsed: " + str(travel * 60))
            #print("Distance: " + str(dis))
            #print("Location: " + startLoc[2])

        #print("Current Miles: " + str(miles))
        #print()
    else:
        print("All packages Delivered")
        print("Miles: " + str(miles))
        result = '{0:02.0f}:{1:02.0f}'.format(*divmod(totalTime * 60, 60))
        print(result)
    i += 1


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
    print(tempList)
    if j < len(truck2)-1:
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
        else:
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

        #print("Current Miles: " + str(miles2))
        #print()
    else:
        print("All packages Delivered")
        print("Miles: " + str(miles2))
        result = '{0:02.0f}:{1:02.0f}'.format(*divmod(totalTime2 * 60, 60))
        print(result)
    j += 1

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

    if k < len(truck3)-1:
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
        else:
            startLoc = DistanceService.getlocationDataByName(pac[2])
            visitedList3.append(startLoc[0])
            nextStop = DistanceService.getNextLocation(startLoc, tempList, visitedList3)
            #DistanceService.getlocationDataByName(truck3[k+1][2])
            dis = DistanceService.getDistanceBetween(startLoc[2], nextStop[2])
            miles3 = miles3 + float(dis)
            travel2 = float(dis) / speed

            totalTime3 = totalTime3 + travel2
            #print("Time elapsed: " + str(travel2 * 60))
            #print("Distance: " + str(dis))
            #print("Location: " + startLoc[2])

        #print("Current Miles: " + str(miles3))
        print()
    else:
        print("All packages Delivered")
        print("Miles: " + str(miles3))
        result = '{0:02.0f}:{1:02.0f}'.format(*divmod(totalTime3 * 60, 60))
        print(result)
    k += 1

print("Total Miles: " + str(miles + miles2 + miles3))
'''
for pac in truck1:
    distance = 0
    del1 = pac[2]
    loc1 = None
    if i == 0:
        loc1 = DistanceService.getlocationDataByName('4001 South 700 East')
    else:
        loc1 = DistanceService.getlocationDataByName(pac[2])
    i += 1
    print(loc1)
'''
'''
val2 = DistanceService.getDistanceBetween('5383 South 900 East', '3148 S 1100')

val = DistanceService.getlocationDataByName('5383 South 900 East')
val3 = DistanceService.getlocationDataByName('3148 S 1100')

print(val)
print(val3)
print(val2)
'''