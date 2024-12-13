plants = {}
grid = []
visited = set()
directions = [
    (-1,0), (1,0), (0,-1), (0,1)
]

def create_2darray(path):
    with open(path, 'r') as file:
        for line in file:
            line = line.strip()
            grid.append(list(line))
            for plant_type in line:
                plants[plant_type] = []


def bfs(row, col, plant_type) -> set:
    rows, cols = len(grid), len(grid[0])
    start = row, col
    queue = [start]
    visited.add(start)

    plot_sub_region = []

    while queue:
        current_cell = queue.pop(0)
        plot_sub_region.append(current_cell)
        #explore
        for explore_row, explore_column in directions:
            neighbor = (current_cell[0] + explore_row, current_cell[1] + explore_column)

            if (0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and neighbor not in visited
                and grid[neighbor[0]][neighbor[1]] == plant_type):
                queue.append(neighbor)
                visited.add(neighbor)

    return plot_sub_region

def get_sub_regions():
    rows, cols = len(grid), len(grid[0])
    for row in range(rows):
        for col in range(cols):
            plant_type = grid[row][col]
            if (row, col) not in visited:
                plot_sub_region = bfs(row, col, plant_type)
                plants[plant_type].append(plot_sub_region)

def calculate_total_pricing():
    total_pricing = 0
    for plant in plants.keys():
        all_plots = plants[plant]
        for plot in all_plots:
            #calculating the price of the plot
            area = len(plot)
            # print(plant, area)
            perimeter = calculate_perimeter(plot)
            total_pricing += area * perimeter
    return total_pricing


def calculate_perimeter(plot) -> int:
    perimeter = 0
    for coordinate in plot:
        row, col = coordinate

        for explore_row, explore_col in directions:
            neighbor = (explore_row + row, explore_col + col)
            if neighbor not in plot:
                perimeter += 1

    return perimeter
    

create_2darray("input")
get_sub_regions()
print(calculate_total_pricing())