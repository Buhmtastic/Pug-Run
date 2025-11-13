# --- 화면 설정 ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
FPS = 60
BACKGROUND_COLOR = (135, 206, 235)  # 하늘색 (공원 테마) - 초기값
DAY_BACKGROUND_COLOR = (247, 247, 247) # 밝은 회색
NIGHT_BACKGROUND_COLOR = (83, 83, 83) # 어두운 회색
GROUND_COLOR = (34, 139, 34)        # 잔디 녹색
GROUND_Y = 350                      # 지면 높이 (수정됨)

# --- 플레이어 설정 (퍼그) ---
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 30               # 퍼그는 키가 낮음
PLAYER_X = 50                    # 고정 X 위치
PLAYER_GROUND_Y = GROUND_Y - PLAYER_HEIGHT # 지면 Y 위치
PLAYER_JUMP_VELOCITY = -13       # 점프 초기 속도 (퍼그는 약간 낮게)
PLAYER_GRAVITY = 0.8             # 중력 가속도
PLAYER_DUCK_HEIGHT = 20          # 숙일 때 높이
PLAYER_COLOR = (245, 222, 179)   # 연한 갈색 (퍼그 색상)
PUG_RUN_2_COLOR = (210, 180, 140) # 퍼그 달리기 애니메이션 2번째 프레임 색상
PUG_JUMP_COLOR = (173, 216, 230)  # 퍼그 점프 색상 (하늘색)

# --- 게임 설정 ---
INITIAL_GAME_SPEED = 6           # 초기 속도
MAX_GAME_SPEED = 13              # 최대 속도
SPEED_INCREMENT = 0.001          # 속도 증가율
SCORE_INCREMENT = 1              # 프레임당 점수 증가
DAY_NIGHT_SWITCH_SCORE = 700     # 낮/밤 전환 점수

# --- UI 설정 ---
SCORE_TEXT_SIZE = 30
GAME_OVER_TEXT_SIZE = 50
RESTART_TEXT_SIZE = 30
SCORE_POS_X_OFFSET = 10
SCORE_POS_Y_SCORE = 10
SCORE_POS_Y_HIGH_SCORE = 40
GAME_OVER_POS_Y_OFFSET = -20
RESTART_POS_Y_OFFSET = 30


# --- 장애물 설정 (공원 테마) ---
OBSTACLE_SPAWN_MIN_GAP = 200     # 최소 장애물 간격
OBSTACLE_SPAWN_MAX_GAP = 400     # 최대 장애물 간격

# 소화전
HYDRANT_WIDTH = 25
HYDRANT_HEIGHT = 35
HYDRANT_COLOR = (220, 20, 60)    # 빨간색

# 나무 그루터기
STUMP_WIDTH = 30
STUMP_HEIGHT = 25
STUMP_COLOR = (139, 69, 19)      # 갈색

# 새/나비 (공중 장애물)
BIRD_WIDTH = 35
BIRD_HEIGHT = 25
BIRD_COLOR = (128, 128, 128)     # 회색
BIRD_Y_POSITIONS = [260, 280, 300]  # 새 가능 높이
