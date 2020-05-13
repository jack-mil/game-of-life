from Settings import Settings
from copy import deepcopy

# Useful constants
DEAD = 0
LIVE = 1


class Cell:
    """
    A simple representation of a cell
    May be further expanded with more features or states
    can be used with inheritance
    """

    def __init__(self, state=0):
        self.state = state


class GameOfLife:
    """
    A GameOfLife object contains the internal representation of the current state of cells
        -call the evolve() method to update the internal population to the next generation
    """

    def __init__(self, initial):
        self.height = Settings().h
        self.width = Settings().w

        # self.cells = [[Cell(LIVE) if (i, j) in initial else Cell(DEAD)
        #                for j in range(self.width)] for i in range(self.height)]

        self.cells = []
        for i in range(self.height):
            col = []
            for j in range(self.width):
                if initial[i, j] == 1:
                    col.append(Cell(LIVE))
                else:
                    col.append(Cell(DEAD))
            self.cells.append(col)

        self.started = False

    def print(self, *args):
        """ Prints a string based representation of the current state """
        for row in self.cells:
            for cell in row:
                print(f'{"#" if cell.state else ".":<2}', sep='', end='')
            print()
        print(*args)

    def evolve(self):
        """
        Evolves the current state one generation using GoL rules
            Rules applied to find the next state of each cell -->
                * Any live cell with more than 3 or less than 2 live neighbors dies
                * A live cell with 2-3 live neighbors lives on
                * Any dead cell with exactly 3 live neighbors becomes alive
        """

        # Copy the current population until the new state is fully created
        new_gen = deepcopy(self.cells)

        for i, row in enumerate(new_gen):
            for j, cell in enumerate(row):

                # Reset neighbor count to 0
                live_neighbors = 0

                # Loop through neighbors
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):

                        # Ignore the cell itself
                        if (k, l) == (i, j):
                            continue

                        # If neighbor is in bounds
                        if 0 <= k < self.height and 0 <= l < self.width:

                            neighbor_state = self.cells[k][l].state

                            #  print(f"Looking at cell ({k},{l}) with state {neighbor_state}")
                            if neighbor_state == LIVE:
                                live_neighbors += 1
                #  print(f'cell ({i},{j}) has {live_neighbors} live neighbors')
                if cell.state == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        cell.state = 0
                elif live_neighbors == 3:
                    cell.state = 1

        self.cells = new_gen


if __name__ == '__main__':
    pop = GameOfLife(4, 4, {(1, 0), (1, 1), (1, 2)})
    pop.print('\n')
    pop.evolve()
    pop.print('\n')
    pop.evolve()
    pop.print('\n')
