import pygame
from game_object import GameObject
from config import PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_X, PLAYER_GROUND_Y, \
    PLAYER_JUMP_VELOCITY, PLAYER_GRAVITY, PLAYER_DUCK_HEIGHT, PLAYER_COLOR

class Player(GameObject):
    """
    플레이어(퍼그) 클래스
    - GameObject 상속
    - 점프, 숙이기 동작
    - 물리 법칙 적용
    """
    
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        
        # Private 상태
        self._velocity_y = 0
        self._is_jumping = False
        self._is_ducking = False
        self._original_height = PLAYER_HEIGHT # 숙이기 후 원래 높이로 돌아오기 위함
    
    # Public 인터페이스
    def jump(self):
        """점프 시작"""
        if not self._is_jumping:
            self._velocity_y = PLAYER_JUMP_VELOCITY
            self._is_jumping = True
    
    def duck(self):
        """숙이기"""
        if not self._is_jumping: # 점프 중에는 숙일 수 없음
            self._is_ducking = True
            self.height = PLAYER_DUCK_HEIGHT # 높이 변경
    
    def stand_up(self):
        """일어서기"""
        self._is_ducking = False
        self.height = self._original_height # 원래 높이로 복귀
    
    # 추상 메서드 구현
    def update(self, *args, **kwargs):
        """물리 업데이트"""
        if self._is_jumping:
            self._apply_gravity()
            self._check_landing()
    
    def draw(self, screen):
        """퍼그 렌더링"""
        rect = self.get_rect()
        pygame.draw.ellipse(screen, PLAYER_COLOR, rect)
        self._draw_eyes(screen) # 눈 그리기
    
    # Private 메서드 (내부 로직)
    def _apply_gravity(self):
        """중력 적용 (캡슐화)"""
        self.y += self._velocity_y
        self._velocity_y += PLAYER_GRAVITY
    
    def _check_landing(self):
        """착지 판정 (캡슐화)"""
        # 플레이어의 바닥이 지면 Y 위치보다 아래로 내려가지 않도록
        if self.y + self.height >= PLAYER_GROUND_Y + self._original_height: # 플레이어의 바닥이 지면과 닿았을 때
            self.y = PLAYER_GROUND_Y # 지면 위치로 고정
            self._is_jumping = False
            self._velocity_y = 0
    
    def _draw_eyes(self, screen):
        """눈 그리기 (내부 디테일)"""
        # 퍼그의 몸체에 비례하여 눈 위치 조정
        eye1_pos = (self.x + self.width // 4, self.y + self.height // 4)
        eye2_pos = (self.x + self.width * 3 // 4, self.y + self.height // 4)
        pygame.draw.circle(screen, (0, 0, 0), eye1_pos, 2)
        pygame.draw.circle(screen, (0, 0, 0), eye2_pos, 2)
    
    def reset(self):
        """초기 상태로 리셋"""
        self.y = PLAYER_GROUND_Y
        self._velocity_y = 0
        self._is_jumping = False
        self._is_ducking = False
        self.height = self._original_height # 높이도 원래대로 복귀
