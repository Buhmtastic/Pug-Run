# Pug Run 캐릭터 디자인 가이드

## 🐕 퍼그 캐릭터 디자인

### 퍼그 특징
퍼그(Pug)는 짧은 주둥이와 동그란 몸매, 큰 눈을 가진 소형견입니다.

**신체 특징**:
- 짧고 통통한 다리
- 동그란 머리
- 큰 돌출된 눈
- 짧은 꼬리 (말려있음)
- 작은 귀

**색상**:
- 연한 갈색(Fawn): RGB(245, 222, 179)
- 검은색(Black): RGB(30, 30, 30)

---

## 🎯 무료 퍼그 에셋 찾기

### 추천 검색어
1. **Kenney.nl**
   - "dog sprite"
   - "pet pixel art"

2. **OpenGameArt.org**
   - "pug pixel"
   - "small dog sprite"

### 라이선스 확인
- ✅ **CC0**: 가장 안전
- ✅ **CC-BY**: 원저작자 표시 필수

---

## 🚀 빠른 시작 (30분 버전)

### Phase 1-3: 도형으로 대체
```python
# player.py
def draw(self, screen):
    # 퍼그를 연한 갈색 타원으로
    pygame.draw.ellipse(screen, (245, 222, 179), self.rect)
    # 눈 2개
    pygame.draw.circle(screen, (0, 0, 0), (self.x + 10, self.y + 8), 2)
```

---

이 가이드대로 제작하면 귀엽고 독창적인 Pug Run 게임을 완성할 수 있습니다! 🐕✨
