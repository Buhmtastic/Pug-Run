import pygame

class AnimationController:
    """
    애니메이션 관리 클래스
    - 애니메이션 상태 캡슐화
    - 각 애니메이션별 독립적인 fps 관리
    """

    def __init__(self):
        self._animations = {}  # {name: {'frames': [...], 'fps': 10, 'frame_duration': 100}}
        self._current_animation = None
        self._current_frame_index = 0
        self._last_frame_time = 0

    def add_animation(self, name, frames, fps):
        """애니메이션 추가 (각 애니메이션마다 독립적인 fps)"""
        self._animations[name] = {
            'frames': frames,
            'fps': fps,
            'frame_duration': 1000 // fps  # ms per frame
        }

    def play(self, name):
        """애니메이션 재생"""
        if self._current_animation != name and name in self._animations:
            self._current_animation = name
            self._current_frame_index = 0
            self._last_frame_time = pygame.time.get_ticks()

    def update(self):
        """애니메이션 업데이트"""
        if self._current_animation and self._current_animation in self._animations:
            anim = self._animations[self._current_animation]
            current_time = pygame.time.get_ticks()
            if current_time - self._last_frame_time > anim['frame_duration']:
                self._current_frame_index = (self._current_frame_index + 1) % len(anim['frames'])
                self._last_frame_time = current_time

    def get_current_frame(self):
        """현재 프레임 이미지 반환"""
        if self._current_animation and self._current_animation in self._animations:
            return self._animations[self._current_animation]['frames'][self._current_frame_index]
        return None
