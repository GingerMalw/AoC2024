# Day 5: Print Queue

# Data inputs:
# updates = r"C:\Users\malwi\Desktop\Codding_stuff_MW\AdventOfCode2024\AoC2024\Day5\Day5_sample_input_update.txt"
updates = r"C:\Users\malwi\Desktop\Codding_stuff_MW\AdventOfCode2024\AoC2024\Day5\Day5_input_update.txt"
# ordering = r"C:\Users\malwi\Desktop\Codding_stuff_MW\AdventOfCode2024\AoC2024\Day5\Day5_sample_input_ordering.txt"
ordering = r"C:\Users\malwi\Desktop\Codding_stuff_MW\AdventOfCode2024\AoC2024\Day5\Day5_input_ordering.txt"

# Part One function:
def find_correct_updates(all_updates, all_orders):
    correct_updates = []
    ab_order = {}
    for order in all_orders:
        first = order[0]
        second = order[1]
        if first not in ab_order:
            ab_order[first] = set()
        ab_order[first].add(second)
    
    for update in all_updates:
        valid = True
        # print(update)

        for idx, current_num in enumerate(update):
            if current_num in ab_order:
                previous_num = update[:idx]
                second_num = ab_order[current_num]
                # print(f"  * current_num: {current_num}, previous: {previous_num}, seconds: {second_num}")
                for num in previous_num:
                    if num in second_num:
                        # print(f" ISSUE: {num} w seconds for {current_num}") 
                        valid = False
                        break
                
                if not valid:
                    break
        if valid:
            correct_updates.append(update)
    
    return correct_updates
    # print(correct_updates)
    # print(ab_order)


def take_middle(updates_list):
    middle_numbers = []
    for line in updates_list:
        middle_number = (len(line)) // 2
        middle_numbers.append(line[middle_number])
        
    # print(f"Middle numbers are: {middle_numbers}")
    return sum(middle_numbers)

# Function upgraded for Part Two:
def page_ordering_rules(list, all_orders):
    fix_updates = []
    ab_order = {}
    for order in all_orders:
        first = order[0]
        second = order[1]
        if first not in ab_order:
            ab_order[first] = set()
        ab_order[first].add(second)
    
    for update in list:
        valid = True
        # print(f"UPDATE: {update}")

        for idx, current_num in enumerate(update):
            if current_num in ab_order:
                previous_num = update[:idx]
                second_num = ab_order[current_num]
                # print(f"  * current_num: {current_num}, previous: {previous_num}, seconds: {second_num}")
                for num in previous_num:
                    if num in second_num:
                        # print(f" ISSUE: {num} w seconds for {current_num}") 
                        update[idx] , update[idx - 1] = update[idx - 1], update[idx]
                        # print(f"NEW: {update}")
                        list.append(update)
                        valid = False
                        break

                if not valid:
                    break

        if valid:
            fix_updates.append(update)
    
    return fix_updates


# --- Part One ---

# extracting updates
with open(updates, 'r', encoding="utf-8") as plik:
    lines = plik.readlines()

all_updates = []
for line in lines:
    update = list(map(int, line.split(',')))
    all_updates.append(update)
# print(all_updates)

# extracting orders
with open(ordering, 'r', encoding="utf-8") as plik:
    orders = plik.readlines()

all_orders = []
for order in orders:
    order = list(map(int, order.split('|')))
    all_orders.append(order)
# print(all_orders)


correct_update = find_correct_updates(all_updates, all_orders)
# print(correct_update)
    
middle_part1 = take_middle(correct_update)
print(f"The mid values sum for Part One: {middle_part1}")


# --- Part Two ---

incorrect_updates = []
for update in all_updates:
    if update not in correct_update:
        incorrect_updates.append(update)
# print(incorrect_updates)

# !! Well, the permutation for this amount of data will kill the process :) !!
# for update in incorrect_updates:
#     update_perm = permutations(update)
#     for perm in update_perm:
#         incorrect_updates_fix.append(find_correct_updates(perm, all_orders))

incorrect_updates_fix = page_ordering_rules(incorrect_updates, all_orders)
# print(incorrect_updates_fix)

middle_part2 = take_middle(incorrect_updates_fix)
print(f"The mid values sum for Part Two: {middle_part2}")