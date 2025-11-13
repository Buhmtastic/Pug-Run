# Pug Run 게임 개발 기획서

## 프로젝트 개요

**게임명**: Pug Run (퍼그 런)  
**장르**: 무한 러너 (Endless Runner)  
**플랫폼**: PC (Python/PyGame)  
**개발 기간**: 5주  
**개발 목적**: 포트폴리오용 게임 개발 프로젝트  
**개발 방법론**: **객체지향 프로그래밍(OOP) 원칙 엄격 준수** ⚠️

**컨셉**: 공원을 자유롭게 뛰어다니는 귀여운 퍼그가 장애물을 피하며 최대한 멀리 달리는 게임

---

## ⚠️ 필수 개발 원칙: 객체지향 프로그래밍 (OOP)

### 중요도: 🔴 CRITICAL - 준수하지 않으면 프로젝트 실패

본 프로젝트는 **객체지향 프로그래밍(OOP) 원칙을 엄격히 준수**하여 개발해야 합니다.

**이유**:
- 코드 유지보수성 향상
- 확장 가능한 구조
- 전문적인 개발 역량 증명
- 포트폴리오 품질 보증

**적용 원칙**:
1. ✅ **캡슐화(Encapsulation)**: 데이터와 메서드를 클래스 내부에 은닉
2. ✅ **상속(Inheritance)**: 공통 기능을 부모 클래스로 추상화
3. ✅ **다형성(Polymorphism)**: 동일 인터페이스로 다양한 객체 처리
4. ✅ **추상화(Abstraction)**: 복잡한 구현 숨기고 인터페이스만 노출

**SOLID 원칙**:
- **S**ingle Responsibility: 각 클래스는 단일 책임만
- **O**pen/Closed: 확장에는 열려있고 수정에는 닫혀있게
- **L**iskov Substitution: 자식 클래스는 부모 클래스로 대체 가능
- **I**nterface Segregation: 인터페이스는 작고 구체적으로
- **D**ependency Inversion: 구체적 구현이 아닌 추상화에 의존

---

## 1. 개발 목적

- **클래식 게임 메커니즘 학습**: 2014년 Google Chrome UX 팀(Sebastien Gabriel, Alan Bettes, Edward Jung)이 개발한 Chrome Dino Game에서 영감을 받아 Python/PyGame으로 무한 러너(Endless Runner) 장르의 핵심 이해
- **독창성 추가**: 공룡 대신 **퍼그(Pug)**를 주인공으로 하여 차별화. Chrome Dino와 법적 충돌 없이 독립적 프로젝트 완성
- **게임 물리 엔진 기초 습득**: 점프 물리, 충돌 감지, 속도 증가 알고리즘 등 2D 액션 게임의 기본 메커니즘 구현 경험
- **빠른 프로토타이핑 검증**: 생성형 AI와 바이브코딩으로 단순하지만 중독성 있는 게임을 단기간에 완성하는 능력 입증
- **포트폴리오 완성도 향상**: 싱글플레이어 캐주얼 게임으로 기존 멀티플레이어 프로젝트와 차별화. 귀여운 캐릭터로 긍정적 인상

**참고**: Chrome Dino Game은 오프라인 에러 페이지의 이스터 에그로 시작하여 월 2억 7천만 회 플레이를 기록한 글로벌 히트작. Pug Run은 이 게임 메커니즘에서 영감을 받았으나, 캐릭터, 테마, 비주얼을 완전히 독창적으로 제작

## 2. 주요 기능 및 제공 가치

### 핵심 게임플레이
- **무한 러너 메커니즘**: 플레이어는 자동으로 달리는 **퍼그**를 조작하여 장애물 회피. 게임 오버 시 재시작 가능한 무한 루프
- **조작 시스템**: 
  - 스페이스바 또는 위 화살표: 점프
  - 아래 화살표: 숙이기 (새/나비 회피용)
- **장애물 종류** (공원 테마):
  - **소화전** 🚒: 지면 장애물. 점프로 회피
  - **나무 그루터기** 🪵: 다양한 크기. 점프로 회피
  - **벤치** 🪑: 긴 장애물 (선택 사항)
  - **새/나비** 🐦🦋: 공중을 나는 장애물. 숙이기 또는 점프로 회피
- **난이도 증가**: 시간 경과에 따라 퍼그의 이동 속도 점진적 증가. 장애물 출현 빈도 상승
- **점수 시스템**: 생존 시간에 비례하여 점수 증가. 하이스코어 저장 기능
- **비주얼 변화**: 일정 점수(원작 기준 700점)마다 배경이 낮→밤 또는 밤→낮으로 전환

### 캐릭터 특징 (퍼그)
- **귀여운 외모**: 짧은 다리, 동그란 몸, 표정 풍부
- **애니메이션**:
  - 달리기: 짧은 다리로 통통 뛰기
  - 점프: 귀엽게 뛰어오르기
  - 혀 내밀기: 달릴 때 혀 날름 (선택 사항)
  - 꼬리 흔들기: 게임 시작 시 (선택 사항)
- **색상**: 연한 갈색/검은색/흰색 중 선택 가능 (선택 사항)

### 제공 가치
- **즉각적 피드백**: 단순한 조작으로 누구나 쉽게 플레이 가능
- **반복 플레이 유도**: "한 번만 더" 심리를 자극하는 중독성
- **감정적 연결**: 귀여운 퍼그 캐릭터로 긍정적 감정 유발
- **집중력 훈련**: 속도 증가에 따른 순간 판단력 향상
- **레트로 감성**: 픽셀 아트 스타일로 향수 자극
- **포트폴리오 차별화**: 흔한 공룡 게임이 아닌 독창적 프로젝트

## 3. 개발 단계별 마일스톤

### Phase 1: 기본 게임 루프 (1주차)

#### 작업 항목
- [ ] 프로젝트 구조 생성 (폴더, 기본 파일)
- [ ] `config.py` 작성 (게임 상수 정의 - 퍼그 테마)
- [ ] `main.py` 작성 (게임 실행 진입점)
- [ ] `GameObject` 추상 클래스 작성 ⭐ **OOP**
  - [ ] 추상 메서드 정의 (update, draw)
  - [ ] 공통 속성 정의 (x, y, width, height)
  - [ ] get_rect() 메서드 구현
- [ ] `Game` 클래스 기본 구조
  - [ ] `__init__()`: PyGame 초기화, 화면 생성
  - [ ] `run()`: 메인 게임 루프 (FPS 60 유지)
  - [ ] `_handle_events()`: 키보드 입력 처리 (**private**)
  - [ ] `_update()`: 게임 상태 업데이트 (**private**)
  - [ ] `_draw()`: 화면 렌더링 (**private**)
- [ ] `Player` 클래스 구현 (GameObject 상속) ⭐ **OOP**
  - [ ] GameObject 상속 선언
  - [ ] super().__init__() 호출
  - [ ] Private 속성 정의 (_velocity_y, _is_jumping)
  - [ ] Public 메서드 (jump, update, draw)
  - [ ] Private 메서드 (_apply_gravity, _check_landing)
  - [ ] 중력 및 점프 물리 구현
  - [ ] 스페이스바/위 화살표로 점프
- [ ] 바닥(ground) 라인 렌더링 (잔디 녹색)
- [ ] 게임 시작/종료 이벤트 처리

#### OOP 체크리스트 ⚠️ 필수 확인
- [ ] **캡슐화**: 모든 속성이 private (_변수) 또는 protected로 선언됨
- [ ] **상속**: Player가 GameObject를 올바르게 상속함
- [ ] **추상화**: GameObject의 추상 메서드를 Player에서 구현함
- [ ] **단일 책임**: 각 클래스가 하나의 책임만 가짐
  - Game: 게임 루프 관리
  - Player: 플레이어 동작
- [ ] **명확한 인터페이스**: Public/Private 메서드 구분 명확
- [ ] **주석**: 각 클래스와 메서드에 docstring 작성

#### Definition of Done (완료 기준)
- ✅ 게임 창이 정상적으로 실행됨 (800x400, 60 FPS)
- ✅ 배경이 하늘색, 바닥이 녹색으로 표시됨 (공원 테마)
- ✅ 스페이스바 입력 시 퍼그가 점프함
- ✅ 점프 후 중력에 의해 바닥으로 복귀
- ✅ ESC 또는 창 닫기로 게임 종료 가능
- ✅ **OOP 체크리스트 모두 통과**
- ✅ 코드 리뷰: 캡슐화, 상속, 단일 책임 원칙 준수 확인

