import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, DAY_BACKGROUND_COLOR, NIGHT_BACKGROUND_COLOR, GROUND_COLOR, GROUND_Y, INITIAL_GAME_SPEED, PLAYER_X, PLAYER_GROUND_Y, SCORE_INCREMENT, SPEED_INCREMENT, MAX_GAME_SPEED, DAY_NIGHT_SWITCH_SCORE, \
    SCORE_TEXT_SIZE, GAME_OVER_TEXT_SIZE, RESTART_TEXT_SIZE, SCORE_POS_X_OFFSET, SCORE_POS_Y_SCORE, SCORE_POS_Y_HIGH_SCORE, GAME_OVER_POS_Y_OFFSET, RESTART_POS_Y_OFFSET 
from player import Player 
from obstacle_manager import ObstacleManager 
from score_manager import ScoreManager
from asset_manager import AssetManager 

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
        
        # AssetManager 초기화
        self._asset_manager = AssetManager()
        self._load_assets() # 에셋 로드
        
        # 폰트 로드 (한 번만)
        self._score_font = pygame.font.Font(None, SCORE_TEXT_SIZE)
        self._game_over_font = pygame.font.Font(None, GAME_OVER_TEXT_SIZE)
        self._restart_font = pygame.font.Font(None, RESTART_TEXT_SIZE)
        
        # 게임 객체들 (의존성 주입 가능)
        self._player = Player(PLAYER_X, PLAYER_GROUND_Y, self._asset_manager) 
        self._obstacle_manager = ObstacleManager(self._asset_manager) 
        self._score_manager = ScoreManager() 
        self._game_speed = INITIAL_GAME_SPEED
        self._is_day = True 
    
    def _load_assets(self):
        """게임에 필요한 에셋 로드"""
        # 플레이어 스프라이트 (임시 플레이스홀더)
        self._asset_manager.load_image("pug_run_1", "pug_run_1.png")
        self._asset_manager.load_image("pug_run_2", "pug_run_2.png")
        self._asset_manager.load_image("pug_jump", "pug_jump.png")
        self._asset_manager.load_image("pug_duck", "pug_duck.png")
        
        # 장애물 스프라이트 (임시 플레이스홀더)
        self._asset_manager.load_image("hydrant", "hydrant.png")
        self._asset_manager.load_image("stump", "stump.png")
        self._asset_manager.load_image("bird", "bird.png")

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
            self._increase_difficulty() 
            self._check_day_night_cycle() 
    
    def _draw(self):
        """화면 렌더링 (캡슐화)"""
        current_bg_color = DAY_BACKGROUND_COLOR if self._is_day else NIGHT_BACKGROUND_COLOR
        self._screen.fill(current_bg_color)
        
        # 바닥 라인 렌더링
        pygame.draw.line(self._screen, GROUND_COLOR, (0, GROUND_Y), (SCREEN_WIDTH, GROUND_Y), 2)

        self._player.draw(self._screen)
        self._obstacle_manager.draw(self._screen)
        self._draw_score() 

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
    
    def _check_day_night_cycle(self):
        """낮/밤 전환 로직"""
        if self._score_manager.score > 0 and \
           (self._score_manager.score // DAY_NIGHT_SWITCH_SCORE) % 2 == 1:
            self._is_day = False 
        else:
            self._is_day = True 
    
    def _draw_score(self):
        """점수 표시"""
        score_text = self._score_font.render(f"Score: {self._score_manager.score}", True, (0, 0, 0))
        high_score_text = self._score_font.render(f"High Score: {self._score_manager.high_score}", True, (0, 0, 0))
        self._screen.blit(score_text, (SCREEN_WIDTH - score_text.get_width() - SCORE_POS_X_OFFSET, SCORE_POS_Y_SCORE))
        self._screen.blit(high_score_text, (SCREEN_WIDTH - high_score_text.get_width() - SCORE_POS_X_OFFSET, SCORE_POS_Y_HIGH_SCORE))
    
    def _draw_game_over_screen(self):
        """게임 오버 화면 렌더링"""
        text = self._game_over_font.render("Game Over!", True, (0, 0, 0))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + GAME_OVER_POS_Y_OFFSET))
        self._screen.blit(text, text_rect)

        restart_text = self._restart_font.render("Press SPACE to Restart", True, (0, 0, 0))
        restart_text_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + RESTART_POS_Y_OFFSET))
        self._screen.blit(restart_text, restart_text_rect)
    
    def reset(self):
        """게임 재시작 (Public)"""
        self._game_over = False
        self._game_speed = INITIAL_GAME_SPEED
        self._player.reset()
        self._obstacle_manager.clear()
        self._score_manager.reset() 
        self._is_day = True