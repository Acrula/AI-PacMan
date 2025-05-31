import pygame

class PacMan:
    def __init__(self, maze, cell_size=24):
        self.maze = maze
        self.cell_size = cell_size
        self.pos = (1, 1)
        self.dir = (0, 0)

    def handle_input(self, key):
        if key == pygame.K_UP:
            self.dir = (0, -1)
        elif key == pygame.K_DOWN:
            self.dir = (0, 1)
        elif key == pygame.K_LEFT:
            self.dir = (-1, 0)
        elif key == pygame.K_RIGHT:
            self.dir = (1, 0)

    def update(self):
        new_pos = (self.pos[0] + self.dir[0], self.pos[1] + self.dir[1])
        if self.maze.is_walkable(new_pos):
            self.pos = new_pos

    def eat(self):
        x, y = self.pos
        if self.maze.grid[y][x] == 2:
            self.maze.grid[y][x] = 0
            return 10
        return 0

    def reset(self):
        self.pos = (1, 1)
        self.dir = (0, 0)

    def draw(self, screen):
        cx = self.pos[0] * self.cell_size + self.cell_size // 2
        cy = self.pos[1] * self.cell_size + self.cell_size // 2
        pygame.draw.circle(screen, (255, 255, 0), (cx, cy), self.cell_size // 2 - 2)
