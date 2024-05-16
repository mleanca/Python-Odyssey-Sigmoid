from flask import Flask, request, render_template
from grid import Grid, solve_sudoku

app = Flask(__name__)

# Routes and views
@app.route('/')
def index() :
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve() :
    puzzle = request.form['puzzle']
    grid = [[int(num) for num in row.split(',')] for row in puzzle.split(';')]
    sudokugrid = Grid(grid)
    sudokugrid.solver()
    solved_grid = str(sudokugrid)
    return solved_grid

if __name__ == '__main__' : 
    app.run(debug = True)