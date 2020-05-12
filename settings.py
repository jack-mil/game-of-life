import numpy as np

# puppy


class Settings:
    def __init__(self,
                 px_height=800,
                 px_width=600,
                 cell_size=20,
                 bg_color=(230, 230, 0)):

        self.size = self.screen_width, self.screen_height = px_height, px_width
        self.block_size = cell_size
        self.bg_color = bg_color
        h, w = int(self.screen_height / self.block_size), int(self.screen_width / self.block_size)
        self.population = np.zeros((h, w))
