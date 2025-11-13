import pygame
from game_object import GameObject
from config import PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_X, PLAYER_GROUND_Y, \
    PLAYER_JUMP_VELOCITY, PLAYER_GRAVITY, PLAYER_DUCK_HEIGHT, PLAYER_COLOR
from animation_controller import AnimationController

class Player(GameObject):
    """
    플레이어(퍼그) 클래스
    - GameObject 상속
    - 점프, 숙이기 동작
    - 물리 법칙 적용
    - 애니메이션 관리
    """
    
    def __init__(self, x, y, asset_manager):
        super().__init__(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        
        # Private 상태
        self._velocity_y = 0
        self._is_jumping = False
        self._is_ducking = False
        self._original_height = PLAYER_HEIGHT
        
        # 애니메이션 설정
        self._asset_manager = asset_manager
        self._animation_controller = AnimationController()
        self._setup_animations()
        self._animation_controller.play("run") # 기본 상태는 'run'
    
    def _setup_animations(self):
        """애니메이션 프레임 설정"""
        run_frames = [
            self._asset_manager.get_image("pug_run_1"),
            self._asset_manager.get_image("pug_run_2")
        ]
        jump_frame = [self._asset_manager.get_image("pug_jump")]
        duck_frame = [self._asset_manager.get_image("pug_duck")]
        
        self._animation_controller.add_animation("run", run_frames, fps=10)
        self._animation_controller.add_animation("jump", jump_frame, fps=1)
        self._animation_controller.add_animation("duck", duck_frame, fps=1)

    # Public 인터페이스
    def jump(self):
        """점프 시작"""
        if not self._is_jumping:
            self._velocity_y = PLAYER_JUMP_VELOCITY
            self._is_jumping = True
            self._animation_controller.play("jump")
    
    def duck(self):
        """숙이기"""
        if not self._is_jumping:
            self._is_ducking = True
            self.height = PLAYER_DUCK_HEIGHT
            self._animation_controller.play("duck")
    
    def stand_up(self):
        """일어서기"""
        self._is_ducking = False
        self.height = self._original_height
        self._animation_controller.play("run")
    
    # 추상 메서드 구현
    def update(self, *args, **kwargs):
        """물리 및 애니메이션 업데이트"""
        if self._is_jumping:
            self._apply_gravity()
            self._check_landing()
        
        self._animation_controller.update()
    
    def draw(self, screen):
        """퍼그 렌더링"""
        current_frame = self._animation_controller.get_current_frame()
        if current_frame:
            rect = self.get_rect()
            screen.blit(current_frame, rect)
        else: # 이미지가 없을 경우 fallback
            rect = self.get_rect()
            pygame.draw.ellipse(screen, PLAYER_COLOR, rect)
    
    # Private 메서드 (내부 로직)
    def _apply_gravity(self):
        """중력 적용 (캡슐화)"""
        self.y += self._velocity_y
        self._velocity_y += PLAYER_GRAVITY
    
    def _check_landing(self):
        """착지 판정 (캡슐화)"""
        if self.y + self.height >= PLAYER_GROUND_Y + self._original_height:
            self.y = PLAYER_GROUND_Y
            self._is_jumping = False
            self._velocity_y = 0
            self._animation_controller.play("run") # 착지 시 달리기 애니메이션으로 전환
    
    def reset(self):
        """초기 상태로 리셋"""
        self.y = PLAYER_GROUND_Y
        self._velocity_y = 0
        self._is_jumping = False
        self._is_ducking = False
        self.height = self._original_height
        self._animation_controller.play("run")