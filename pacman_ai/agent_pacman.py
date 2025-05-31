import pygame

class PacMan:
    def __init__(self, maze, start_pos=(1, 1), cell_size=24):
        self.maze = maze
        self.pos = start_pos
        self.direction = (0, 0)
        self.cell_size = cell_size

    def reset(self):
        self.pos = (1, 1)
        self.direction = (0, 0)

    def handle_input(self, key):
        if key == pygame.K_UP:
            self.try_change_direction((0, -1))
        elif key == pygame.K_DOWN:
            self.try_change_direction((0, 1))
        elif key == pygame.K_LEFT:
            self.try_change_direction((-1, 0))
        elif key == pygame.K_RIGHT:
            self.try_change_direction((1, 0))

    def try_change_direction(self, new_dir):
        # Cek apakah arah baru bisa dilewati, kalau bisa update arah
        new_pos = (self.pos[0] + new_dir[0], self.pos[1] + new_dir[1])
        if self.maze.is_walkable(new_pos):
            self.direction = new_dir

    def update(self):
        # Gerak otomatis sesuai arah selama jalan bisa dilewati
        new_pos = (self.pos[0] + self.direction[0], self.pos[1] + self.direction[1])
        if self.maze.is_walkable(new_pos):
            self.pos = new_pos
        else:
            self.direction = (0, 0)  # berhenti jika tidak bisa lanjut

    def eat(self):
        # Jika ada pellet (2) di posisi saat ini, hapus dan beri skor 10
        x, y = self.pos
        if self.maze.grid[y][x] == 2:
            self.maze.grid[y][x] = 0
            return 10
        return 0

    def draw(self, screen):
        center = (self.pos[0] * self.cell_size + self.cell_size // 2,
                  self.pos[1] * self.cell_size + self.cell_size // 2)
        pygame.draw.circle(screen, (255, 255, 0), center, self.cell_size // 2 - 2)
