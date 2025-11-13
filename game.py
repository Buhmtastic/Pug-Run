import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BACKGROUND_COLOR, GROUND_COLOR, GROUND_Y, INITIAL_GAME_SPEED, PLAYER_X, PLAYER_GROUND_Y, SCORE_INCREMENT, SPEED_INCREMENT, MAX_GAME_SPEED
from player import Player 
from obstacle_manager import ObstacleManager 
from score_manager import ScoreManager

class Game:
    """
    게임 전체 생명주기 관리
    - 게임 루프
    - 상태 관리
    - 객체 간 상호작용 조율
    """
    
    def __init__(self):
        """게임 초기화"""
        pygame.init()
        self._screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pug Run")
        self._clock = pygame.time.Clock()
        self._running = False
        self._game_over = False
        
        # 게임 객체들 (의존성 주입 가능)
        self._player = Player(PLAYER_X, PLAYER_GROUND_Y) 
        self._obstacle_manager = ObstacleManager() 
        self._score_manager = ScoreManager() # ScoreManager 인스턴스화
        self._game_speed = INITIAL_GAME_SPEED
    
    # Public 인터페이스
    def run(self):
        """메인 게임 루프 (외부 호출용)"""
        self._running = True
        while self._running:
            self._handle_events()
            self._update()
            self._draw()
            self._clock.tick(FPS)
        pygame.quit()
    
    # Private 메서드 (내부 구현)
    def _handle_events(self):
        """입력 처리 (캡슐화)"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            elif event.type == pygame.KEYDOWN:
                if self._game_over:
                    if event.key == pygame.K_SPACE:
                        self.reset()
                else:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                        self._player.jump()
                    elif event.key == pygame.K_DOWN:
                        self._player.duck()
            elif event.type == pygame.KEYUP:
                if not self._game_over:
                    if event.key == pygame.K_DOWN:
                        self._player.stand_up()
    
    def _update(self):
        """게임 상태 업데이트 (캡슐화)"""
        if not self._game_over:
            self._player.update()
            self._obstacle_manager.update(self._game_speed)
            self._check_collision()
            self._update_score() 
            self._increase_difficulty() # 난이도 증가 로직 호출
    
    def _draw(self):
        """화면 렌더링 (캡슐화)"""
        self._screen.fill(BACKGROUND_COLOR)
        
        # 바닥 라인 렌더링
        pygame.draw.line(self._screen, GROUND_COLOR, (0, GROUND_Y), (SCREEN_WIDTH, GROUND_Y), 2)

        self._player.draw(self._screen)
        self._obstacle_manager.draw(self._screen)
        self._draw_score() # 점수 표시 호출

        if self._game_over:
            self._draw_game_over_screen()
        
        pygame.display.flip() # 화면 업데이트
    
    def _check_collision(self):
        """충돌 검사 (내부 로직)"""
        if self._obstacle_manager.check_collision(self._player):
            self._game_over = True
    
    def _update_score(self):
        """점수 업데이트 (내부 로직)"""
        self._score_manager.add_score(SCORE_INCREMENT)
    
    def _increase_difficulty(self):
        """난이도 증가 (내부 로직)"""
        if self._game_speed < MAX_GAME_SPEED:
            self._game_speed += SPEED_INCREMENT
    
    def _draw_score(self):
        """점수 표시"""
        font = pygame.font.Font(None, 30)
        score_text = font.render(f"Score: {self._score_manager.score}", True, (0, 0, 0))
        high_score_text = font.render(f"High Score: {self._score_manager.high_score}", True, (0, 0, 0))
        self._screen.blit(score_text, (SCREEN_WIDTH - score_text.get_width() - 10, 10))
        self._screen.blit(high_score_text, (SCREEN_WIDTH - high_score_text.get_width() - 10, 40))
    
    def _draw_game_over_screen(self):
        """게임 오버 화면 렌더링"""
        font = pygame.font.Font(None, 50)
        text = font.render("Game Over!", True, (0, 0, 0))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20))
        self._screen.blit(text, text_rect)

        restart_font = pygame.font.Font(None, 30)
        restart_text = restart_font.render("Press SPACE to Restart", True, (0, 0, 0))
        restart_text_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30))
        self._screen.blit(restart_text, restart_text_rect)
    
    def reset(self):
        """게임 재시작 (Public)"""
        self._game_over = False
        self._game_speed = INITIAL_GAME_SPEED
        self._player.reset()
        self._obstacle_manager.clear()
        self._score_manager.reset() # ScoreManager 리셋 호출