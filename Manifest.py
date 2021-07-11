import csv
from HashTable import HashTable

truck1 = []
truck1_list = ["1", "13", "14", "15", "16", '19', "20", "29", "30", "31", "34", "37", "40"]
truck2 = []
truck2_list = ["2", "3", "8", "10", "12", "18", "21", "23", '27', '36', '38']
truck3 = []
truck3_list = ["4", "5", "6", "7", "9", '11', '17', '22', '24', "25", '26', '28', '32', '33', '35', '39']
package_hash = HashTable()
keys = []

'''
This reads the package data from the Packages csv and adds them to a hash map for retrieval later. Each packages is 
loaded on to a truck based on the lists above. Each package starts with the status "At hub".
Runs in O(n)
'''
with open('Data/Packages.csv', 'r') as csvfile:
    package_data = csv.reader(csvfile, delimiter=',')

    for row in package_data:

        package_ID = row[0]
        street = row[1]
        city = row[2]
        state = row[3]
        zip_code = row[4]
        requirements = row[5]
        weight = row[6]
        notes = row[7]
        start_time = ''
        location = ''
        status = 'At hub'
        values = [package_ID, location, street, city, state, zip_code, requirements, weight, notes, start_time, status]
        key = package_ID
        package_hash.insert(key, values)
        keys.append(key)

        if row[0] in truck1_list:
            truck1.append(values)
        if row[0] in truck2_list:
            truck2.append(values)
        if row[0] in truck3_list:
            truck3.append(values)


    def truck1_loaded():
        return truck1

    def truck2_loaded():
        return truck2

    def truck3_loaded():
        return truck3

    def get_hash():
        return package_hash

#print(truck1)
#print(truck2)
#print(truck3)
#
#print(len(truck1))
#print(len(truck2))
#print(len(truck3))
