class GameBoard:
    directions = {
        'up': (-1,0),
        'down': (1,0),
        'left': (0,-1),
        'right': (0,1)
    }

    def __init__(self, board, start_pos):
        self._board = board
        self._start_pos = start_pos
    
    def get_board(self):
        return self._board
    
    def get_start_pos(self):
        return self._start_pos

#looks for the start position while generating the 2d array
def init_2d_board(file_name):
    board = []
    guard_position = None

    with open(file_name, 'r') as file:
        for row_number, line in enumerate(file):
            stripe = line.strip()
            board.append(list(stripe))

            if '^' in stripe:
                col_index = stripe.index('^')
                guard_position = (row_number, col_index)

    return GameBoard(board, guard_position)


def unblock_position(direction):
    if direction == 'up':
        return 'right'
    if direction == 'right':
        return 'down'
    if direction == 'down':
        return 'left'
    if direction == 'left':
        return 'up'

# rule1: flip any "." to "X", if "." count++
# rule2: return count when index out of bounds
# rule3: guard has 4 directions, and will go cordinate 90degree per # reached
#   up-> right  right->down,  down >left,  left->up
def start_game(game):
    end_score = 1
    current_row, current_col = game.get_start_pos()
    direction = 'up'
    board = game.get_board()

    #capture guard movements
    while 0 <= current_row <len(board) and 0 <= current_col < len(board[0]):
        row_dir, col_dir = game.directions[direction] #guard's direction, updates per loop
        #move guard on turn as he starts off with 1 score
        next_row = current_row + row_dir # guard row position
        next_col = current_col + col_dir # guard col position

        #check if the move is legal (within bounds + not blocked)
        if 0 <= next_row < len(board) and 0 <= next_col <len(board[0]):
            if board[next_row][next_col] != '#':
                #legal move, update position
                current_row, current_col = next_row, next_col
                if board[next_row][next_col] == '.':
                    #new tile 
                    end_score += 1
                    board[next_row][next_col] = 'X'
            else:
                #blocked by object, change direction
                direction = unblock_position(direction)
        else:
            #out of bounds
            return end_score
    return end_score

if __name__ == "__main__":
    game = init_2d_board("input")
    print(start_game(game))
