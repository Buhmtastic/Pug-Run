import pygame

class AnimationController:
    """
    애니메이션 관리 클래스
    - 애니메이션 상태 캡슐화
    """
    
    def __init__(self):
        self._frames = {}  # {animation_name: [frame1, frame2, ...]}`
        self._current_animation = None
        self._current_frame_index = 0
        self._frame_duration = 0 # ms per frame
        self._last_frame_time = 0
    
    def add_animation(self, name, frames, fps):
        """애니메이션 추가"""
        self._frames[name] = frames
        self._frame_duration = 1000 // fps # ms
    
    def play(self, name):
        """애니메이션 재생"""
        if self._current_animation != name:
            self._current_animation = name
            self._current_frame_index = 0
            self._last_frame_time = pygame.time.get_ticks()
    
    def update(self):
        """애니메이션 업데이트"""
        if self._current_animation and self._frames[self._current_animation]:
            current_time = pygame.time.get_ticks()
            if current_time - self._last_frame_time > self._frame_duration:
                self._current_frame_index = (self._current_frame_index + 1) % \
                                            len(self._frames[self._current_animation])
                self._last_frame_time = current_time
    
    def get_current_frame(self):
        """현재 프레임 이미지 반환"""
        if self._current_animation and self._frames[self._current_animation]:
            return self._frames[self._current_animation][self._current_frame_index]
        return None
