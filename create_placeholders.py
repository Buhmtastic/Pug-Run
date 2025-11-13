import pygame
import os
from config import (
    PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_DUCK_HEIGHT, PLAYER_COLOR,
    PUG_RUN_2_COLOR, PUG_JUMP_COLOR,
    HYDRANT_WIDTH, HYDRANT_HEIGHT, HYDRANT_COLOR,
    STUMP_WIDTH, STUMP_HEIGHT, STUMP_COLOR,
    BIRD_WIDTH, BIRD_HEIGHT, BIRD_COLOR
)

# assets/images 디렉토리가 없으면 생성
os.makedirs("assets/images", exist_ok=True)

# 플레이어 이미지
player_size = (PLAYER_WIDTH, PLAYER_HEIGHT)
duck_size = (PLAYER_WIDTH, PLAYER_DUCK_HEIGHT)

# pug_run_1.png
run1_surface = pygame.Surface(player_size)
run1_surface.fill(PLAYER_COLOR)
pygame.image.save(run1_surface, "assets/images/pug_run_1.png")

# pug_run_2.png
run2_surface = pygame.Surface(player_size)
run2_surface.fill(PUG_RUN_2_COLOR)
pygame.image.save(run2_surface, "assets/images/pug_run_2.png")

# pug_jump.png
jump_surface = pygame.Surface(player_size)
jump_surface.fill(PUG_JUMP_COLOR)
pygame.image.save(jump_surface, "assets/images/pug_jump.png")

# pug_duck.png
duck_surface = pygame.Surface(duck_size)
duck_surface.fill(STUMP_COLOR)
pygame.image.save(duck_surface, "assets/images/pug_duck.png")

# 장애물 이미지
# hydrant.png
hydrant_size = (HYDRANT_WIDTH, HYDRANT_HEIGHT)
hydrant_surface = pygame.Surface(hydrant_size)
hydrant_surface.fill(HYDRANT_COLOR)
pygame.image.save(hydrant_surface, "assets/images/hydrant.png")

# stump.png
stump_size = (STUMP_WIDTH, STUMP_HEIGHT)
stump_surface = pygame.Surface(stump_size)
stump_surface.fill(STUMP_COLOR)
pygame.image.save(stump_surface, "assets/images/stump.png")

# bird.png
bird_size = (BIRD_WIDTH, BIRD_HEIGHT)
bird_surface = pygame.Surface(bird_size)
bird_surface.fill(BIRD_COLOR)
pygame.image.save(bird_surface, "assets/images/bird.png")

print("Placeholder images created successfully.")
