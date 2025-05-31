import pygame
import random

class Maze:
    def __init__(self, width=20, height=21, tile_size=24):  # Ukuran sedang
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.grid = [[1 for _ in range(self.width)] for _ in range(self.height)]
        self.generate_maze()

    def generate_maze(self):
        for y in range(self.height):
            for x in range(self.width):
                if x == 0 or x == self.width-1 or y == 0 or y == self.height-1:
                    self.grid[y][x] = 1
                else:
                    self.grid[y][x] = 0

        mid_x = self.width // 2
        mid_y = self.height // 2

        # Dinding tengah (ghost house)
        for y in range(mid_y-2, mid_y+2):
            for x in range(mid_x-2, mid_x+2):
                self.grid[y][x] = 1

        for _ in range(50):  # Jumlah dinding acak sedang
            x = random.randint(1, self.width-2)
            y = random.randint(1, self.height-2)
            if not (mid_y-2 <= y < mid_y+2 and mid_x-2 <= x < mid_x+2):
                self.grid[y][x] = 1

        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == 0:
                    self.grid[y][x] = 2

    def is_walkable(self, pos):
        x, y = pos
        return 0 <= y < self.height and 0 <= x < self.width and self.grid[y][x] != 1

    def draw(self, screen):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                px = x * self.tile_size
                py = y * self.tile_size
                if cell == 1:
                    pygame.draw.rect(screen, (0, 0, 255), (px, py, self.tile_size, self.tile_size))
                elif cell == 2:
                    pygame.draw.circle(
                        screen,
                        (255, 255, 255),
                        (px + self.tile_size // 2, py + self.tile_size // 2),
                        max(2, self.tile_size // 8)
                    )

    def reset(self):
        self.generate_maze()
