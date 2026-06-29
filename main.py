import pygame, random

pygame.init()

SCREEN_W= 480
MAX_V_TILES = 20
TILE_W = SCREEN_W//MAX_V_TILES

screen = pygame.display.set_mode((SCREEN_W, SCREEN_W))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
pygame.display.set_caption("Snake")

d = "R"
snake = [[0, 0]]
food = [None, None]
food_present = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and d != "D": d = "U"
            elif event.key == pygame.K_d and d != "L": d = "R"
            elif event.key == pygame.K_s and d != "U": d = "D"
            elif event.key == pygame.K_a and d != "R": d = "L"

    head = snake[0].copy()
    
    if d == "R": head[0] += 1
    elif d == "L": head[0] -= 1
    elif d == "U": head[1] -= 1
    elif d == "D": head[1] += 1

    if head in snake: exit()

    snake = [head] + snake
    
    if not food_present:
        while True:
            food[0] = random.randrange(0, MAX_V_TILES)
            food[1] = random.randrange(0, MAX_V_TILES)
            if food not in snake: break
        food_present = True

    if head[0] == food[0] and head[1] == food[1]: food_present = False
    else: snake.pop()
    
    if head[0] < 0 or head[0] >= MAX_V_TILES: exit()
    if head[1] < 0 or head[1] >= MAX_V_TILES: exit()

    screen.fill("black")
    
    if food_present: pygame.draw.rect(screen, "brown", (food[0]*TILE_W, food[1]*TILE_W, TILE_W, TILE_W))
    for i, body in enumerate(snake):
        pygame.draw.rect(screen, (0, 255, int(255*(i/len(snake)))), (body[0]*TILE_W, body[1]*TILE_W, TILE_W, TILE_W))
    score_text = font.render(f"{len(snake)}", False, "white")
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    clock.tick(10)

pygame.quit()