from collections import deque
import pygame

class GhostAgent:
    def __init__(self, maze, pos=(10, 3), mode="chaser", patrol_path=None, cell_size=24):
        self.maze = maze
        self.pos = pos
        self.mode = mode  # "chaser" atau "patroller"
        self.patrol_path = patrol_path or []
        self.index = 0  # untuk patrol
        self.delay = 0
        self.cell_size = cell_size

    def update(self, pacman_pos=None):
        # Update posisi dengan delay supaya gerak lambat
        if self.delay % 4 == 0:  # delay 4 frame
            if self.mode == "chaser" and pacman_pos is not None:
                self.pos = self.chase(pacman_pos)
            elif self.mode == "patroller" and self.patrol_path:
                self.index = (self.index + 1) % len(self.patrol_path)
                self.pos = self.patrol_path[self.index]
        self.delay += 1

    def chase(self, target):
        start = self.pos
        queue = deque([(start, [])])
        visited = set([start])
        while queue:
            (x, y), path = queue.popleft()
            if (x, y) == target:
                return path[0] if path else self.pos
            for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if self.maze.is_walkable((nx, ny)) and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), path + [(nx, ny)]))
        return self.pos

    def draw(self, screen):
        color = (255, 0, 0) if self.mode == "chaser" else (255, 128, 0)
        # Posisi tengah lingkaran dihitung dengan cell_size agar pas di grid
        center_x = self.pos[0] * self.cell_size + self.cell_size // 2
        center_y = self.pos[1] * self.cell_size + self.cell_size // 2
        pygame.draw.circle(screen, color, (center_x, center_y), self.cell_size // 2 - 4)
