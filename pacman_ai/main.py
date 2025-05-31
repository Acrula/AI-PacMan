import pygame
from agent_pacman import PacMan
from agent_ghost import GhostAgent
from maze import Maze

# Inisialisasi pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Custom Pac-Man")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Inisialisasi game
maze = Maze()
pacman = PacMan(maze)
ghosts = [
    GhostAgent(maze, pos=(10, 3), mode="chaser"),
]

score = 0
lives = 3

running = True
while running:
    screen.fill((0, 0, 0))

    # Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            pacman.handle_input(event.key)

    # Update
    pacman.update()
    for ghost in ghosts:
        ghost.update(pacman.pos)

    # Deteksi tabrakan dengan ghost
    for ghost in ghosts:
        if ghost.pos == pacman.pos:
            lives -= 1
            pacman.reset()
            if lives == 0:
                running = False

    # Update skor jika makan pellet
    score += pacman.eat()

    # Gambar semua elemen
    maze.draw(screen)
    pacman.draw(screen)
    for ghost in ghosts:
        ghost.draw(screen)

    # Teks skor dan nyawa
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    lives_text = font.render(f"Lives: {lives}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (500, 10))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
