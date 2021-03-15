# 참고 : https://chancoding.tistory.com/116?category=846070

### plotpy 라이브러리 설치하기
# pip install plotly

### LG디스플레이 데이터 가져오기
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pandas_datareader import data
from datetime import datetime
import pandas as pd

# 데이터 가져올 날짜 설정
start_date = datetime(2013,1,1)
end_date = datetime(2021,3,14)

# 야후에서 LG디스플레이 데이터 가져오기
lgd = data.get_data_yahoo("034220.KS", start_date, end_date)


### Plotly를 사용해 캔들 차트 그리기
lgd = lgd.reset_index() # Date index를 Column으로 보내주기 위함

# Plotly 캔들스틱 그래프 그리기
stock_name = 'LG디스플레이'
fig = go.Figure(data=[go.Candlestick(x=lgd['Date'],
                                     open=lgd['Open'],
                                     high=lgd['High'],
                                     low=lgd['Low'],
                                     close=lgd['Close'])])
fig.show() # ValueError: Mime type rendering requires nbformat>=4.2.0 but it is not installed



### 쉬는 날 제거하기
# 데이터 가져올 날짜 설정
start_date = datetime(2013,1,1)
end_date = datetime(2021,3,14)

# 야후에서 LG디스플레이 데이터 가져오기
lgd = data.get_data_yahoo("034220.KS", start_date, end_date)
lgd = lgd.reset_index()

stock_name = 'LG디스플레이'
fig = go.Figure(data=[go.Candlestick(x=lgd['Date'],
                                     open=lgd['Open'],
                                     high=lgd['High'],
                                     low=lgd['Low'],
                                     close=lgd['Close'])])

# x축 type을 카테고리형으로 설정, 순서를 오름차순으로 날짜순서가 되도록 설정
fig.layout = dict(title=stock_name,
                  xaxis=dict(type="category",
                             categoryorder='category ascending'))
fig.update_xaxes(nticks=5)
fig.show()  # ValueError: Mime type rendering requires nbformat>=4.2.0 but it is not installed


