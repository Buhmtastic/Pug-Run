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
    
    def __init__(self, x, y, width, height, obstacle_type):
        super().__init__(x, y, width, height)
        self._obstacle_type = obstacle_type
        self._speed = 0 # 장애물 이동 속도는 Game 클래스에서 주입받음
    
    def update(self, speed, *args, **kwargs): # GameObject의 update 시그니처에 맞춤
        """장애물 이동"""
        self._speed = speed
        self.x -= self._speed
    
    def is_off_screen(self):
        """화면 밖 판정"""
        return self.x + self.width < 0
    
    @abstractmethod
    def draw(self, screen):
        """렌더링 (자식 클래스에서 구현)"""
        pass

class Hydrant(Obstacle):
    """소화전 장애물"""
    
    def __init__(self, x):
        super().__init__(x, PLAYER_GROUND_Y - HYDRANT_HEIGHT, 
                        HYDRANT_WIDTH, HYDRANT_HEIGHT, 'hydrant')
    
    def draw(self, screen):
        """소화전 렌더링"""
        rect = self.get_rect()
        pygame.draw.rect(screen, HYDRANT_COLOR, rect)

class Stump(Obstacle):
    """나무 그루터기 장애물"""
    
    def __init__(self, x):
        super().__init__(x, PLAYER_GROUND_Y - STUMP_HEIGHT,
                        STUMP_WIDTH, STUMP_HEIGHT, 'stump')
    
    def draw(self, screen):
        """나무 렌더링"""
        rect = self.get_rect()
        pygame.draw.rect(screen, STUMP_COLOR, rect)

class Bird(Obstacle):
    """새 장애물 (공중)"""
    
    def __init__(self, x, y_pos):
        super().__init__(x, y_pos, BIRD_WIDTH, BIRD_HEIGHT, 'bird')
    
    def draw(self, screen):
        """새 렌더링"""
        rect = self.get_rect()
        pygame.draw.ellipse(screen, (128, 128, 128), rect) # 회색 타원으로 임시 렌더링
