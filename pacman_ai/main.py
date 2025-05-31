import pygame
from agent_pacman import PacMan
from agent_ghost import GhostAgent
from maze import Maze

# Inisialisasi pygame
pygame.init()
maze = Maze()
tile_size = 24
screen_width = maze.width * tile_size
screen_height = maze.height * tile_size
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Custom Pac-Man")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Inisialisasi game
pacman = PacMan(maze, cell_size=tile_size)
ghosts = [
    GhostAgent(maze, pos=(10, 3), mode="chaser", cell_size=tile_size),
]

score = 0
lives = 3

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            pacman.handle_input(event.key)

    pacman.update()
    for ghost in ghosts:
        ghost.update(pacman.pos)

    for ghost in ghosts:
        if ghost.pos == pacman.pos:
            lives -= 1
            pacman.reset()
            if lives == 0:
                running = False

    score += pacman.eat()

    if maze.is_cleared():
        maze.draw(screen)
        pacman.draw(screen)
        for ghost in ghosts:
            ghost.draw(screen)
        win_text = font.render("You Win!", True, (255, 255, 0))
        screen.blit(win_text, (screen_width // 2 - 80, screen_height // 2 - 20))
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

    maze.draw(screen)
    pacman.draw(screen)
    for ghost in ghosts:
        ghost.draw(screen)

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    lives_text = font.render(f"Lives: {lives}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (screen_width - 150, 10))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
