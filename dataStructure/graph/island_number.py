def number_island(grid):
    island_number = 0

    def traverse_adjacent_island(grid, row, col):
        if (0 <= row < len(grid)) and (0 <= col < len(grid[0])) and grid[row][col] == "1":
            grid[row][col] = "0"
            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                traverse_adjacent_island(grid, row+i, col+j)

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "1":
                island_number += 1

                traverse_adjacent_island(grid, row, col)
    return island_number


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(number_island(grid))