#### 예상 소요 시간
- 환경 설정: 1시간
- GameObject 추상 클래스: 1시간 ⭐ **OOP**
- Game 클래스 구조: 2시간
- Player 클래스 (상속 포함): 3시간 ⭐ **OOP**
- 점프 물리 및 테스트: 2시간
- OOP 코드 리뷰 및 리팩토링: 1시간 ⭐ **OOP**
**총 10시간**

---

### Phase 2: 장애물 시스템 (2주차)

#### 작업 항목
- [ ] `Obstacle` 추상 클래스 구현 (GameObject 상속) ⭐ **OOP**
  - [ ] GameObject 상속
  - [ ] 공통 속성 정의 (obstacle_type, speed)
  - [ ] 공통 메서드 (update, is_off_screen)
  - [ ] 추상 메서드 (draw) - 자식 클래스에서 구현
  - [ ] get_rect() 오버라이드
- [ ] `Hydrant` 클래스 (Obstacle 상속) ⭐ **OOP - 다형성**
  - [ ] Obstacle 상속
  - [ ] 생성자에서 super().__init__() 호출
  - [ ] draw() 메서드 구현 (소화전 스타일)
  - [ ] 빨간색 렌더링
- [ ] `Stump` 클래스 (Obstacle 상속) ⭐ **OOP - 다형성**
  - [ ] Obstacle 상속
  - [ ] draw() 메서드 구현 (나무 스타일)
  - [ ] 갈색 렌더링
- [ ] `ObstacleManager` 클래스 ⭐ **OOP - Factory Pattern**
  - [ ] Private 속성 (_obstacles 리스트)
  - [ ] Public 메서드 (update, draw, check_collision, clear)
  - [ ] Private 메서드 (_spawn_obstacle_if_needed, _create_random_obstacle)
  - [ ] Factory Pattern으로 장애물 생성
  - [ ] 무작위 장애물 타입 선택
  - [ ] 화면 밖 장애물 제거
- [ ] 충돌 감지 시스템
  - [ ] ObstacleManager.check_collision(player) 구현
  - [ ] pygame.Rect.colliderect() 활용
  - [ ] 충돌 시 게임 오버 플래그 설정
- [ ] 게임 오버 화면
  - [ ] "Game Over" 텍스트 표시
  - [ ] 최종 점수 표시
  - [ ] 스페이스바로 재시작 안내
- [ ] 게임 재시작 기능
  - [ ] Game.reset() 메서드 구현
  - [ ] Player.reset() 호출
  - [ ] ObstacleManager.clear() 호출
  - [ ] 점수 및 속도 초기화

#### OOP 체크리스트 ⚠️ 필수 확인
- [ ] **상속 구조**: Obstacle → Hydrant, Stump 상속 관계 올바름
- [ ] **다형성**: ObstacleManager가 Obstacle 리스트로 다양한 타입 처리
- [ ] **캡슐화**: ObstacleManager의 _obstacles 리스트 직접 접근 불가
- [ ] **Factory Pattern**: _create_random_obstacle()로 객체 생성 캡슐화
- [ ] **단일 책임**: 
  - Obstacle: 장애물 동작
  - ObstacleManager: 장애물 관리
  - Game: 흐름 제어
- [ ] **추상화**: Obstacle의 draw()가 추상 메서드로 정의됨
- [ ] **의존성 역전**: Game이 구체적 장애물이 아닌 ObstacleManager에 의존

#### Definition of Done
- ✅ 화면 오른쪽에서 소화전/나무가 생성됨
- ✅ 장애물이 일정 속도로 왼쪽으로 이동
- ✅ 장애물과 퍼그 충돌 시 게임 오버
- ✅ 게임 오버 시 "Game Over" 화면 표시
- ✅ 스페이스바로 게임 재시작 가능
- ✅ 장애물이 무작위 간격으로 생성됨
- ✅ 장애물이 공원 테마에 어울림
- ✅ **OOP 체크리스트 모두 통과**
- ✅ 코드 리뷰: 상속, 다형성, Factory Pattern 확인

#### 예상 소요 시간
- Obstacle 추상 클래스: 2시간 ⭐ **OOP**
- Hydrant, Stump 클래스: 2시간 ⭐ **OOP**
- ObstacleManager (Factory): 3시간 ⭐ **OOP**
- 충돌 감지: 2시간
- 게임 오버/재시작: 2시간
- OOP 코드 리뷰 및 리팩토링: 2시간 ⭐ **OOP**
**총 13시간**

---

### Phase 3: 고급 기능 (3주차)

#### 작업 항목
- [ ] `Bird` 클래스 (Obstacle 상속) ⭐ **OOP - 다형성**
  - [ ] Obstacle 상속
  - [ ] 공중을 나는 장애물
  - [ ] 3가지 높이 중 무작위 선택
  - [ ] draw() 메서드 구현 (새 스타일)
  - [ ] 날갯짓 애니메이션 (선택 사항)
- [ ] 숙이기(Duck) 기능 - Player 클래스 확장
  - [ ] duck() 메서드 구현
  - [ ] stand_up() 메서드 구현
  - [ ] 아래 화살표 입력 감지
  - [ ] 퍼그 높이 변경 (30px → 20px)
  - [ ] Private 속성 (_is_ducking) 추가
  - [ ] 히트박스 크기 동적 조정
  - [ ] 키를 떼면 원래 크기로 복귀
- [ ] `ScoreManager` 클래스 생성 ⭐ **OOP - 단일 책임**
  - [ ] Private 속성 (_score, _high_score, _score_file)
  - [ ] add_score(amount) 메서드
  - [ ] reset() 메서드
  - [ ] Property로 score, high_score 노출
  - [ ] Private 메서드 (_load_high_score, _save_high_score)
  - [ ] 파일 I/O 캡슐화
  - [ ] 하이스코어 파일 저장 (`data/highscore.txt`)
  - [ ] 하이스코어 불러오기 및 표시
- [ ] 난이도 증가 로직 - Game 클래스에 추가
  - [ ] Private 메서드 (_increase_difficulty)
  - [ ] 점수 증가에 따른 게임 속도 증가
  - [ ] 최대 속도 제한 (MAX_GAME_SPEED)
  - [ ] 장애물 출현 빈도 증가 (선택 사항)
- [ ] ObstacleManager Factory 확장
  - [ ] _create_random_obstacle()에 Bird 타입 추가
  - [ ] 소화전/나무/새 중 무작위 생성
  - [ ] 일정 점수 이상에서만 새 출현 (선택)
- [ ] Game 클래스 리팩토링
  - [ ] ScoreManager 의존성 주입
  - [ ] 점수 로직을 ScoreManager에 위임

#### OOP 체크리스트 ⚠️ 필수 확인
- [ ] **단일 책임 원칙**: ScoreManager가 점수 관리만 담당
- [ ] **개방-폐쇄 원칙**: 새 장애물 추가 시 기존 코드 수정 최소화
- [ ] **다형성**: Bird가 Obstacle로 처리됨
- [ ] **캡슐화**: ScoreManager의 파일 I/O가 private 메서드로 숨김
- [ ] **의존성 주입**: Game이 ScoreManager를 생성자에서 받음 (선택)
- [ ] **Property 패턴**: ScoreManager.score가 읽기 전용
- [ ] **리팩토링**: 중복 코드 제거, 메서드 분리

#### Definition of Done
- ✅ 아래 화살표로 숙이기 가능
- ✅ 새 장애물이 공중에 나타남
- ✅ 화면에 점수가 표시됨
- ✅ 게임 오버 시 하이스코어 저장
- ✅ 시간이 지날수록 게임 속도 증가
- ✅ 소화전/나무/새가 번갈아 나타남
- ✅ **OOP 체크리스트 모두 통과**
- ✅ 코드 리뷰: 단일 책임, 캡슐화, 다형성 확인

#### 예상 소요 시간
- Bird 클래스: 2시간 ⭐ **OOP**
- 숙이기 기능: 2시간
- ScoreManager 클래스: 3시간 ⭐ **OOP**
- 난이도 증가: 2시간
- Factory 확장: 1시간
- OOP 리팩토링: 2시간 ⭐ **OOP**
- 통합 테스트: 1시간
**총 13시간**

---

### Phase 4: 비주얼 및 사운드 (4주차)

