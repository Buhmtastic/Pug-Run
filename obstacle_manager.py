import pygame
import random
from obstacle import Hydrant, Stump, Bird 
from config import SCREEN_WIDTH, OBSTACLE_SPAWN_MIN_GAP, OBSTACLE_SPAWN_MAX_GAP, BIRD_Y_POSITIONS 

class ObstacleManager:
    """
    장애물 관리 클래스
    - 장애물 생성 (Factory Pattern)
    - 장애물 업데이트
    - 충돌 감지
    """
    
    def __init__(self, asset_manager):
        self._obstacles = []  # private: 장애물 리스트
        self._asset_manager = asset_manager # AssetManager 의존성 주입
        self._last_spawn_x = SCREEN_WIDTH
        self._spawn_gap = OBSTACLE_SPAWN_MIN_GAP 
    
    def update(self, speed):
        """모든 장애물 업데이트"""
        for obstacle in list(self._obstacles): 
            obstacle.update(speed)
        
        self._remove_off_screen_obstacles()
        self._spawn_obstacle_if_needed()
    
    def draw(self, screen):
        """모든 장애물 렌더링"""
        for obstacle in self._obstacles:
            obstacle.draw(screen)
    
    def check_collision(self, player):
        """플레이어와 충돌 검사"""
        player_rect = player.get_rect()
        for obstacle in self._obstacles:
            if player_rect.colliderect(obstacle.get_rect()):
                return True
        return False
    
    def clear(self):
        """모든 장애물 제거"""
        self._obstacles.clear()
    
    # Private 메서드 (Factory Pattern)
    def _spawn_obstacle_if_needed(self):
        """장애물 생성 로직 (캡슐화)"""
        if len(self._obstacles) == 0 or \
           self._obstacles[-1].x < SCREEN_WIDTH - self._spawn_gap:
            obstacle = self._create_random_obstacle()
            self._obstacles.append(obstacle)
            self._spawn_gap = random.randint(
                OBSTACLE_SPAWN_MIN_GAP, 
                OBSTACLE_SPAWN_MAX_GAP
            )
    
    def _create_random_obstacle(self):
        """랜덤 장애물 생성 (Factory Pattern)"""
        obstacle_type = random.choice(['hydrant', 'stump', 'bird']) 
        
        if obstacle_type == 'hydrant':
            return Hydrant(SCREEN_WIDTH, self._asset_manager)
        elif obstacle_type == 'stump':
            return Stump(SCREEN_WIDTH, self._asset_manager)
        else: # 'bird'
            y_pos = random.choice(BIRD_Y_POSITIONS)
            return Bird(SCREEN_WIDTH, y_pos, self._asset_manager)
    
    def _remove_off_screen_obstacles(self):
        """화면 밖 장애물 제거 (캡슐화)"""
        self._obstacles = [obs for obs in self._obstacles 
                          if not obs.is_off_screen()]