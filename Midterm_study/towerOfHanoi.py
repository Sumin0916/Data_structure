"""
기둥 a에 있는 모든 원판을 보조 기둥 c를 사용해 기둥 b로 옮겨라.
"""

def move(n, a, b, c):
    if n == 0:
        return
    move(n-1, a, c, b)
    print(f"{a}에 있는 원판을 {b}로 옮겼다.")
    move(n-1, c, b, a)

move(4, 'A', 'B', 'C')
