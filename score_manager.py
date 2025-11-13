import os

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
        if os.path.exists(self._score_file):
            try:
                with open(self._score_file, 'r') as f:
                    self._high_score = int(f.read())
            except ValueError: # 파일 내용이 숫자가 아닐 경우
                self._high_score = 0
            except Exception as e:
                print(f"Error loading high score: {e}")
                self._high_score = 0
        else:
            self._high_score = 0
    
    def _save_high_score(self):
        """하이스코어 저장"""
        try:
            # data 디렉토리가 없으면 생성
            os.makedirs(os.path.dirname(self._score_file), exist_ok=True)
            with open(self._score_file, 'w') as f:
                f.write(str(self._high_score))
        except Exception as e:
            print(f"Error saving high score: {e}")
