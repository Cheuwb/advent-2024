from collections import deque

plants = {}
grid = []
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


def bfs(row, col, plant_type, visited) -> list:
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
    visited = set()
    rows, cols = len(grid), len(grid[0])
    for row in range(rows):
        for col in range(cols):
            plant_type = grid[row][col]
            if (row, col) not in visited:
                plot_sub_region = bfs(row, col, plant_type, visited)
                plants[plant_type].append(plot_sub_region)

def calculate_total_pricing():
    total_pricing_p1 = 0
    total_pricing_p2 = 0
    for plant in plants.keys():
        # print(plant)
        all_plots = plants[plant]
        for plot in all_plots:
            #calculating the price of the plot
            area = len(plot)
            # print(plant, area)
            perimeter, sides = calculate_perimeter(plot)
            total_pricing_p1 += area * perimeter
            total_pricing_p2 += area * sides
    print(total_pricing_p1)
    print(total_pricing_p2)

def calculate_perimeter(plot) -> int:
    directional_edge = dict() # Track perimeter cells based on direction as key, coordinate of the perimeter as value
    plot = set(plot)
    perimeter = 0
    for coordinate in plot:
        row, col = coordinate

        for er, ec in directions:
            neighbor = (er + row, ec + col)
            if neighbor not in plot:
                perimeter += 1

                #p2 sides calculation -> tracking perimeter directions -> connected components
                if (er, ec) not in directional_edge:
                    directional_edge[(er, ec)] = set()
                directional_edge[(er, ec)].add((row, col)) #track direction of perimeter edge
    
    # Calculate # of straight sections of the perimeter fence
    sides = calc_sides(directional_edge)
    return perimeter, sides

def calc_sides(directional_edge):
    sides = 0
    # direction key, DIRECTIONAL EDGES (location)
    for k, DES in directional_edge.items():
        #For each perimeter in the travelled direction
        visited = set()
        for (PR, PC) in DES:
            if (PR, PC) in visited:
                continue
            
            sides += 1
            Q = deque([(PR, PC)])

            #Explore connectiviy of the edge
            while Q:
                pr, pc = Q.popleft()

                #incase more than 1 neighboring cell connects to this perimeter
                if (pr, pc) in visited:
                    continue

                visited.add((pr, pc))

                #Checking neighbors
                for dr, dc in directions:
                    er, ec = pr + dr, pc + dc
                    if (er, ec) in DES:
                    #Explore neighboring edge in the same direection key -> a connected perimeter to form a side
                        Q.append((er, ec))
    # print(sides)
    return sides


create_2darray("input")
get_sub_regions()
calculate_total_pricing()