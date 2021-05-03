#############################################
# Wikidocs
# 파이썬으로 배우는 알고리즘 트레이딩
#############################################

# 참고 : https://wikidocs.net/2850
# 파이썬 기본 자료 구조

# 리스트는 출석부에 학생들의 이름을 적어 두는 것과 비슷한 개념
# 파이썬 리스트에 있는 데이터에 하나씩 접근 : 인덱싱
# 파이썬 리스트에 있는 여러 개의 데이터 동시 접근 : 파이썬 슬라이싱
# 0:5 → 0번 위치에서 5번 위치까지 가져와라

# 파이썬 리스트에 데이터 추가하는 방법
# 1. append 메서드
# 2. insert 메서드 : 원하는 위치에 추가
kospi_top10 = ['삼성전자', 'SK하이닉스', '현대차', '한국전력', '아모레퍼시픽', '제일모직', '삼성전자우', '삼성생명', 'NAVER', '현대모비스']
kospi_top10.insert(3, 'SK텔레콤')


# 참고 : https://wikidocs.net/2853
# 튜플
t = ('Samsung', 'LG', 'SK')


# 참고 : https://wikidocs.net/2856
# 딕셔너리 : 연관되는 데이터 저장
cur_price = {}
type(cur_price)

cur_price['daeshin'] = 30000
cur_price

cur_price['Daum KAKAO'] = 80000
cur_price
len(cur_price)

# 딕셔너리에 데이터 삽입 : 명시적으로 키-값 쌍으로 넣기, 초기값 입력
# 딕셔너리에 데이터 삭제 : del
cur_price['daeshin']

# 딕셔너리로부터 키-값 구하기
cur_price.keys()
list(cur_price.keys())
price_list = list(cur_price.values())
price_list

'naver' in cur_price.keys()         # False
'daeshin' in cur_price.keys()       # True


# 참고 : 연습문제 https://wikidocs.net/3037
### 연습문제 3-1
# 리스트 만들기
naver_closing_price = [474500, 461500, 501000, 500500, 488500]

### 연습문제 3-2
# 종가 기준 가장 높은 가격
print(max(naver_closing_price))

### 연습문제 3-3
# 종가 기준 가장 낮은 가격
print(min(naver_closing_price))

### 연습문제 3-4
# 가장 종가 높았던 요일과 가장 종가 낮았던 요일 가격 차이
print(max(naver_closing_price) - min(naver_closing_price))
print('가격차: ', max(naver_closing_price) - min(naver_closing_price))

### 연습문제 3-5
# 수요일 종가 화면 출력
print(naver_closing_price[2])
print('수요일 종가: ', naver_closing_price[2])

### 연습문제 3-6
# 딕셔너리 날짜:종가 만들기
naver_closing_price2 = {'09/07' : 474500, '09/08' : 461500,
                        '09/09' : 501000, '09/10' : 500500,
                        '09/11' : 488500}

### 연습문제 3-7
# 딕셔너리 활용해 09/09 종가 출력
naver_closing_price2['09/09']