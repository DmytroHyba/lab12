import re

with open('access_log_Jul95.txt', 'r') as file:
    counter = 0
    for line in file:
        pattern = r"17/May/2015:(0[1-9]:[0-5][0-9|1[0-9]:[0-5][0-9]|20:[0-5][0-9]|21:00).+GET.+presentations"
        if re.search(pattern, line):
            counter += 1
print("Number of requests : " + str(counter))