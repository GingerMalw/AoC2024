# Day 1: Historian Hysteria
import os
with open("Day1/Day1_input.txt", "r") as plik:
    data = plik.read()
    # print(data)

# first part

l_list = []
r_list = []

for line in data.splitlines():
    if line.strip():
        left, right = line.split()
        l_list.append(int(left))
        r_list.append(int(right))

l_list.sort()
r_list.sort()

id_list = sum([abs(left - right) for left, right in zip(l_list, r_list)])
print("Total distances:", id_list)

# second part
occurance = []

for number in l_list:
    occurance.append(r_list.count(number))
    
occurance_total = sum([abs(number * ocur) for number, ocur in zip(l_list, occurance)])
print("Similarity score:", occurance_total)