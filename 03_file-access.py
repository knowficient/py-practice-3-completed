# Read in text file "car_specs.txt" with car names and its battery capacity separated by commas
# Separate the names and its battery capacity and
# write the car names into a text file "car_names.txt"
# and write its battery capacity into another text file "car_battery.txt"

name = []         # create empty list for car names
cap = []          # create empty list for car battery capacity
with open("car_specs.txt", mode="r") as file:
        line = file.readline()             # read the first line
        row = []                           # create empty list
        while line:                        # while line is not empty
            line = line.replace("\n","")   # remove newline symbol from string
            row = line.split(",")          # convert string into list with commas
            name.append(row[0])            # append first item into name list
            cap.append(row[1])             # append second item into capacity list
            line = file.readline()         # read the new line and get back to while-loop

with open("car_names.txt",mode="w") as file:
    for i in name:                         # for item in the name list
        file.write(i)                      # write item into text file
        file.write("\n")                   # add newline feed

with open("car_battery.txt",mode="w") as file:
    for i in cap:                          # for item in the capacity list
        file.write(i)                      # write item into text file
        file.write("\n")                   # add newline feed

