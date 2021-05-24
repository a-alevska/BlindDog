from agents import *
from ipythonblocks import BlockGrid

color = {"Breeze": (225, 225, 225),
        "Pit": (0,0,0),
        "Gold": (253, 208, 23),
        "Glitter": (253, 208, 23),
        "Wumpus": (43, 27, 23),
        "Stench": (128, 128, 128),
        "Explorer": (0, 0, 255),
        "Wall": (44, 53, 57)
        }

class wampusEnvironment(Environment):

    def program(percepts):
        '''Returns an action based on it's percepts'''
        print(percepts)
        return input()

        w = WumpusEnvironment(program, 7, 7)         
        grid = BlockGrid(w.width, w.height, fill=(123, 234, 123))

        def draw_grid(world):
            global grid
            grid[:] = (123, 234, 123)
            for x in range(0, len(world)):
                for y in range(0, len(world[x])):
                    if len(world[x][y]):
                        grid[y, x] = color[world[x][y][-1].__class__.__name__]

        def step():
            global grid, w
            draw_grid(w.get_world())
            grid.show()
            w.step()

