def flip(grid, dir):
    tmp = eval(repr(grid))
    if dir == "H":
        grid[0][0] = tmp[1][0]
        grid[0][1] = tmp[1][1]
        grid[1][0] = tmp[0][0]
        grid[1][1] = tmp[0][1]
        
    elif dir == "V":
        grid[0][0] = tmp[0][1]
        grid[0][1] = tmp[0][0]
        grid[1][0] = tmp[1][1]
        grid[1][1] = tmp[1][0]

    return grid

def main():
    grid = [[1, 2], [3, 4]]

    commands = input()

    h_count = 0
    v_count = 0

    for ch in commands:
        if ch == "H": h_count += 1
        elif ch == "V": v_count += 1
        else: continue

    if h_count % 2 == 1: flip(grid, "H")
    if v_count % 2 == 1: flip(grid, "V")

    for row in grid:
        for col in row:
            if col == row[-1]: print(col)
            else: print(col, end=" ")

if __name__ == "__main__": main()