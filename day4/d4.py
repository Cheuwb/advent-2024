def read_file_to_2d_array(file_path):
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file]


def is_match_xmas(grid, word, start_row, start_col, direction, rows, cols):
    word_len = len(word)
    row_dir, col_dir = direction

    for i in range(word_len):
        row = start_row + i * row_dir
        col = start_col + i * col_dir

        if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != word[i]:
            return False

    return True


def find_xmas(grid, word="XMAS"):
    rows = len(grid)
    cols = len(grid[0])
    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1),   # Right
        (-1, -1), # Top-left diagonal
        (-1, 1),  # Top-right diagonal
        (1, -1),  # Bottom-left diagonal
        (1, 1),   # Bottom-right diagonal
    ]

    count = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == word[0]:  #XMAS_SCAN on any "X" character
                for direction in directions:
                    if is_match_xmas(grid, word, row, col, direction, rows, cols):
                        count += 1

    return count

if __name__ == "__main__":
    file_path = "input"
    grid = read_file_to_2d_array(file_path)
    count = find_xmas(grid)
    print(count)