# 참고 : https://chancoding.tistory.com/111?category=846070
# pip install mplfinance
# pip install mpl_finance

# LG디스플레이 데이터 가져오기
from mpl_finance import candlestick2_ohlc
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import pandas as pd
from pandas_datareader import data
from datetime import datetime
from IPython.display import display

# 데이터를 가져올 날짜 설정
start_date = datetime(2021,1,1)
end_date = datetime(2021,3,11)

# 야후에서 코스피 데이터 가져오기
lgd_df = data.get_data_yahoo('034220.KS', start_date, end_date)
display(lgd_df.head(5))

# 지수 이동평균선 데이터 구하기
lgd_df['MA5'] = lgd_df['Close'].rolling(5).mean()
lgd_df['MA20'] = lgd_df['Close'].rolling(20).mean()
lgd_df['MA60'] = lgd_df['Close'].rolling(60).mean()
display(lgd_df.tail(5))

# 그래프 그리기
fig, ax = plt.subplots(figsize=(10,5))

ax.set_title('LG Display INDEX', fontsize=15)
ax.set_ylabel('LG Display')
ax.set_xlabel('Date Time')
ax.plot(lgd_df.index, lgd_df[['Close', 'MA5', 'MA20', 'MA60']])
ax.legend(['Close','MA5','MA20','MA60'])
plt.show()


## 캔들 스틱 차트 그리기
fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111)
index = lgd_df.index.astype('str') # 캔들스틱 x축이 str로 들어감

# 이동평균선 그리기
ax.plot(index, lgd_df['MA5'], label='MA5', linewidth=0.7)
ax.plot(index, lgd_df['MA20'], label='MA20', linewidth=0.7)
ax.plot(index, lgd_df['MA60'], label='MA60', linewidth=0.7)

# x축 티커 숫자 20개로 제한
ax.xaxis.set_major_locater(ticker.MaxNLocator(20))

# 그래프 title과 축 이름 지정
ax.set_title('LG Display', fontsize=22)
ax.set_xlabel('Date')

# 캔들차트 그리기
candlestick2_ohlc(ax, lgd_df['Open'], lgd_df['High'],
                  lgd_df['Low'], lgd_df['Close'],
                  width=0.5, colorup='r', colordown='b')
ax.legend()
plt.grid()
plt.show()