import re

# --- Day 6: Guard Gallivant ---


def start_point(data):
    for str_line_id, line in enumerate(data):
            str_col_id = line.find('^')
            if str_col_id != -1:
                return str_line_id, str_col_id


def moving_up(lines, str_line_id, str_col_id):
    # print("\nMoving up!")
    # start_point = (str_line_id, str_col_id)
    # print(f"Current position: {start_point}")

    for line_id in range(str_line_id-1, -1, -1):
        if line_id < 0:
             break
        
        position = (line_id, str_col_id)
        # print(f"Updated position up: {position}")
        obstruction = lines[line_id][str_col_id]
        # print(f"Obstruction detected: {obstruction}")
        
        if obstruction in (".","x"):
            path_line = list(lines[line_id])
            path_line[str_col_id] = 'x'
            lines[line_id] = ''.join(path_line)

        if obstruction == '#':
            # print(lines)
            moving_right(lines, line_id+1, str_col_id)
            break


def moving_right(lines, str_line_id, str_col_id):
        # print("\nMoving right!")
        # start_point = (str_line_id, str_col_id)
        # print(f"Current position: {start_point}")
        line_info = lines[str_line_id]
        lines_list = list(line_info)
        
        for collumn in range (str_col_id+1, len(lines_list)):
            # position = (str_line_id, collumn)
            # print(f"Updated position up: {position}")
            obstruction = lines_list[collumn]
            # print(f"Obstruction detected: {obstruction}")
            
            if obstruction in (".","x"):
                lines_list[collumn] = 'x'
                lines[str_line_id] = ''.join(lines_list)
            
            if obstruction == '#':
                # print(lines)
                moving_down(lines, str_line_id, collumn-1)
                break


def moving_down(lines, str_line_id, str_col_id):
        # print("\nMoving down!")
        # start_point = (str_line_id, str_col_id)
        # print(f"Current position: {start_point}")

        for line_id in range(str_line_id+1, len(lines)):
            # position = (line_id, str_col_id)
            # print(f"Updated position up: {position}")
            obstruction = lines[line_id][str_col_id]
            # print(f"Obstruction detected: {obstruction}")

            if obstruction in (".","x"):
                path_line = list(lines[line_id])
                path_line[str_col_id] = 'x'
                lines[line_id] = ''.join(path_line)

            if obstruction == '#':
                # print(lines)
                moving_left(lines, line_id-1, str_col_id)
                break


def moving_left(lines, str_line_id, str_col_id):
        # print("\nMoving left!")
        # start_point = (str_line_id, str_col_id)
        # print(f"Current position: {start_point}")
        line_info = lines[str_line_id]
        lines_list = list(line_info)
        
        for collumn in range (str_col_id-1, -1, -1):
            # position = (str_line_id, collumn)
            # print(f"Updated position up: {position}")
            obstruction = lines_list[collumn]
            # print(f"Obstruction detected: {obstruction}")
            
            if obstruction in (".","x"):
                lines_list[collumn] = 'x'
                lines[str_line_id] = ''.join(lines_list)
            
            if obstruction == '#':
                # print(lines)
                moving_up(lines, str_line_id, collumn+1)
                break


# data_input = r"C:\Users\malwi\Desktop\Codding_stuff_MW\AdventOfCode2024\AoC2024\Day6\Day6_input_sample.txt"
data_input = r"C:\Users\malwi\Desktop\Codding_stuff_MW\AdventOfCode2024\AoC2024\Day6\Day6_input.txt"

with open(data_input, 'r', encoding="utf-8") as plik:
    lines = plik.readlines()
            
start = start_point(lines)
moving_up(lines, start[0], start[1])
# print(lines)

# How many distinct positions will the guard visit before leaving the mapped area?
distinct = sum(line.count('x') for line in lines) + 1
print(f'\nGuard visited:   {distinct}   distinct positions before leaving')