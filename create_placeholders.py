import pygame
import os

# assets/images 디렉토리가 없으면 생성
os.makedirs("assets/images", exist_ok=True)

# 플레이어 이미지
player_size = (40, 30)
duck_size = (40, 20)
pygame.draw.rect(pygame.Surface(player_size), (245, 222, 179), (0, 0, *player_size))
pygame.image.save(pygame.Surface(player_size), "assets/images/pug_run_1.png")

run2_surface = pygame.Surface(player_size)
run2_surface.fill((210, 180, 140))
pygame.image.save(run2_surface, "assets/images/pug_run_2.png")

jump_surface = pygame.Surface(player_size)
jump_surface.fill((173, 216, 230))
pygame.image.save(jump_surface, "assets/images/pug_jump.png")

duck_surface = pygame.Surface(duck_size)
duck_surface.fill((139, 69, 19))
pygame.image.save(duck_surface, "assets/images/pug_duck.png")

# 장애물 이미지
hydrant_size = (25, 35)
hydrant_surface = pygame.Surface(hydrant_size)
hydrant_surface.fill((220, 20, 60))
pygame.image.save(hydrant_surface, "assets/images/hydrant.png")

stump_size = (30, 25)
stump_surface = pygame.Surface(stump_size)
stump_surface.fill((139, 69, 19))
pygame.image.save(stump_surface, "assets/images/stump.png")

bird_size = (35, 25)
bird_surface = pygame.Surface(bird_size)
bird_surface.fill((128, 128, 128))
pygame.image.save(bird_surface, "assets/images/bird.png")

print("Placeholder images created successfully.")
