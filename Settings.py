import numpy as np


class Settings:
    '''
    Settings for the Game of Life player. Defaults can be modified.
    (Extend docstring when utilized more)
    '''

    def __init__(self, px_height=800, px_width=600,
                 cell_size=20, bg_color=(230, 230, 0)):

        self.size = self.screen_height, self.screen_width = px_height, px_width
        self.block_size = cell_size
        self.bg_color = bg_color
        self.h, self.w = int(self.screen_height / self.block_size),\
                         int(self.screen_width / self.block_size)
        self.population = np.zeros((self.h, self.w))
