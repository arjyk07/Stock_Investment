# 참고 : https://chancoding.tistory.com/113?category=846070

### 데이터 준비
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
from pandas_datareader import data
from datetime import datetime
import pandas as pd
import numpy as np

# 데이터를 가져올 날짜 설정
start_date = datetime(1997, 7, 1)
end_date = datetime(2021, 3, 14)

# 야후에서 코스피 데이터 가져오기
kospi_df = data.get_data_yahoo("^KS11", start_date, end_date)

# 코스피 지수 그래프 그리기
fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111)

ax.plot(kospi_df[['Close']])
type(kospi_df['Close'])     # Series
type(kospi_df[['Close']])   # DataFrame

ax.set_title('KOSPI Index', fontsize=30)
ax.set_xlabel('Date', fontsize=20)

plt.grid()
plt.show()



### 주가 지수 변화량 비교
# 당일 시초가 매수 종가 매도
kospi_df['Open2Close'] = (kospi_df['Close'] - kospi_df['Open'])

# 당일 종가 매수 다음날 시초가 매도
kospi_df['Close2TmrOpen'] = (kospi_df['Open'] - kospi_df['Close'].shift(1))

overNight = kospi_df[['Open2Close', 'Close2TmrOpen']].fillna(0) # 데이터가 없는 날은 0

overNight.cumsum().plot()
plt.show()



### 주기 지수 변화율 비교
# 변화율 계산을 위해 %로만 바뀜. 위와 수식 유사
kospi_df['Open2Close'] = (kospi_df['Close'] - kospi_df['Open']) * 100 / kospi_df['Open']
kospi_df['Close2TmrOpen'] = (kospi_df['Open'] - kospi_df['Close'].shift(1)) * 100 / kospi_df['Close'].shift(1)

overNight = kospi_df[['Open2Close', 'Close2TmrOpen']].fillna(0)
overNight
overNight.describe()
overNight.sum()
overNight.cumsum().plot()



### Overnight 복리 수익률 비교
(overNight/100 + 1).cumprod()

fig, axes = plt.subplots(1, 2, figsize=(10,5))

axes[0].set_title("Open To Close")
axes[1].set_title("Close To Next Open")

(overNight/100 + 1).cumprod()['Open2Close'].plot(ax=axes[0], color='b')
(overNight/100 + 1).cumprod()['Close2TmrOpen'].plot(ax=axes[1], color='r')



### 개별 종목 오버나잇 효과 파악
# 데이터를 가져올 날짜 설정
start_date = datetime(2016,1,1)
end_date = datetime(2021,3,14)

# KODEX200, 삼성전자, LG디스플레이, 대한유화, 카카오
for kr_ticker in ['069500', '005930', '034220', '006650', '035720']:
    # 코스피 코스닥을 직접 확인하기 위해서 try expept 문 사용
    # 코스피는 뒤에 .KS, 코스닥은 뒤에 .KQ ticker를 붙여서 검색해야 함

    try:
        stock_df = data.get_data_yahoo(kr_ticker+".KS", start_date, end_date)
    except:
        stock_df = data.get_data_yahoo(kr_ticker+".KQ", start_date, end_date)

    # 주간, 오버나잇 수익률
    stock_df['Open2Close'] = (stock_df['Close'] - stock_df['Open']) * 100 / stock_df['Open']
    stock_df['Close2TmrOpen'] = (stock_df['Open'] - stock_df['Close'].shift(1)) * 100 / stock_df['Close'].shift(1)

    overNight = stock_df[['Open2Close', 'Close2TmrOpen']].fillna(0)

    # 복리 수익률
    geo = (overNight/100 + 1).cumprod()

    # 그래프 그리기
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    axes[0].set_title("Open To Close")
    axes[1].set_title("Close to Next Open")

    geo['Open2Close'].plot(ax=axes[0], color='b')
    geo['Close2TmrOpen'].plot(ax=axes[1], color='r')

    plt.legen('best')
    plt.show()
