#Sudoku Solver code
class Grid:
    def __init__(self, grid):
        self.grid = grid

    def __str__(self):
        grid_str = ''
        for row in self.grid:
            row_str = [str(i) if i else '*' for i in row]
            grid_str += ' '.join(row_str)
            grid_str += '\n'
        return grid_str

    def find_empty_cell(self):
        for row, contents in enumerate(self.grid):
            try:
                col = contents.index(0)
                return row, col
            except ValueError:
                pass
        return None

    def valid_in_row(self, row, num):
        return num not in self.grid[row]

    def valid_in_col(self, col, num):
        return all(self.grid[row][col] != num for row in range(9))

    def valid_in_subgrid(self, row, col, num):
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.grid[row_no][col_no] == num:
                    return False
        return True

    def is_valid(self, empty, num):
        row, col = empty
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_subgrid = self.valid_in_subgrid(row, col, num)
        return all([valid_in_row, valid_in_col, valid_in_subgrid])

    def solver(self):
        if (next_empty := self.find_empty_cell()) is None:
            return True
        for guess in range(1, 10):
            if self.is_valid(next_empty, guess):
                row, col = next_empty
                self.grid[row][col] = guess
                if self.solver():
                    return True
                self.grid[row][col] = 0
        return False

def solve_sudoku(grid):
    sudokugrid = Grid(grid)
    print(f'Puzzle to solve:\n{sudokugrid}')
    if sudokugrid.solver():
        print(f'Solved puzzle:\n{sudokugrid}')
    else:
        print('The provided puzzle is unsolvable.')
    return sudokugrid

#sample puzzle
puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]

print(solve_sudoku(puzzle))