# 참고 : 파이썬 증권데이터 분석(김황후 저)

### Chapter6 트레이딩 전략과 구현
## p256 효율적 투자선 구하기

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import Analyzer       # 별도 모듈

mk = Analyzer.MarketDB()
stocks = ['LG디스플레이', '대한유화', '카카오', '한국전력공사']
df = pd.DataFrame()
for s in stocks:
    df[s] = mk.get_daily_price(s, '2016-01-04', '2021.3.16')['close']

daily_ret = df.pct_change()
annual_ret = daily_ret.mean() * 252
daily_cov = daily_ret.cov()
annual_cov = daily_cov * 252

port_ret = []
port_risk = []
port_weights = []

daily_ret
annual_ret
daily_cov
annual_cov

