import random, pygame

W, H = 480, 360
pygame.init()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("ShopEasy Catch - arrows to move, R to restart")
font = pygame.font.Font(None, 30)
clock = pygame.time.Clock()

def new_game():
    return {"basket": pygame.Rect(W // 2 - 40, H - 40, 80, 24), "items": [], "score": 0, "lives": 3, "frame": 0}

g = new_game()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            g = new_game()
    keys = pygame.key.get_pressed()
    if g["lives"] > 0:
        g["basket"].x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 8
        g["basket"].clamp_ip(screen.get_rect())
        g["frame"] += 1
        if g["frame"] % max(8, 25 - g["score"] // 50) == 0:
            g["items"].append([pygame.Rect(random.randint(10, W - 30), -20, 22, 22), random.uniform(3, 6) + g["score"] / 200, random.random() < 0.25])
        for item in g["items"][:]:
            item[0].y += item[1]
            if item[0].colliderect(g["basket"]):
                g["lives" if item[2] else "score"] += -1 if item[2] else 10
                g["items"].remove(item)
            elif item[0].top > H:
                g["items"].remove(item)
    screen.fill((235, 242, 250))
    pygame.draw.rect(screen, (44, 90, 154), g["basket"], border_radius=6)
    for rect, _, bad in g["items"]:
        if bad: pygame.draw.rect(screen, (190, 60, 60), rect)
        else: pygame.draw.circle(screen, (224, 169, 62), rect.center, 11)
    screen.blit(font.render(f"Score {g['score']}   Lives {g['lives']}", True, (20, 26, 35)), (10, 10))
    if g["lives"] <= 0:
        screen.blit(font.render("Game over! Press R to play again", True, (190, 60, 60)), (70, H // 2))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()