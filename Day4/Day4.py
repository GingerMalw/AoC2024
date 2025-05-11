# Day 4: Ceres Search

import re
path = r"C:\Users\malwi\Desktop\Codding_stuff_MW\AdventOfCode2024\AoC2024\Day4\Day4_input.txt"
with open(path, "r") as plik:
    data = plik.read()

# Part 1
# - simple word in row "XMAS" and "SAMX",
simple_xmas = r"XMAS"
simple_samx = r"SAMX"
find_simple_xmas = re.findall(simple_xmas, data)
find_simple_samx = re.findall(simple_samx, data)
all_simple = len(find_simple_samx) + len(find_simple_xmas)
# print(find_simple)
print("Amount of 'XMAS' and 'SAMX' in simple way: ", all_simple)

# - the vertical where need to count digits in row and check if the same position in next row fit the word creation (or backward word),
def load_grid(data):
    with open(data, 'r') as vert:
        return [line.strip() for line in vert if line.strip()]

def check_vert(grid, word):
    if not grid:
        return 0
    
    rows = len(grid)
    cols = min(len(row) for row in grid)
    digit = len(word)
    count = 0

    for dig in range(cols):
        vertical_str = ''.join(d[dig] for d in grid)
        for i in range(rows - digit+1):
            if vertical_str[i:i + digit] == word:
                count += 1
    return count

data_grid = load_grid(path)

vertical_samx = check_vert(data_grid, simple_samx)
vertical_xmas = check_vert(data_grid, simple_xmas)
find_vertical = vertical_samx + vertical_xmas
print("Amount of 'XMAS' and 'SAMX' found vertical: ", find_vertical)

# - the diagonal where need to count digits in row and check if position +/-1 fit the word creation (or backward word),
def check_diag(grid, word):
    if not grid:
        return 0

    rows = len(grid)
    cols = min(len(row) for row in grid)
    digit = len(word)
    count = 0

    # one diagonal dirrection
    for dig in range(rows - digit +1):
        for i in range(cols - digit +1):
            diagonal_str = ''.join(grid[dig+a][i+a] for a in range(digit))
            if diagonal_str == word:
                count += 1

    # second diagonal dirrection
    for dig in range(rows - digit +1):
        for i in range(digit -1, cols):
            diagonal_str = ''.join(grid[dig+a][i-a] for a in range(digit))
            if diagonal_str == word:
                count += 1

    return count

diagonal_samx = check_diag(data_grid, simple_samx)
diagonal_xmas = check_diag(data_grid, simple_xmas)
find_diagonal = diagonal_xmas + diagonal_samx
# print(find_diagonal)
print("Amount of 'XMAS' and 'SAMX' found diagonal: ", find_diagonal)

# the total for Part1:
total_Part1 = all_simple + find_vertical + find_diagonal
print("Total 'XMAS' appearance: ", total_Part1)

# Part 2
# wtf...