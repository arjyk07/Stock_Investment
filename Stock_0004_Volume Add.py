# 참고 : https://chancoding.tistory.com/112?category=846070
from mpl_finance import candlestick2_ohlc
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
from pandas_datareader import data
from datetime import datetime
import pandas as pd
import numpy as np

# 데이터를 가져올 날짜 설정
start_date = datetime(2020,9,1)
end_date = datetime(2021,3,11)

# 야후에서 LG디스플레이 데이터 가져오기
lgd_df = data.get_data_yahoo('034220.KS', start_date, end_date)
lgd_df2 = data.DataReader('034220.KS', 'yahoo')

# LG디스플레이 이동평균선 데이터 구하기
lgd_df['MA5'] = lgd_df['Close'].rolling(5).mean()
lgd_df['MA20'] = lgd_df['Close'].rolling(20).mean()
lgd_df['MA60'] = lgd_df['Close'].rolling(60).mean()

fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111)
index = lgd_df.index.astype('str') # 캔들스틱 x축이 str로 들어감

# 이동평균선 그리기
ax.plot(index, lgd_df['MA5'], label='MA5', linewidth=0.7)
ax.plot(index, lgd_df['MA20'], label='MA20', linewidth=0.7)
ax.plot(index, lgd_df['MA60'], label='MA60', linewidth=0.7)

# x축 티커 숫자 20개로 제한
ax.xaxis.set_major_locator(ticker.MaxNLocator(10))

# 그래프 title과 축 이름 지정
ax.set_title('LG Display', fontsize=22)
ax.set_xlabel('Date')

# 캔들차트 그리기
candlestick2_ohlc(ax, lgd_df['Open'], lgd_df['High'],
                  lgd_df['Low'], lgd_df['Close'],
                  width=0.5, colorup='r', colordown='b')
ax.legend()
plt.grid()
plt.xticks(rotation=45)
plt.show()




## 그래프 프레임 잡기
fig = plt.figure(figsize=(20,10))
top_axes = plt.subplot2grid((4,4), (0,0), rowspan=3, colspan=4)
bottom_axes = plt.subplot2grid((4,4), (3,0), rowspan=1, colspan=4, sharex=top_axes)
bottom_axes.get_yaxis().get_major_formatter().set_scientific(False) # 거래량 값 그대로 표현

## 거래량 그래프
fig = plt.figure(figsize=(15,5))
ax = fig.add_subplot(111)

ax.bar(index, lgd_df['Volume'], color='r')

ax.xaxis.set_major_locator(ticker.MaxNLocator(10))
ax.set_title('LG Display', fontsize=22)
ax.set_xlabel('Date')

plt.grid()
plt.xticks(rotation=45)
plt.show()

## 거래량 그래프에서 빨간색과 파란색 구분하기
# 색깔 구분을 위한 함수
color_fuc = lambda x : 'r' if x >= 0 else 'b'
# LG디스플레이 거래량의 차이
lgd_df['Volume'].diff().fillna(0) # 첫 행은 값이 NaN이므로 0으로 채워줌
# 색깔 구분을 위한 함수를 apply 시켜 Red와 Blue를 구분한다.
color_df = lgd_df['Volume'].diff().fillna(0).apply(color_fuc)
# 구분된 값을 list 형태로 만들어준다.
color_list = list(color_df)

# 그래프를 그릴 때, color = color_list를 넣어서 색깔을 지정함
ax.bar(index, lgd_df['Volume'], color=color_list)



## 거래량 그래프 다시 그리기
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)

# 거래량 그래프
ax.bar(index, lgd_df['Volume'], color=color_list)
ax.get_yaxis().get_major_formatter().set_scientific(False) # 거래량 값 그대로 표현

# 그래프 title과 축 이름 지정
ax.xaxis.set_major_locator(ticker.MaxNLocator(10))
ax.set_title('LG Display', fontsize=10)
ax.set_xlabel('Date')

plt.grid()
plt.xticks(rotation=45)
plt.show()



###############################################################
# 캔들차트+거래량 그래프 최종 소스 코드 #
###############################################################

#-----------------------------------------------------------------
# 그래프 구역 나누기
fig = plt.figure(figsize=(10,5))
top_axes = plt.subplot2grid((4,4), (0,0), rowspan=3, colspan=4)
bottom_axes = plt.subplot2grid((4,4), (3,0), rowspan=1, colspan=4, sharex=top_axes)
bottom_axes.get_yaxis().get_major_formatter().set_scientific(False)
#-----------------------------------------------------------------

# 인덱스 설정
idx = lgd_df.index.astype('str')

# 이동평균선 그리기
top_axes.plot(idx, lgd_df['MA5'], label='MA5', linewidth=0.7)
top_axes.plot(idx, lgd_df['MA20'], label='MA20', linewidth=0.7)
top_axes.plot(idx, lgd_df['MA60'], label='MA60', linewidth=0.7)

# 캔들차트 그리기
candlestick2_ohlc(top_axes, lgd_df['Open'], lgd_df['High'],
                  lgd_df['Low'], lgd_df['Close'],
                  width=0.5, colorup='r', colordown='b')

#----------------------------------------------------------------

# 거래량 날짜 지정
color_fuc = lambda x : 'r' if x>=0 else 'b'
color_list = list(lgd_df['Volume'].diff().fillna(0).apply(color_fuc))
bottom_axes.bar(idx, lgd_df['Volume'], width=0.5,
                align='center',
                color=color_list)

#----------------------------------------------------------------

# 그래프 title 지정
top_axes.set_title('LG Display', fontsize=15)
# x축 티커 숫자 20개로 제한
top_axes.xaxis.set_major_locator(ticker.MaxNLocator(10))
# x축 라벨 지정
bottom_axes.set_xlabel('Date', fontsize=15)

top_axes.legend()
plt.tight_layout()
# plt.xticks(rotation=45)
plt.show()