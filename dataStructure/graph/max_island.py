def number_island(grid):
    max_area = 0
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def traverse_adjacent_island(grid, row, col):
        visited = []
        visited.append((row, col))
        grid[row][col] = "0"
        area=1
        while visited:
            r_visited, col_visited = visited.pop()
            for r, c in directions:
                if (0 <= (r + r_visited) < len(grid)) and (0 <= (c + col_visited) < len(grid[0])) and grid[r + r_visited][
                    c + col_visited] == "1":
                    grid[r + r_visited][c+col_visited] = "0"
                    visited.append((r + r_visited, col_visited + c))
                    area+=1
        return area

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "1":
                max_area=max(max_area,traverse_adjacent_island(grid, row, col))
    return max_area


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

print(number_island(grid))
