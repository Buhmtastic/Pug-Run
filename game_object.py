from abc import ABC, abstractmethod
import pygame

class GameObject(ABC):
    """
    모든 게임 객체의 추상 부모 클래스
    - 위치, 크기 관리
    - 렌더링 인터페이스
    - 충돌 박스 제공
    """
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @abstractmethod
    def update(self, *args, **kwargs):
        """상태 업데이트 (자식 클래스에서 구현)"""
        pass

    @abstractmethod
    def draw(self, screen):
        """화면 렌더링 (자식 클래스에서 구현)"""
        pass

    def get_rect(self):
        """충돌 감지용 Rect 반환"""
        return pygame.Rect(self.x, self.y, self.width, self.height)
