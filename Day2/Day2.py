import os

# --- Day 2: Red-Nosed Reports ---

def report_inc(report):
    for level in range(len(report)-1):
        if report[level] >= report[level+1]:
            return False
    return True


def report_dec(report):
    for level in range(len(report)-1):
        if report[level] <= report[level+1]:
            return False
    return True

with open(r"C:\Users\malwi\Desktop\Codding_stuff_MW\AdventOfCode2024\AoC2024\Day2\Day2_input.txt", "r") as plik:
    data = plik.read()

# Part I

report_box = [list(map(int, line.split())) for line in data.splitlines()]
print("Number of reports on the list:", len(report_box))

# Checking the decreasing / increasing reports first
report_box_filtered = []
for report in report_box:
    if report_dec(report) or report_inc(report):
        report_box_filtered.append(report)

print("Amount of filtered lists: ", len(report_box_filtered))

safe_reports = 0
for report in report_box_filtered:
    if all(abs(report[level+1] - report[level]) in {1,2,3} for level in range(len(report)-1)):
        safe_reports += 1

print("Safe reports amount:", safe_reports)


# Part II

report_box_unsafe = [report for report in report_box if report not in report_box_filtered]
print("Amount of not safe list", len(report_box_unsafe))
# print(report_box_unsafe)

report_box_unsafe_ex = []
for report in report_box_unsafe:
    for level in range(len(report)):
        aditional_report = report[:level] + report[level+1:]
        report_box_unsafe_ex.append(aditional_report)
# print(len(report_box_unsafe_ex))

report_box_filtered_ex = []
for report in report_box_unsafe_ex:
    if report_dec(report) or report_inc(report):
        report_box_filtered_ex.append(report)
# print(len(report_box_filtered_ex))

safe_reports_mod = 0
for report in report_box_filtered_ex:
    is_safe = True
    
    for level in range(len(report)-1):
        if abs(report[level+1] - report[level]) not in {1,2,3}:
               is_safe = False
               break
               
    if is_safe:
        safe_reports_mod += 1

print("Safe reports amount (mod):", safe_reports_mod)
print("Total:", safe_reports + safe_reports_mod)