import pygame
import os

class AssetManager:
    """
    리소스 관리 클래스
    - 이미지, 사운드 로딩 및 캐싱
    - 에러 처리 및 기본값 제공
    """
    
    def __init__(self):
        self._images = {}  # private: 이미지 딕셔너리
        self._sounds = {}  # private: 사운드 딕셔너리 (선택 사항)
    
    def load_image(self, name, path):
        """이미지 로드 및 캐싱"""
        if name not in self._images:
            full_path = os.path.join('assets', 'images', path)
            try:
                image = pygame.image.load(full_path).convert_alpha()
                self._images[name] = image
            except pygame.error as e:
                print(f"Error loading image {full_path}: {e}")
                self._images[name] = None # 로드 실패 시 None 저장
        return self._images[name]
    
    def get_image(self, name):
        """캐시된 이미지 반환"""
        return self._images.get(name)
    
    # 사운드 관련 메서드는 선택 사항이므로 나중에 구현
    # def load_sound(self, name, path):
    #     if name not in self._sounds:
    #         full_path = os.path.join('assets', 'sounds', path)
    #         try:
    #             sound = pygame.mixer.Sound(full_path)
    #             self._sounds[name] = sound
    #         except pygame.error as e:
    #             print(f"Error loading sound {full_path}: {e}")
    #             self._sounds[name] = None
    #     return self._sounds[name]
    
    # def get_sound(self, name):
    #     return self._sounds.get(name)
    
    # def play_sound(self, name):
    #     sound = self.get_sound(name)
    #     if sound:
    #         sound.play()