#### 작업 항목
- [ ] **캐릭터 디자인 최종 확정 (법적 리스크 최소화)** ⚖️
  - [ ] Chrome Dino와 시각적으로 명확히 구분되는지 확인
  - [ ] 색상, 비율, 스타일 차별화
  - [ ] 오픈소스 에셋 사용 시 라이선스 확인 (CC0 권장)
  - [ ] 팀원 또는 외부인에게 "Chrome Dino 같아 보이나요?" 질문
- [ ] 낮/밤 모드 전환
  - [ ] 일정 점수(700점)마다 배경색 변경
  - [ ] 낮: 밝은 회색 (247, 247, 247)
  - [ ] 밤: 어두운 회색 (83, 83, 83)
  - [ ] 부드러운 전환 효과 (선택 사항)
- [ ] 픽셀 아트 스프라이트 제작 또는 수집
  - [ ] **방법 A**: 자체 디자인 (퍼그 테마)
    - 퍼그 달리기 애니메이션 (2~3 프레임)
    - 퍼그 점프 스프라이트
    - 퍼그 숙이기 스프라이트
    - 혀 내밀기 애니메이션 (선택 사항)
    - 소화전 스프라이트 (2~3종류)
    - 나무 그루터기 스프라이트
    - 새 날갯짓 애니메이션 (2 프레임)
  - [ ] **방법 B**: 오픈소스 에셋 (Kenney.nl, OpenGameArt.org)
    - "dog sprite", "pug pixel art" 검색
    - "park obstacles" 검색
    - CC0 라이선스 에셋 선택
    - 필요시 색상/크기 수정
  - [ ] 바닥 텍스처 (잔디)
- [ ] `AssetManager` 클래스 생성 ⭐ **OOP - 단일 책임**
  - [ ] Private 속성 (_images, _sounds 딕셔너리)
  - [ ] load_image(name, path) 메서드
  - [ ] get_image(name) 메서드
  - [ ] load_sound(name, path) 메서드 (선택)
  - [ ] play_sound(name) 메서드 (선택)
  - [ ] 에러 처리 및 기본값 제공
  - [ ] 리소스 캐싱 (메모리 효율)
- [ ] `AnimationController` 클래스 ⭐ **OOP - 상태 패턴**
  - [ ] Private 속성 (_frames, _current_frame, _frame_time)
  - [ ] add_animation(name, frames, fps) 메서드
  - [ ] play(name) 메서드
  - [ ] update(delta_time) 메서드
  - [ ] get_current_frame() 메서드
  - [ ] 애니메이션 상태 캡슐화
- [ ] Player 클래스 리팩토링
  - [ ] AssetManager 의존성 주입
  - [ ] AnimationController 통합
  - [ ] draw() 메서드 수정 (스프라이트 렌더링)
  - [ ] _get_current_sprite() private 메서드
  - [ ] 상태별 애니메이션 전환 (running/jumping/ducking)
- [ ] Obstacle 하위 클래스 스프라이트 적용
  - [ ] Hydrant, Stump, Bird에 AssetManager 사용
  - [ ] draw() 메서드 수정
  - [ ] 이미지 로딩 실패 시 기본 도형으로 대체 (Fallback)
- [ ] 사운드 효과 (선택 사항)
  - [ ] AssetManager를 통한 사운드 로딩
  - [ ] 점프 사운드
  - [ ] 게임 오버 사운드
  - [ ] BGM (무한 반복)
- [ ] 시작 화면 (선택 사항)
  - [ ] 게임 제목 표시
  - [ ] "Press SPACE to Start" 안내
  - [ ] 간단한 조작 설명

#### OOP 체크리스트 ⚠️ 필수 확인
- [ ] **단일 책임**: AssetManager는 리소스 로딩만 담당
- [ ] **캡슐화**: 파일 경로, 로딩 로직이 AssetManager에 숨김
- [ ] **에러 처리**: 리소스 없을 때 기본값 제공 또는 예외 처리
- [ ] **의존성 주입**: Player, Obstacle이 AssetManager를 주입받음
- [ ] **상태 패턴**: AnimationController가 애니메이션 상태 관리
- [ ] **Fallback 패턴**: 이미지 로딩 실패 시 도형으로 대체
- [ ] **메모리 관리**: 리소스 중복 로딩 방지 (캐싱)

#### Definition of Done
- ✅ 점수에 따라 배경색이 변경됨
- ✅ 플레이어가 픽셀 아트로 표시됨
- ✅ **캐릭터가 Chrome Dino와 명확히 구분됨** ⚖️
- ✅ 달리기 애니메이션이 자연스러움
- ✅ 장애물이 스프라이트로 렌더링됨
- ✅ (선택) 점프/충돌 사운드 재생
- ✅ 전체적인 비주얼이 완성도 있음
- ✅ **OOP 체크리스트 모두 통과**
- ✅ 코드 리뷰: AssetManager 단일 책임, 의존성 주입 확인

#### 예상 소요 시간
- **캐릭터 디자인 확정**: 2시간
- 낮/밤 전환: 2시간
- 스프라이트 제작/수집: 4시간
- AssetManager 클래스: 3시간 ⭐ **OOP**
- AnimationController 클래스: 2시간 ⭐ **OOP** (선택)
- Player/Obstacle 스프라이트 통합: 3시간
- 사운드 통합: 2시간 (선택)
- OOP 리팩토링: 1시간 ⭐ **OOP**
**총 19시간 (선택 사항 포함 시 23시간)**

---

### Phase 5: 테스트 및 배포 (5주차)

#### 작업 항목
- [ ] 난이도 밸런싱
  - [ ] 초보자 테스트 (100점 도달 가능 여부)
  - [ ] 점프 타이밍 조정
  - [ ] 장애물 간격 조정
  - [ ] 속도 증가 곡선 최적화
- [ ] 버그 수정
  - [ ] 충돌 감지 오류 수정
  - [ ] 점프 중 다시 점프 방지
  - [ ] 화면 밖 장애물 메모리 누수 확인
  - [ ] 게임 오버 후 입력 무시 확인
- [ ] 예외 처리
  - [ ] 하이스코어 파일 없을 때 처리
  - [ ] 이미지 파일 로딩 실패 처리
  - [ ] 사운드 파일 없을 때 처리
- [ ] **OOP 코드 품질 최종 점검** ⭐ **CRITICAL**
  - [ ] 모든 클래스가 단일 책임 원칙 준수
  - [ ] Private/Protected/Public 접근 제어 올바름
  - [ ] 상속 관계가 논리적으로 타당함
  - [ ] 다형성이 올바르게 활용됨
  - [ ] 캡슐화가 충분히 이루어짐
  - [ ] 의존성 주입이 적절히 사용됨
  - [ ] 매직 넘버가 config.py 상수로 이동
  - [ ] Docstring이 모든 클래스/메서드에 존재
  - [ ] 명확한 메서드/변수 이름 사용
  - [ ] 중복 코드 제거 완료
- [ ] 코드 리뷰 체크리스트 ⭐ **OOP**
  - [ ] `GameObject` 추상 클래스 올바르게 구현됨
  - [ ] `Player`, `Obstacle` 상속 구조 올바름
  - [ ] `ObstacleManager` Factory Pattern 적용 확인
  - [ ] `ScoreManager` 단일 책임 준수
  - [ ] `AssetManager` 리소스 캡슐화 확인
  - [ ] `Game` 클래스가 적절히 의존성 관리
  - [ ] 모든 Manager 클래스들이 독립적
- [ ] 문서화
  - [ ] README.md 작성
    - [ ] 게임 소개
    - [ ] OOP 설계 원칙 강조 ⭐
    - [ ] 클래스 다이어그램 (선택)
    - [ ] 설치 방법
    - [ ] 실행 방법
    - [ ] 조작 방법
    - [ ] 스크린샷
  - [ ] requirements.txt 작성
  - [ ] 라이선스 파일 추가 (MIT 권장)
  - [ ] 개발 과정 회고 (선택)
- [ ] 최종 테스트
  - [ ] 모든 Phase의 Definition of Done 재확인
  - [ ] OOP 체크리스트 100% 통과 확인
  - [ ] 다양한 환경에서 실행 테스트

#### OOP 최종 점검 체크리스트 ⚠️ 필수 확인
- [ ] **클래스 설계**:
  - [ ] 모든 클래스가 명확한 책임을 가짐
  - [ ] 클래스 간 결합도가 낮음
  - [ ] 각 클래스의 응집도가 높음
