#############################################
# Wikidocs
# 파이썬으로 배우는 알고리즘 트레이딩
#############################################

# 참고 : https://wikidocs.net/2864
# 제어문

# if ~ elif ~ else문
price = 7000
if price < 1000:
    bid = 1
elif price >= 1000 and price < 5000:
    bid = 5
elif price >= 5000 and price < 10000:
    bid = 10
elif price >= 10000 and price < 50000:
    bid = 50
elif price >= 50000 and price < 100000:
    bid = 100
elif price >= 100000 and price < 500000:
    bid = 500
elif price >= 500000:
    bid = 1000
bid



# for 반복문 : 같은 일을 되풀이함
for i in [0,1,2,3,4,5,6,7,8,9,10]:
    print(i)


# range : 범위
range(1,10)
list(range(1,10))

for i in range(0,11):
    print(i)


# for와 리스트와 튜플, 딕셔너리
interest_stocks = ["Naver", "Samsung", "SK Hynix"]              # 리스트 : 수정o
interest_stocks2 = ("Naver", "Samsung", "SK Hynix")             # 튜플 : 수정x
interest_stocks3 = {"Naver":10, "Samsung":5, "SK Hynix":30}     # 딕셔너리 : 키-값 쌍

for company in interest_stocks:
    print("%s: Buy 10" % company)       # 문자열이 출력될 위치에 %s를 쓰고, 실제로 출력될 문자열은 %기호 뒤에 변수명 지정

for company in interest_stocks:
    print("company: Buy 10")

for company in interest_stocks2:
    print("%s: Buy 10" % company)

for company, stock_num in interest_stocks3.items():
    print("%s: Buy %s" % (company, stock_num))

for company in interest_stocks3.keys():
    print("%s: Buy %s" % (company, interest_stocks3[company]))


# for : 반복횟수가 미리 정해져있거나 리스트/튜플/사전과 같은 파이썬 자료구조와 함께 사용
# while : 반복횟수가 특별히 정해져있지 않고, 어떤 조건을 충족하는 동안만 실행될 때 주로 사용
i = 0
while i <= 10:      # while문의 조건문으로 조건식 판단
    print(i)
    i = i+1
i

# while 문을 이용한 연속 상한가 계산
LG_Display = 23950      # 2021/5/4 종가 기준
day = 1
while day < 6:
    LG_Display = LG_Display + LG_Display * 0.3
    day = day + 1
LG_Display


# while과 if : 홀수만 출력하기
num = 0
while num <= 10:
    if num % 2 == 1:
        print(num)
    num += 1


# break : 반복적으로 수행하다가 특정 조건일 때 반복문 자체를 빠져나와야 할 때
# continue : 반복문 전체를 빠져나오는 것이 아니라 해당 조건만 건너뛰고 싶을 때
num = 0
while num < 10:
    num += 1
    if num == 5:
        continue
    print(num)


# 중첩 루프 : 반복문 여러 개가 겹쳐 있는 구조
for i in [1,2,3,4]:
    for j in [1,2,3,4]:
        pass

""" 중첩 루프 예시 
    1층에 가서 1층의 각 세대에 신문 배달,
    2층에 가서 2층의 각 세대에 신문 배달,
    3층에 가서 3층의 각 세대에 신문 배달,
    4층에 가서 4층의 각 세대에 신문 배달
"""
apart = [[101,102,103,104], [201,202,203,204], [301,302,303,304]]
for floor in apart:
    for room in floor:
        # print("Newspaper delivery: ", room)
        print("Newspaper delivery: %s" % room)


### 연습문제
# 연습문제 4-1 : ***** 패턴 출력
print('*' * 5, end='')      # 줄바꿈 없이 출력

# 연습문제 4-2 : ***** 5줄 출력(중첩루프 활용)
test = [['*****'],['*****'],['*****'],['*****']]
for i in test:
    for x in i:
        print(x)

# 연습문제 4-3 : *, **, ***, ****, ***** 패턴 출력
test2 = '*'
for i in range(1,6):
    print(i * test2)

# 연습문제 4-4 : *****, ****, ***, ** , * 패턴 출력
test3 = '*'
test3a = 5
while test3a > 0:
    print(test3 * test3a)
    test3a -= 1

# 연습문제 4-5 : *, **, ***, ****, ***** 패턴 출력(오른쪽 정렬)
test4 = '*'
for i in range(1,6):
    print(' ' * (5-i), test4 * i)

# 연습문제 4-6 : *****, ****, ***, ** , * 패턴 출력(오른쪽 정렬)
test5 = '*'
for i in range(0,5):
    print(' ' * i, test5 * (5-i))

# 연습문제 4-7 : *, ***, *****, *******, ********* 출력(가운데 정렬)
# 연습문제 4-8 : *********, *******, *****, ***, * 출력(가운데 정렬)
# 연습문제 4-9 : 신문배달 프로그램(단, 미납세대 배달x)
