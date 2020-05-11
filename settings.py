import numpy as np
# puppy


class Settings:
    def __init__(self):
        self.size = self.screen_width, self.screen_height = 800, 600
        self.block_size = 20
        self.bg_color = (230, 230, 0)
        h, w = int(self.screen_height / self.block_size), int(self.screen_width / self.block_size)
        self.population = np.zeros((h, w))
