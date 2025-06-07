import re

# --- Day 3: Mull It Over ---

with open("Day3/Day3_input.txt", "r") as plik:
    data = plik.read()

# Part 1

# regex patter first:
pattern = r"mul\(\d{1,3},\d{1,3}\)"
numbers = r"\d+,\d+"
muls = re.findall(pattern, data)
digits = [re.findall(numbers, i) for i in muls]
# print(muls)
# print(digits)

digits_corrected = []
for mul in digits:
    for nr in mul:
        a = nr.split(",")
        number = [int(b) for b in a]
        digits_corrected.append(number)
# print(digits_corrected)

sum = 0
for mul in digits_corrected:
    sum += mul[0]*mul[1]

print("Total multiplication result: ", sum)

# Part 2
pattern2 = r"mul\(\d{1,3},\d{1,3}\)|don\'t\(\)|do\(\)"

muls_block = re.findall(pattern2, data)
# print(muls_block)

block = re.compile("don\'t\(\)")
approval = re.compile("don\(\)")
mul_new = re.compile("mul\(\d{1,3},\d{1,3}\)")
flag = True
digits_withdis = []
for element in muls_block:
    if block.match(element):
        flag = False
    elif approval.match(element):
        flag = True
    if flag and mul_new.match(element):
        digits_withdis.append(element)

digits_withdis2 = []
for i in digits_withdis:
    digits_withdis2.append(re.findall(numbers, i))

digits_withdis_corrected = []
for mul2 in digits_withdis2:
    for nr in mul2:
        a = nr.split(",")
        number = [int(b) for b in a]
        digits_withdis_corrected.append(number)

sum2 = 0
for mul2 in digits_withdis_corrected:
    sum2 += mul2[0]*mul2[1]

print("Total multiplication result (corrected): ", sum2)