- [ ] **캡슐화**:
  - [ ] 모든 속성이 private (_변수) 또는 protected
  - [ ] Public 인터페이스만 외부 노출
  - [ ] Property를 통한 제어된 접근
- [ ] **상속과 다형성**:
  - [ ] 상속 관계가 is-a 관계를 만족
  - [ ] 추상 클래스/메서드가 적절히 사용됨
  - [ ] 자식 클래스가 부모 클래스로 대체 가능 (LSP)
- [ ] **설계 패턴**:
  - [ ] Factory Pattern (ObstacleManager)
  - [ ] Singleton Pattern (AssetManager, 선택 사항)
  - [ ] Strategy Pattern (AnimationController, 선택 사항)
- [ ] **코드 품질**:
  - [ ] 매직 넘버 없음 (모두 상수로)
  - [ ] 중복 코드 없음
  - [ ] 긴 메서드 리팩토링 완료 (15줄 이하 권장)
  - [ ] 복잡한 조건문 메서드로 분리

#### Definition of Done
- ✅ 게임이 안정적으로 작동함
- ✅ 난이도가 적절히 밸런싱됨
- ✅ 모든 예외 상황이 처리됨
- ✅ README.md가 완성됨
- ✅ **OOP 최종 점검 체크리스트 100% 통과** ⭐
- ✅ 코드 리뷰 완료 및 승인
- ✅ 포트폴리오로 제출 가능한 품질

#### 예상 소요 시간
- 난이도 밸런싱: 3시간
- 버그 수정: 3시간
- 예외 처리: 2시간
- **OOP 코드 품질 점검**: 4시간 ⭐ **CRITICAL**
- **OOP 코드 리뷰 및 리팩토링**: 3시간 ⭐ **CRITICAL**
- 문서화: 3시간
- 최종 테스트: 2시간
**총 20시간**

---
- [ ] 배포 준비
  - [ ] GitHub 저장소 생성 및 업로드
  - [ ] .gitignore 작성
  - [ ] 실행 파일 빌드 (PyInstaller, 선택)
  - [ ] 릴리즈 노트 작성

#### Definition of Done
- ✅ 게임을 10회 플레이하여 버그 없음 확인
- ✅ 초보자가 100점을 달성할 수 있음
- ✅ README.md가 완성됨
- ✅ GitHub에 업로드됨
- ✅ 다른 PC에서 실행 테스트 완료
- ✅ 게임 플레이 영상 녹화 (선택)

#### 예상 소요 시간
- 밸런싱 및 플레이테스트: 4시간
- 버그 수정: 3시간
- 코드 정리: 2시간
- 문서화: 3시간
- 배포 준비: 2시간
**총 14시간**

---

## 10. 테스트 체크리스트

### 기능 테스트
- [ ] 게임이 정상적으로 실행됨
- [ ] 스페이스바/위 화살표로 점프 가능
- [ ] 아래 화살표로 숙이기 가능
- [ ] 소화전과 충돌 시 게임 오버
- [ ] 나무와 충돌 시 게임 오버
- [ ] 새와 충돌 시 게임 오버
- [ ] 점수가 정상적으로 증가
- [ ] 하이스코어가 저장되고 불러와짐
- [ ] 게임 속도가 점진적으로 증가
- [ ] 낮/밤 모드가 전환됨
- [ ] 게임 오버 후 재시작 가능
- [ ] ESC로 게임 종료 가능

### OOP 설계 테스트 ⭐ 필수
- [ ] **클래스 독립성**: 각 클래스를 독립적으로 테스트 가능
- [ ] **상속 관계**: Player가 GameObject로 타입 캐스팅 가능
- [ ] **다형성**: ObstacleManager가 모든 Obstacle 타입 처리
- [ ] **캡슐화**: Private 속성에 직접 접근 불가능 (외부에서)
- [ ] **Factory Pattern**: ObstacleManager가 다양한 장애물 생성
- [ ] **의존성 주입**: Game이 Player/ObstacleManager 교체 가능
- [ ] **단일 책임**: 각 클래스 수정 시 다른 클래스 영향 최소화
- [ ] **인터페이스 일관성**: 같은 이름의 메서드가 같은 동작 수행

### 코드 품질 테스트
- [ ] **Docstring**: 모든 클래스와 public 메서드에 존재
- [ ] **명명 규칙**: 
  - [ ] 클래스명은 PascalCase (예: GameObject)
  - [ ] 메서드명은 snake_case (예: get_rect)
  - [ ] Private 변수는 _underscore (예: _velocity)
  - [ ] 상수는 UPPER_CASE (예: SCREEN_WIDTH)
- [ ] **매직 넘버**: 코드에 숫자 직접 사용 안 함 (config.py 사용)
- [ ] **중복 코드**: 같은 로직이 2번 이상 반복되지 않음
- [ ] **메서드 길이**: 대부분의 메서드가 15줄 이하
- [ ] **복잡도**: 중첩 if문이 3단계 이상 없음

### 엣지 케이스 테스트
- [ ] 점프 중 다시 점프 시도 → 무시됨
- [ ] 숙이는 중 점프 시도 → 정상 작동
- [ ] 장애물이 겹쳐서 생성되지 않음
- [ ] 점수가 99999를 초과해도 오류 없음
- [ ] 하이스코어 파일이 없어도 게임 실행됨
- [ ] 연속으로 빠르게 재시작해도 문제없음

### 성능 테스트
- [ ] FPS가 60으로 유지됨
- [ ] 메모리 사용량이 일정함 (누수 없음)
- [ ] 1분 이상 플레이 시 렉 없음
- [ ] 장애물 100개 이상 생성 시에도 안정적

### 사용자 경험 테스트
- [ ] 초보자가 조작법을 직관적으로 이해
- [ ] 게임 오버 이유가 명확함
- [ ] 재시작이 빠르고 부드러움
- [ ] 하이스코어 갱신 시 만족감 제공

---

## 11. Git 브랜치 전략

### 브랜치 구조
```
main (또는 master)
├── develop
│   ├── feature/game-loop
│   ├── feature/player-jump
│   ├── feature/obstacles
│   ├── feature/collision
│   ├── feature/scoring
│   ├── feature/graphics
│   └── feature/sounds
└── hotfix/[버그명]
```

