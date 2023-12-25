def number_island(grid):
    island_number = 0
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def traverse_adjacent_island(grid, row, col):
        stack = []
        grid[row][col]="0"
        stack.append((row,col))

        while stack:
            r,c=stack.pop(0)
            for new_r, new_c in directions:
                if (0<=r+new_r<len(grid)) and (0<=c+new_c<len(grid[0])) and grid[r+new_r][c+new_c]=="1":
                    grid[r+new_r][c+new_c]="0"
                    stack.append(((r+new_r),(c+new_c)))




    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "1":
                island_number += 1

                traverse_adjacent_island(grid, row, col)
    return island_number


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(number_island(grid))

