import pygame
from agent_pacman import PacMan
from agent_ghost import GhostAgent
from maze import Maze

pygame.init()

maze = Maze()  # Ukuran sudah diset sedang

screen_width = maze.width * maze.tile_size
screen_height = maze.height * maze.tile_size
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Custom Pac-Man")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

pacman = PacMan(maze)
ghosts = [GhostAgent(maze, pos=(10, 3), mode="chaser")]

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

    maze.draw(screen)
    pacman.draw(screen)
    for ghost in ghosts:
        ghost.draw(screen)

    screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (10, 10))
    screen.blit(font.render(f"Lives: {lives}", True, (255, 255, 255)), (screen_width - 140, 10))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