### 브랜치 규칙
- **main**: 배포 가능한 안정 버전만 유지
- **develop**: 개발 중인 최신 코드
- **feature/**: 각 기능별 브랜치 (Phase별로 생성)
- **hotfix/**: 긴급 버그 수정

### 커밋 메시지 규칙
```
[타입] 제목

본문 (선택)

예시:
[feat] Add player jump physics
[fix] Fix collision detection bug
[refactor] Improve obstacle manager code
[docs] Update README with installation guide
[test] Add unit tests for player class
```

### 작업 흐름
1. develop에서 feature 브랜치 생성
2. 기능 개발 및 커밋
3. develop으로 merge (Pull Request)
4. Phase 완료 시 develop → main merge
5. main에 태그 추가 (v0.1.0, v0.2.0 등)

---

## 12. 개발 회의 안건

### 킥오프 미팅 (Phase 1 시작 전)
- [ ] 개발기획서 리뷰
- [ ] 역할 분담 (1인 개발 시 Skip)
- [ ] 개발 환경 설정 확인
- [ ] Git 저장소 생성
- [ ] 첫 주 목표 확인

### 주간 체크인 (매주 월요일)
- [ ] 지난 주 완료 항목 리뷰
- [ ] 이번 주 목표 설정
- [ ] 막힌 부분 논의
- [ ] 일정 조정 필요성 검토

### Phase 완료 리뷰 (각 Phase 종료 시)
- [ ] Definition of Done 달성 여부 확인
- [ ] 다음 Phase 준비사항 점검
- [ ] 배운 점 / 개선점 정리

### 최종 리뷰 (Phase 5 완료 후)
- [ ] 전체 프로젝트 회고
- [ ] 성공 요인 / 실패 요인 분석
- [ ] 다음 프로젝트 아이디어 논의

---

## 13. 리스크 관리 계획

### 높은 우선순위 리스크

| 리스크 | 발생 확률 | 영향도 | 대응 방안 |
|--------|----------|--------|----------|
| 점프 물리가 부자연스러움 | 중 | 높음 | 여러 설정값으로 반복 테스트. 레퍼런스 게임과 비교 |
| 충돌 감지 정확도 낮음 | 중 | 높음 | 히트박스 크기 조정. 픽셀 퍼펙트 대신 여유 공간 |
| 난이도 밸런싱 실패 | 높음 | 중 | 여러 사람에게 플레이테스트 요청. 통계 수집 |
| 개발 일정 지연 | 중 | 중 | Phase 4(그래픽)를 선택 사항으로 조정 |

### 중간 우선순위 리스크

| 리스크 | 발생 확률 | 영향도 | 대응 방안 |
|--------|----------|--------|----------|
| 스프라이트 제작 시간 부족 | 중 | 낮음 | 무료 픽셀 아트 에셋 활용. 간단한 도형으로 대체 |
| 성능 이슈 (FPS 저하) | 낮음 | 중 | 장애물 수 제한. 이미지 캐싱 적용 |
| 크로스 플랫폼 호환성 | 낮음 | 낮음 | Windows에서 우선 개발. 타 OS는 추후 테스트 |

---
- 난이도 밸런싱 (초보자도 즐길 수 있도록)
- 버그 수정 및 예외 처리
- README 작성 및 플레이 가이드
- GitHub 업로드 및 실행 파일 빌드

## 4. 전체 일정(타임라인)

### 주차별 상세 일정

| 주차 | 단계 | 주요 산출물 | 예상 시간 | 핵심 작업 | 완료 기준 |
|------|------|-------------|----------|----------|----------|
| 1주차 | Phase 1 | 플레이 가능한 프로토타입 | 10시간 | 점프 물리 구현 | 공룡이 점프하고 착지함 |
| 2주차 | Phase 2 | 장애물 시스템 완성 | 13시간 | 충돌 감지, 게임 오버 | 선인장 회피 가능, 재시작 가능 |
| 3주차 | Phase 3 | 완전한 게임플레이 | 13시간 | 점수, 난이도 증가 | 점수 저장, 속도 증가 |
| 4주차 | Phase 4 | 그래픽 및 사운드 | 15시간 | 스프라이트 적용 | 비주얼 완성도 향상 |
| 5주차 | Phase 5 | 최종 배포 버전 | 14시간 | 테스트, 문서화 | GitHub 배포 완료 |

**총 개발 기간**: 5주  
**총 예상 시간**: 65시간 (주당 13시간 평균)

### 일일 작업 계획 예시 (Phase 1 - 1주차)

#### Day 1 (3시간) - 프로젝트 설정
- [ ] Python/PyGame 개발 환경 설정
- [ ] Git 저장소 생성 및 초기 커밋
- [ ] 프로젝트 폴더 구조 생성
- [ ] config.py 작성
- [ ] main.py 기본 구조

#### Day 2 (2시간) - 게임 루프
- [ ] Game 클래스 기본 구조
- [ ] 메인 게임 루프 (FPS 60)
- [ ] 배경 렌더링

#### Day 3 (3시간) - 플레이어 기본
- [ ] Player 클래스 생성
- [ ] 플레이어 사각형 렌더링
- [ ] 키보드 입력 처리

#### Day 4 (2시간) - 점프 물리 (1/2)
- [ ] 중력 가속도 구현
- [ ] 점프 초기 속도 설정
- [ ] 착지 판정

#### Day 5 (2시간) - 점프 물리 (2/2)
- [ ] 점프 타이밍 조정
- [ ] 테스트 및 미세 조정
- [ ] Phase 1 완료 확인

### 주간 마일스톤

**Week 1 목표**: "공룡이 점프한다"
- 성공 지표: 팀원이 게임을 실행하고 점프를 테스트할 수 있음

**Week 2 목표**: "장애물을 피할 수 있다"
- 성공 지표: 5분 이상 플레이 가능, 게임 오버 후 재시작

**Week 3 목표**: "점수를 경쟁할 수 있다"
- 성공 지표: 하이스코어 저장, 속도 증가 체감

**Week 4 목표**: "보기 좋은 게임이다"
- 성공 지표: 스크린샷이 포트폴리오에 쓸 만함

**Week 5 목표**: "배포 가능한 게임이다"
- 성공 지표: GitHub에 업로드, README 완성

---

## 14. 참고 자료 및 도구

### 필수 학습 자료
- **PyGame 공식 문서**: https://www.pygame.org/docs/
- **PyGame 튜토리얼**: https://www.pygame.org/wiki/tutorials
- **게임 개발 기초 (YouTube)**: "PyGame Tutorial" 검색

### 충돌 감지 참고
- PyGame Rect.colliderect() 문서
- AABB (Axis-Aligned Bounding Box) 개념

### 픽셀 아트 리소스 (무료)
- **OpenGameArt.org**: https://opengameart.org/
- **itch.io Free Assets**: https://itch.io/game-assets/free
- **Kenney.nl**: https://kenney.nl/assets (추천)

### 사운드 효과 (무료)
- **Freesound.org**: https://freesound.org/
- **OpenGameArt.org Audio**: 효과음 검색

### 개발 도구
- **Visual Studio Code**: 코드 에디터
  - 추천 확장: Python, Pylance
- **Git**: 버전 관리
- **GitHub Desktop**: Git GUI (선택)
- **PyInstaller**: 실행 파일 빌드 (선택)
  ```bash
  pip install pyinstaller
  pyinstaller --onefile main.py
  ```

### Chrome Dino Game 분석
- **소스코드**: Chromium 프로젝트에서 검색 (참고용)
- **게임 플레이**: chrome://dino (크롬 브라우저)
- **개발자 인터뷰**: https://blog.google/products/chrome/chrome-dino/

---

## 15. 성공 지표 (KPI)

### 개발 프로세스 지표
- [ ] 각 Phase를 예정된 주차 내에 완료
- [ ] 주간 커밋 수 5회 이상
- [ ] Definition of Done 100% 달성
- [ ] 코드 리뷰 (자체 또는 AI) 수행

### 게임 품질 지표
- [ ] 초보자 플레이테스트 10회 중 8회 이상 100점 도달
- [ ] 버그 발생률 < 5% (플레이 100회 중 버그 5회 이하)
- [ ] FPS 60 유지율 > 95%
- [ ] 게임 오버 후 재시작 시간 < 2초

### 학습 목표 달성
- [ ] PyGame 기본 구조 이해
- [ ] 게임 물리 엔진 구현 경험
- [ ] 충돌 감지 알고리즘 습득
- [ ] Git 버전 관리 능숙도 향상
- [ ] AI 보조 개발 워크플로우 확립

---

## 5. 기술 스택 및 개발 환경

### 필수 요구사항
- **Python**: 3.8 이상 (3.10 권장)
- **PyGame**: 2.5.0 이상
- **운영체제**: Windows 10/11, macOS 10.14+, Linux (Ubuntu 20.04+)

### 개발 도구
- **IDE**: VSCode (권장), PyCharm Community
- **버전 관리**: Git 2.30+
- **패키지 관리**: pip 또는 conda

### 필수 라이브러리
```
pygame>=2.5.0
```

### 선택 라이브러리 (Phase 4+)
```
pygame-menu>=4.4.0  # 메뉴 UI (선택)
```

### 개발 환경 설정
```bash
# 가상환경 생성 (권장)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt

# 게임 실행
python main.py
```

---

## 6. 프로젝트 구조

```
pugrun/                     # 프로젝트 루트 (dinorun → pugrun)
├── main.py                 # 게임 실행 진입점
├── game.py                 # 게임 메인 로직 클래스
├── player.py               # 퍼그(플레이어) 클래스
├── obstacle.py             # 장애물 클래스 (소화전, 나무, 새 등)
├── config.py               # 게임 설정 상수
├── utils.py                # 유틸리티 함수
├── requirements.txt        # 의존성 목록
├── README.md              # 프로젝트 설명
├── assets/                # 게임 리소스
│   ├── images/           # 스프라이트 이미지
│   │   ├── pug_run.png   # 퍼그 달리기
│   │   ├── pug_jump.png  # 퍼그 점프
│   │   ├── pug_duck.png  # 퍼그 숙이기
│   │   ├── hydrant.png   # 소화전
│   │   ├── stump.png     # 나무 그루터기
│   │   └── bird.png      # 새
│   └── sounds/           # 사운드 효과 (선택)
│       ├── jump.wav
│       ├── bark.wav      # 짖는 소리 (선택)
│       └── game_over.wav
├── data/                  # 게임 데이터
│   └── highscore.txt     # 하이스코어 저장
└── tests/                 # 테스트 코드 (선택)
    ├── test_player.py
    └── test_collision.py
```

---

## 7. 핵심 클래스 설계 (OOP 원칙 적용)

### 🔴 OOP 설계 필수 준수사항

**모든 클래스는 다음 원칙을 반드시 따라야 함**:
1. **단일 책임 원칙(SRP)**: 각 클래스는 하나의 책임만 가짐
2. **캡슐화**: private 속성(_변수명), public 메서드로 접근
3. **상속 구조**: 공통 기능은 부모 클래스로 추상화
4. **명확한 인터페이스**: 외부에서 호출할 메서드만 public으로

---

### 7.1 Game 클래스 (게임 총괄)
**책임**: 게임 전체 흐름 관리 (단일 책임)

```python
class Game:
    """
    게임 전체 생명주기 관리
    - 게임 루프
    - 상태 관리
    - 객체 간 상호작용 조율
    """
    
    def __init__(self):
        """게임 초기화"""
        self._screen = None          # private: 화면 객체
        self._clock = None            # private: FPS 관리
        self._running = False         # private: 게임 실행 상태
        self._game_over = False       # private: 게임 오버 상태
        
        # 게임 객체들 (의존성 주입 가능)
        self._player = None           # Player 객체
        self._obstacle_manager = None # ObstacleManager 객체
        self._score = 0               # private: 점수
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
    
    # Private 메서드 (내부 구현)
    def _handle_events(self):
        """입력 처리 (캡슐화)"""
        pass
    
    def _update(self):
        """게임 상태 업데이트 (캡슐화)"""
        if not self._game_over:
            self._player.update()
            self._obstacle_manager.update(self._game_speed)
            self._check_collision()
            self._update_score()
            self._increase_difficulty()
    
    def _draw(self):
        """화면 렌더링 (캡슐화)"""
        self._screen.fill(BACKGROUND_COLOR)
        self._player.draw(self._screen)
        self._obstacle_manager.draw(self._screen)
        self._draw_score()
    
    def _check_collision(self):
        """충돌 검사 (내부 로직)"""
        if self._obstacle_manager.check_collision(self._player):
            self._game_over = True
    
    def reset(self):
        """게임 재시작 (Public)"""
        self._game_over = False
        self._score = 0
        self._game_speed = INITIAL_GAME_SPEED
        self._player.reset()
        self._obstacle_manager.clear()
```

**OOP 원칙 적용**:
- ✅ **캡슐화**: 내부 상태는 `_변수`로 private 처리
- ✅ **단일 책임**: 게임 흐름만 관리, 렌더링/물리는 각 객체에 위임
- ✅ **명확한 인터페이스**: `run()`, `reset()` 만 public

---

### 7.2 GameObject 추상 클래스 (부모 클래스)
**책임**: 모든 게임 객체의 공통 기능 정의

```python
from abc import ABC, abstractmethod

class GameObject(ABC):
    """
    모든 게임 객체의 추상 부모 클래스
    - 위치, 크기 관리
    - 렌더링 인터페이스
    - 충돌 박스 제공
    """
    
    def __init__(self, x, y, width, height):
        self._x = x              # protected: 자식 클래스 접근 가능
        self._y = y
        self._width = width
        self._height = height
    
    # 추상 메서드 (자식 클래스 필수 구현)
    @abstractmethod
    def update(self):
        """상태 업데이트 (자식 클래스에서 구현)"""
        pass
    
    @abstractmethod
    def draw(self, screen):
        """화면 렌더링 (자식 클래스에서 구현)"""
        pass
    
    # 공통 메서드
    def get_rect(self):
        """충돌 감지용 Rect 반환"""
        return pygame.Rect(self._x, self._y, self._width, self._height)
    
    # Getter/Setter (캡슐화)
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
```

**OOP 원칙 적용**:
- ✅ **추상화**: 공통 인터페이스 정의
- ✅ **상속**: 자식 클래스에서 구체적 구현
- ✅ **캡슐화**: Property로 접근 제어

---

### 7.3 Player 클래스 (퍼그 캐릭터)
**책임**: 플레이어 캐릭터의 상태와 행동 관리

```python
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
        self._original_height = PLAYER_HEIGHT
    
    # Public 인터페이스
    def jump(self):
        """점프 시작"""
        if not self._is_jumping:
            self._velocity_y = PLAYER_JUMP_VELOCITY
            self._is_jumping = True
    
    def duck(self):
        """숙이기"""
        if not self._is_jumping:
            self._is_ducking = True
            self._height = PLAYER_DUCK_HEIGHT
    
    def stand_up(self):
        """일어서기"""
        self._is_ducking = False
        self._height = self._original_height
    
    # 추상 메서드 구현
    def update(self):
        """물리 업데이트"""
        if self._is_jumping:
            self._apply_gravity()
            self._check_landing()
    
    def draw(self, screen):
        """퍼그 렌더링"""
        rect = self.get_rect()
        pygame.draw.ellipse(screen, PLAYER_COLOR, rect)
        self._draw_eyes(screen)
    
    # Private 메서드 (내부 로직)
    def _apply_gravity(self):
        """중력 적용 (캡슐화)"""
        self._y += self._velocity_y
        self._velocity_y += PLAYER_GRAVITY
    
    def _check_landing(self):
        """착지 판정 (캡슐화)"""
        if self._y >= PLAYER_GROUND_Y:
            self._y = PLAYER_GROUND_Y
            self._is_jumping = False
            self._velocity_y = 0
    
    def _draw_eyes(self, screen):
        """눈 그리기 (내부 디테일)"""
        eye1_pos = (self._x + 10, self._y + 8)
        eye2_pos = (self._x + 20, self._y + 8)
        pygame.draw.circle(screen, (0, 0, 0), eye1_pos, 2)
        pygame.draw.circle(screen, (0, 0, 0), eye2_pos, 2)
    
    def reset(self):
        """초기 상태로 리셋"""
        self._y = PLAYER_GROUND_Y
        self._velocity_y = 0
        self._is_jumping = False
        self._is_ducking = False
```

**OOP 원칙 적용**:
- ✅ **상속**: GameObject의 공통 기능 활용
- ✅ **캡슐화**: 물리 계산은 private 메서드로 숨김
- ✅ **단일 책임**: 플레이어 동작만 관리
- ✅ **다형성**: GameObject의 update/draw 재정의

---

### 7.4 Obstacle 클래스 (장애물 부모)
**책임**: 모든 장애물의 공통 기능

```python
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
        self._speed = 0
    
    def update(self, speed):
        """장애물 이동"""
        self._speed = speed
        self._x -= speed
    
    def is_off_screen(self):
        """화면 밖 판정"""
        return self._x + self._width < 0
    
    @abstractmethod
    def draw(self, screen):
        """렌더링 (자식 클래스에서 구현)"""
        pass
```

**하위 클래스 (다형성)**:

```python
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
        pygame.draw.ellipse(screen, (128, 128, 128), rect)
```

**OOP 원칙 적용**:
- ✅ **상속**: Obstacle 공통 기능 재사용
- ✅ **다형성**: 각 장애물이 독립적 draw() 구현
- ✅ **개방-폐쇄**: 새 장애물 추가 시 기존 코드 수정 불필요

---

### 7.5 ObstacleManager 클래스 (장애물 관리자)
**책임**: 장애물 생성, 관리, 충돌 감지

```python
class ObstacleManager:
    """
    장애물 관리 클래스
    - 장애물 생성 (Factory Pattern)
    - 장애물 업데이트
    - 충돌 감지
    """
    
    def __init__(self):
        self._obstacles = []  # private: 장애물 리스트
        self._last_spawn_x = SCREEN_WIDTH
        self._spawn_gap = OBSTACLE_SPAWN_MIN_GAP
    
    def update(self, speed):
        """모든 장애물 업데이트"""
        # 장애물 이동
        for obstacle in self._obstacles:
            obstacle.update(speed)
        
        # 화면 밖 장애물 제거
        self._remove_off_screen_obstacles()
        
        # 새 장애물 생성
        self._spawn_obstacle_if_needed()
    
    def draw(self, screen):
        """모든 장애물 렌더링"""
        for obstacle in self._obstacles:
            obstacle.draw(screen)
    
    def check_collision(self, player):
        """플레이어와 충돌 검사"""
        player_rect = player.get_rect()
        for obstacle in self._obstacles:
            if player_rect.colliderect(obstacle.get_rect()):
                return True
        return False
    
    def clear(self):
        """모든 장애물 제거"""
        self._obstacles.clear()
    
    # Private 메서드 (Factory Pattern)
    def _spawn_obstacle_if_needed(self):
        """장애물 생성 로직 (캡슐화)"""
        if len(self._obstacles) == 0 or \
           self._obstacles[-1].x < SCREEN_WIDTH - self._spawn_gap:
            obstacle = self._create_random_obstacle()
            self._obstacles.append(obstacle)
            self._spawn_gap = random.randint(
                OBSTACLE_SPAWN_MIN_GAP, 
                OBSTACLE_SPAWN_MAX_GAP
            )
    
    def _create_random_obstacle(self):
        """랜덤 장애물 생성 (Factory Pattern)"""
        obstacle_type = random.choice(['hydrant', 'stump', 'bird'])
        
        if obstacle_type == 'hydrant':
            return Hydrant(SCREEN_WIDTH)
        elif obstacle_type == 'stump':
            return Stump(SCREEN_WIDTH)
        else:  # bird
            y_pos = random.choice(BIRD_Y_POSITIONS)
            return Bird(SCREEN_WIDTH, y_pos)
    
    def _remove_off_screen_obstacles(self):
        """화면 밖 장애물 제거 (캡슐화)"""
        self._obstacles = [obs for obs in self._obstacles 
                          if not obs.is_off_screen()]
```

**OOP 원칙 적용**:
- ✅ **단일 책임**: 장애물 관리만 담당
- ✅ **캡슐화**: 내부 리스트 직접 접근 불가
- ✅ **Factory Pattern**: 장애물 생성 로직 캡슐화
- ✅ **다형성**: 다양한 Obstacle 타입 처리

---

### 7.6 ScoreManager 클래스 (점수 관리)
**책임**: 점수 계산 및 하이스코어 저장

```python
class ScoreManager:
    """
    점수 관리 클래스
    - 점수 증가
    - 하이스코어 저장/불러오기
    - 파일 I/O 캡슐화
    """
    
    def __init__(self):
        self._score = 0              # private: 현재 점수
        self._high_score = 0         # private: 최고 점수
        self._score_file = 'data/highscore.txt'
        self._load_high_score()
    
    def add_score(self, amount):
        """점수 추가"""
        self._score += amount
    
    def reset(self):
        """점수 초기화"""
        if self._score > self._high_score:
            self._high_score = self._score
            self._save_high_score()
        self._score = 0
    
    @property
    def score(self):
        """현재 점수 (읽기 전용)"""
        return self._score
    
    @property
    def high_score(self):
        """최고 점수 (읽기 전용)"""
        return self._high_score
    
    # Private 메서드 (파일 I/O 캡슐화)
    def _load_high_score(self):
        """하이스코어 불러오기"""
        try:
            with open(self._score_file, 'r') as f:
                self._high_score = int(f.read())
        except:
            self._high_score = 0
    
    def _save_high_score(self):
        """하이스코어 저장"""
        try:
            with open(self._score_file, 'w') as f:
                f.write(str(self._high_score))
        except:
            pass
```

**OOP 원칙 적용**:
- ✅ **단일 책임**: 점수 관리만
- ✅ **캡슐화**: 파일 I/O 숨김
- ✅ **Property**: 읽기 전용 접근

---

### 7.7 클래스 다이어그램

```
GameObject (추상)
    ├── Player (퍼그)
    └── Obstacle (추상)
            ├── Hydrant (소화전)
            ├── Stump (나무)
            └── Bird (새)

Game (게임 총괄)
    ├─> Player
    ├─> ObstacleManager
    └─> ScoreManager

ObstacleManager
    └─> Obstacle[] (다형성)
```

**관계**:
- **상속** (is-a): Player **is a** GameObject
- **구성** (has-a): Game **has a** Player
- **의존** (uses): ObstacleManager **uses** Obstacle

---

## 8. 게임 설정 상수 (config.py)

### 화면 설정
```python
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
FPS = 60
BACKGROUND_COLOR = (135, 206, 235)  # 하늘색 (공원 테마)
GROUND_COLOR = (34, 139, 34)        # 잔디 녹색
```

### 플레이어 설정 (퍼그)
```python
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 30               # 퍼그는 키가 낮음
PLAYER_X = 50                    # 고정 X 위치
PLAYER_GROUND_Y = 300            # 지면 Y 위치
PLAYER_JUMP_VELOCITY = -13       # 점프 초기 속도 (퍼그는 약간 낮게)
PLAYER_GRAVITY = 0.8             # 중력 가속도
PLAYER_DUCK_HEIGHT = 20          # 숙일 때 높이
PLAYER_COLOR = (245, 222, 179)   # 연한 갈색 (퍼그 색상)
TONGUE_OUT = True                # 혀 내밀기 애니메이션
```

### 게임 설정
```python
INITIAL_GAME_SPEED = 6           # 초기 속도
MAX_GAME_SPEED = 13              # 최대 속도
SPEED_INCREMENT = 0.001          # 속도 증가율
OBSTACLE_SPAWN_MIN_GAP = 200     # 최소 장애물 간격
OBSTACLE_SPAWN_MAX_GAP = 400     # 최대 장애물 간격
SCORE_INCREMENT = 1              # 프레임당 점수 증가
DAY_NIGHT_SWITCH_SCORE = 700     # 낮/밤 전환 점수
```

### 장애물 설정 (공원 테마)
```python
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
BIRD_Y_POSITIONS = [260, 280, 300]  # 새 가능 높이
```

---

## 9. 핵심 알고리즘 상세

### 9.1 점프 물리
```python
# Player 클래스 내부
def update(self):
    if self.is_jumping:
        self.y += self.velocity_y
        self.velocity_y += PLAYER_GRAVITY  # 중력 적용
        
        # 착지 판정
        if self.y >= PLAYER_GROUND_Y:
            self.y = PLAYER_GROUND_Y
            self.is_jumping = False
            self.velocity_y = 0
```

### 9.2 충돌 감지
```python
# AABB (Axis-Aligned Bounding Box) 방식
def check_collision(player_rect, obstacle_rect):
    return player_rect.colliderect(obstacle_rect)

# 히트박스 여유 (Collision Tolerance)
def get_hitbox(self):
    # 실제 크기보다 5px 작게 설정 (여유 공간)
    return pygame.Rect(
        self.x + 5,
        self.y + 5,
        self.width - 10,
        self.height - 10
    )
```

### 9.3 장애물 생성 로직
```python
def spawn_obstacle(self):
    # 마지막 장애물과의 간격 확인
    if len(self.obstacles) == 0 or \
       self.obstacles[-1].x < SCREEN_WIDTH - self.spawn_gap:
        
        # 무작위 장애물 타입 선택
        obstacle_type = random.choice(['cactus', 'pterosaur'])
        new_obstacle = Obstacle(SCREEN_WIDTH, obstacle_type)
        self.obstacles.append(new_obstacle)
        
        # 다음 간격 설정 (무작위)
        self.spawn_gap = random.randint(
            OBSTACLE_SPAWN_MIN_GAP,
            OBSTACLE_SPAWN_MAX_GAP
        )
```

### 9.4 난이도 증가
```python
# Game 클래스 내부
def update(self):
    # 점수에 따른 속도 증가
    if self.game_speed < MAX_GAME_SPEED:
        self.game_speed += SPEED_INCREMENT
    
    # 점수 증가
    self.score += SCORE_INCREMENT
    
    # 낮/밤 전환
    if self.score % DAY_NIGHT_SWITCH_SCORE == 0:
        self.is_day = not self.is_day
```

---

---

## 부록 A: 기술 참고 자료

**개발 환경**: Python 3.8+, PyGame 2.x  

**공식 문서**:
- Wikipedia - Dinosaur Game: https://en.wikipedia.org/wiki/Dinosaur_Game
- Google Chrome Blog (개발자 인터뷰): https://blog.google/products/chrome/chrome-dino/
- Chrome Dino 소스코드: Chromium 오픈소스 (참고용)
- PyGame 공식 문서: https://www.pygame.org/docs/

---

## 부록 B: 핵심 구현 상세

### B.1 점프 물리 공식
```python
# 매 프레임마다 실행
velocity_y += GRAVITY  # 중력 적용 (예: 0.8)
y += velocity_y         # 위치 업데이트

# 점프 시작 시
velocity_y = JUMP_VELOCITY  # 음수 값 (예: -15)

# 착지 판정
if y >= GROUND_Y:
    y = GROUND_Y
    velocity_y = 0
    is_jumping = False
```

### B.2 충돌 감지 최적화
- **히트박스 여유**: 실제 크기보다 5~10px 작게 설정
- **충돌 판정 타이밍**: 플레이어가 완전히 겹칠 때만 게임 오버
- **성능**: 픽셀 퍼펙트 대신 사각형 충돌로 CPU 사용 최소화

### B.3 무한 스크롤 원리
```python
# 장애물 이동 (왼쪽으로)
obstacle.x -= game_speed

# 화면 밖으로 나간 장애물 제거
if obstacle.x < -obstacle.width:
    obstacles.remove(obstacle)

# 새 장애물 생성 (오른쪽 끝)
if should_spawn_new_obstacle():
    new_obstacle = Obstacle(SCREEN_WIDTH)
    obstacles.append(new_obstacle)
```

### B.4 난이도 곡선 설계
- **초기 속도**: 6 (느림, 초보자 적응 시간)
- **최대 속도**: 13 (숙련자도 어려움)
- **증가율**: 0.001 (프레임당, 약 16초마다 속도 +1)
- **결과**: 약 2분 플레이 시 최고 난이도 도달

---

## 부록 C: 개발 리스크 상세

### C.1 밸런싱 난이도
**문제**: 너무 쉬우면 지루하고, 너무

---

## 부록 E: OOP 개발 가이드 종합 ⭐ CRITICAL

### 🔴 필수 숙지: 이 프로젝트는 OOP를 준수하지 않으면 실패합니다

본 프로젝트의 **최우선 목표**는 **객체지향 프로그래밍(OOP) 원칙을 엄격히 준수**하여 전문적이고 유지보수 가능한 코드를 작성하는 것입니다.

---

### OOP 4대 원칙 필수 체크리스트

#### 1. 캡슐화 (Encapsulation) ✅
- 모든 속성을 `_변수명`으로 private 처리
- Public 인터페이스만 외부 노출
- Property 또는 Getter/Setter 사용

#### 2. 상속 (Inheritance) ✅
- GameObject 추상 클래스 존재
- Player, Obstacle이 GameObject 상속
- `super().__init__()` 호출

#### 3. 다형성 (Polymorphism) ✅
- ObstacleManager가 모든 Obstacle 타입 처리
- 새 장애물 추가 시 기존 코드 수정 불필요
- Factory Pattern 적용

#### 4. 추상화 (Abstraction) ✅
- ABC 모듈 사용
- @abstractmethod 데코레이터 사용
- 추상 메서드 미구현 시 에러 발생

---

### SOLID 원칙 체크리스트

- **S**: 각 클래스가 단일 책임만 가짐
- **O**: 새 기능 추가 시 기존 코드 수정 최소화
- **L**: 자식 클래스를 부모 클래스로 대체 가능
- **I**: 불필요한 메서드 강제하지 않음
- **D**: 구체적 클래스가 아닌 추상화에 의존

---

### 면접 대응 시나리오

**Q: '이 프로젝트에서 OOP를 어떻게 적용했나요?'**

**A:**
> '4가지 관점에서 OOP를 엄격히 적용했습니다:
> 
> 1. **캡슐화**: 모든 클래스의 속성을 private(_변수)로 선언하고 Public 인터페이스만 노출했습니다.
> 
> 2. **상속**: GameObject 추상 클래스를 만들어 Player와 Obstacle이 공통 기능을 상속받도록 했습니다.
> 
> 3. **다형성**: ObstacleManager가 Obstacle 타입 리스트로 모든 장애물을 처리합니다.
> 
> 4. **추상화**: ABC 모듈로 하위 클래스가 반드시 update()와 draw()를 구현하도록 강제했습니다.
> 
> SOLID 원칙도 준수했습니다. 특히 단일 책임 원칙에 따라 Game, Player, ObstacleManager, ScoreManager를 명확히 분리했고, Factory Pattern으로 개방-폐쇄 원칙도 지켰습니다.'

---

### 결론

✅ **OOP 원칙 100% 준수 = 프로젝트 성공**
❌ **OOP 원칙 무시 = 프로젝트 실패**

**이 프로젝트의 성공 여부는 OOP 준수 여부로 결정됩니다!**

---

: 자연스러운 장애물
- **새** 🐦: 공중 장애물
- **선인장/익룡 사용 안 함** → Chrome Dino와 완전 차별화

### 명칭 사용
- **프로젝트명**: "Pug Run" (독창적, 법적 문제 없음)
- **사용 금지**: "Chrome Dino", "T-Rex Runner", "Google Dino"
- **영감 출처 표기**: README에 "Inspired by Chrome Dino Game" 명시

### 프로젝트 라이선스 권장
- **MIT License**: 가장 자유로운 오픈소스 라이선스
- 상업적 이용, 수정, 배포 모두 허용
- 원저작자 표시만 필수

### 참고 출처 명시
README에 다음 문구 포함:
```markdown
## Acknowledgments

This game is inspired by the Chrome Dino Game mechanism.
Original Chrome Dino: Sebastien Gabriel, Alan Bettes, Edward Jung (2014)

**Design Choice**: We chose a pug character instead of a dinosaur to:
- Ensure complete legal safety
- Demonstrate originality and independent thinking
- Create a memorable, distinctive project for our portfolio
```

### 포트폴리오 어필 포인트

**면접 시나리오**:
> **면접관**: "왜 공룡 대신 퍼그를 선택했나요?"
> 
> **당신**: "세 가지 이유입니다:
> 1. **법적 안전성**: Chrome Dino와의 시각적 유사성을 완벽히 회피
> 2. **차별화**: 포트폴리오에서 눈에 띄는 독특한 프로젝트
> 3. **사용자 경험**: 귀여운 캐릭터로 긍정적 감정 유도
> 
> 이 결정 과정에서 저작권법 분석, 리스크 관리, 창의적 문제 해결 능력을 발휘했습니다."

### 법적 리스크 최소화 체크리스트
배포 전 필수 확인:
- [x] 퍼그 캐릭터 사용 → 법적 문제 없음
- [x] 공원 테마 장애물 → 독창적
- [x] 게임 이름 "Pug Run" → 상표권 문제 없음
- [ ] README에 영감 출처 명시
- [ ] 오픈소스 에셋 사용 시 라이선스 준수

### 결론
✅ **퍼그 게임 개발은 100% 안전하고 합법적**  
✅ **포트폴리오 프로젝트로 최적의 선택**  
💰 **추가 비용**: $0 (무료 에셋 또는 자체 제작)  
⚖️ **법적 리스크**: 0%  
🎯 **포트폴리오 가치**: 매우 높음

**상세 분석**: 별도 문서 "저작권_리스크_분석_DinoRun.md" 참조 (공룡 캐릭터 관련)

---

## 부록 E: 확장 가능성 로드맵

### 단기 (v1.1 - v1.3)
- [ ] 파워업 시스템 (무적, 슬로우 모션)
- [ ] 다양한 장애물 추가 (돌, 새, 구름)
- [ ] 배경 테마 추가 (사막, 설원, 도시)
- [ ] 업적 시스템 (100점 달성, 1000점 달성 등)

### 중기 (v2.0)
- [ ] 멀티플레이어 경쟁 모드
  - 2~4명이 동시에 플레이
  - 가장 오래 생존한 사람 승리
- [ ] 온라인 리더보드
  - 전 세계 하이스코어 비교
  - 일일/주간/전체 랭킹
- [ ] 캐릭터 커스터마이징
  - 다양한 공룡 스킨
  - 색상 변경 기능

### 장기 (v3.0)
- [ ] 모바일 버전 (Android/iOS)
  - 터치 컨트롤
  - 세로 모드 지원
- [ ] 스토리 모드
  - 레벨 기반 진행
  - 보스 장애물
- [ ] AI 대전 모드
  - 컴퓨터 AI와 경쟁

---

## 문서 변경 이력

| 날짜 | 버전 | 변경 내용 | 작성자 |
|------|------|----------|--------|
| 2025-11-12 | v1.0 | 초안 작성 | - |
| 2025-11-12 | v2.0 | 상세 개발 로드맵 추가 | - |

---

**문서 끝**

이 개발기획서는 DinoRun 게임 개발 팀이 효율적으로 작업하고 명확한 목표를 달성하기 위한 가이드임. 
필요에 따라 내용을 수정하고 보완할 것을 권장함.
