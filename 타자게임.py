import random #랜덤모듈 사용
import time #시간모듈 사용

# 단어 리스트
w = ["고양이", "개", "여우", "원숭이", "생쥐", "팬더", "개구리", "뱀", "늑대", "호랑이", "사자", "사슴", "토끼"]
n = 1                                   # 문제 번호
print("[타자 게임] 준비되면 Enter!")
input()                                 # 사용자가 엔터를 누를 때까지 기다림
start = time.time()                     # 시작 시간을 기록
q = random.choice(w)                    # 단어 리스트에서 요소를 랜덤하게 뽑는다.
while n <= 5:                          # 문제를 다섯 번 반복
    print("*문제", n)
    print(q)                            # 문제를 출력
    x = input()                         # 사용자 입력을 받는다.
    if q == x:                          # 사용자가 올바르게 입력했는지?
        print("통과!")
        n = n + 1                       # 문제 번호를 1 증가
        q = random.choice(w)            # 새 문제를 뽑는다.
    else:
        print("오타! 다시 도전!")

end = time.time()                       # 종료 시간을 기록
a = end - start                        # 실제로 걸린 시간을 계산
a = format(a, ".1f")                  # 소수점 첫째 자리까지만 표시되도록 포맷팅
print("타자 시간 :", a , "초")
