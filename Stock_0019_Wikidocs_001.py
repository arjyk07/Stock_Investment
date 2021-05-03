#############################################
# Wikidocs
# 파이썬으로 배우는 알고리즘 트레이딩
#############################################

# 참고 : https://wikidocs.net/2843
# 파이썬 기본 자료 구조 

### 연습문제 2-1
"""
    다음(Daum) 주가 89,000원, 100주
    네이버(Naver) 주가 751,000원, 20주
    주식 총액 계산하는 프로그램
"""
daum = 89000 * 100
naver = 751000 * 20
sum_stock = daum + naver


### 연습문제 2-2
# 주식총액에서 다음, 네이버 주가가 각각 5%, 10% 하락한 경우 손실액
daum_down = daum - (daum * 0.05)
naver_down = naver - (naver * 0.10)
sum_stock_down = daum_down + naver_down

daum = 89000
naver = 751000
loss = (daum * 0.05 * 100) + (naver * 0.1 * 20)
print(loss)

### 연습문제 2-3
# 화씨 온도(F) → 섭씨 온도(C) 변환
F = 50
C = (F-32) / 1.8
print(C)

### 연습문제 2-4
# 화면에 "pizza" 10번 출력하는 프로그램
p = "pizza"
print(p * 10)
print("pizza\n" * 10)

### 연습문제 2-5
# 3일 연속으로 하한가 기록했을 때 종가
naver = 1000000
naver_1 = naver - (naver * 0.3)
naver_2 = naver_1 - (naver_1 * 0.3)
naver_3 = naver_2 - (naver_2 * 0.3)
print(naver_3)

# 연습문제 2-6
# 다음 형식 출력
"""
이름: 파이썬
생년월일: 2014년 12월 12일
주민등록번호: 20141212-16233210
"""
print(" 이름: 파이썬\n 생년월일: 2014년 12월 12일\n 주민등록번호: 20141212-1623210")

# 연습문제 2-7
# s라는 변수에 'Daum KaKao' 문자 바인딩, 문자 슬라이싱/연결하기로
# 'KaKao Daum'으로 변경하기
s = 'Daum KaKao'
print(s[5:] + ' ' + s[:5])

# 연습문제 2-8
# a라는 변수에 'hello world'를 'hi world'로 변경
a = 'hello world'
print(a[0] + 'i ' + a[6:])
print('hi ' + a[6:])

# 연습문제 2-9
# x라는 변수에 'abcdef'를 'bcdefa'로 변경
x = 'abcdef'
print(x[1:] + x[0])