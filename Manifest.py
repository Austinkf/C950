import csv
from HashTable import HashTable

truck1 = []
truck1_list = ["1", "13", "14", "15", "16", "20", "29", "30", "31", "34", "37", "40"]
truck2 = []
truck2_list = ["2", "3", "6", "8", "10", "12", "18", "21", "23", "25", '27", "28', '32', '36', '38']
truck3 = []
truck3_list = ["4", "5", "7", "9", '11', '17', '19', '22', '24', '26', '33', '35', '39']
package_hash = HashTable()
keys = []

# Read in package data
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

        i = 0
        j = 0
        k = 0
        x = 0

        if row[0] in truck1_list:
            truck1.append(values)
        if row[0] in truck2_list:
            truck2.append(values)
        if row[0] in truck3_list:
            truck3.append(values)
        '''
        if len(truck1) < 16:
            truck1.append(values)
        elif len(truck2) < 16:
            truck2.append(values)
        else:
            truck3.append(values)
        '''
        '''
        while i < len(keys):
            while j < len(truck1_list):
                if truck1_list[j] == keys[i]:
                    truck1.append(values)
                j += 1
            i += 1
        '''
        # while i < len(keys):
        #     while k < len(truck2_list):
        #         if truck2_list[k] == keys[i]:
        #             truck2.append(values)
        #         k += 1
        #     i += 1
        # while i < len(keys):
        #     while x < len(truck3_list):
        #         if truck3_list[x] == keys[i]:
        #             truck3.append(values)
        #         x += 1
        #     i += 1

    def truck1_loaded():
        return truck1

    def truck2_loaded():
        return truck2

    def truck3_loaded():
        return truck3

    def get_hash():
        return package_hash

print(truck1)
print(truck2)
print(truck3)
#
print(len(truck1))
print(len(truck2))
print(len(truck3))
