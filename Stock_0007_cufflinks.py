# 참고 : https://chancoding.tistory.com/117?category=846070

### cufflinks 설치
# pip install cufflinks
# pip install chart_studio


### cufflinks와 chart_studio로 캔들스틱 차트 그리기
import chart_studio.plotly as py
import cufflinks as cf
cf.go_offline(connected=True)

from pandas_datareader import data
from datetime import datetime
import pandas as pd

# 데이터를 가져올 날짜 설정
start_date = datetime(2013,1,1)
end_date = datetime(2021,3,14)

# 야후에서 LG디스플레이 데이터 가져오기
lgd = data.get_data_yahoo("034220.KS", start_date, end_date)
lgd.reset_index(inplace=True)

# QuantFig 메소드를 사용해서 그래프 그리기
qf = cf.QuantFig(lgd, title='LG Display Quant Figure', legend='top', name='LG디스플레이')
qf.iplot()      # jupyter notebook에서 확인


### 거래량, 볼린저밴드 등의 다른 지표 추가하기
qf=cf.QuantFig(lgd, title='LG Display Quant Figure', legend='top', name='LG디스플레이')
qf.add_bollinger_bands()
qf.add_volume()
qf.add_macd()
qf.iplot()