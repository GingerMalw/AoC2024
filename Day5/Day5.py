# updates = r"C:\Users\malwi\Desktop\Codding_stuff_MW\AdventOfCode2024\AoC2024\Day5\Day5_sample_input_update.txt"
updates = r"C:\Users\malwi\Desktop\Codding_stuff_MW\AdventOfCode2024\AoC2024\Day5\Day5_input_update.txt"
# ordering = r"C:\Users\malwi\Desktop\Codding_stuff_MW\AdventOfCode2024\AoC2024\Day5\Day5_sample_input_ordering.txt"
ordering = r"C:\Users\malwi\Desktop\Codding_stuff_MW\AdventOfCode2024\AoC2024\Day5\Day5_input_ordering.txt"

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
                        # print(f"    ! KOLIZJA: {num} w seconds dla {current_num}") 
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
    print(f"Sum for middle numbers is: {sum(middle_numbers)}")

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
    
take_middle(correct_update)