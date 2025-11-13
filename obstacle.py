from abc import abstractmethod
from game_object import GameObject
import pygame
from config import PLAYER_GROUND_Y, HYDRANT_WIDTH, HYDRANT_HEIGHT, HYDRANT_COLOR, \
    STUMP_WIDTH, STUMP_HEIGHT, STUMP_COLOR, BIRD_WIDTH, BIRD_HEIGHT

class Obstacle(GameObject):
    """
    장애물 부모 클래스
    - GameObject 상속
    - 좌측 이동
    - 화면 밖 판정
    """
    
    def __init__(self, x, y, width, height, asset_manager, image_name):
        super().__init__(x, y, width, height)
        self._asset_manager = asset_manager
        self._image_name = image_name
        self._speed = 0
    
    def update(self, speed, *args, **kwargs): # GameObject의 update 시그니처에 맞춤
        """장애물 이동"""
        self._speed = speed
        self.x -= self._speed
    
    def is_off_screen(self):
        """화면 밖 판정"""
        return self.x + self.width < 0
    
    def draw(self, screen):
        """스프라이트 렌더링"""
        image = self._asset_manager.get_image(self._image_name)
        if image:
            screen.blit(image, self.get_rect())
        else: # 이미지가 없을 경우 fallback
            pygame.draw.rect(screen, (255, 0, 255), self.get_rect()) # 보라색으로 표시

class Hydrant(Obstacle):
    """소화전 장애물"""
    
    def __init__(self, x, asset_manager):
        super().__init__(x, PLAYER_GROUND_Y - HYDRANT_HEIGHT, 
                        HYDRANT_WIDTH, HYDRANT_HEIGHT, asset_manager, "hydrant")

class Stump(Obstacle):
    """나무 그루터기 장애물"""
    
    def __init__(self, x, asset_manager):
        super().__init__(x, PLAYER_GROUND_Y - STUMP_HEIGHT,
                        STUMP_WIDTH, STUMP_HEIGHT, asset_manager, "stump")

class Bird(Obstacle):
    """새 장애물 (공중)"""
    
    def __init__(self, x, y_pos, asset_manager):
        super().__init__(x, y_pos, BIRD_WIDTH, BIRD_HEIGHT, asset_manager, "bird")