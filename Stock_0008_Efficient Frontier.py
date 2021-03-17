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

# 포트폴리오 수익률, 리스크, 비중 저장할 리스트 생성
port_ret = []
port_risk = []
port_weights = []

daily_ret
annual_ret
daily_cov
annual_cov


# 몬테카를로 시뮬레이션
for _ in range(20000):
    weights = np.random.random(len(stocks))
    weights /= np.sum(weights)

    returns = np.dot(weights, annual_ret)
    risk = np.sqrt(np.dot(weights.T, np.dot(annual_cov, weights)))

    port_ret.append(returns)
    port_risk.append(risk)
    port_weights.append(weights)

portfolio = {'Returns': port_ret, 'Risk': port_risk}
for i, s in enumerate(stocks):
    portfolio[s] = [weight[i] for weight in port_weights]
df = pd.DataFrame(portfolio)
df = df[['Returns', 'Risk'] + [s for s in stocks]]


# 효율적 투자선(Efficient Frontier) 확인
df.plot.scatter(x='Risk', y='Returns', figsize=(10, 7), grid=True)
plt.title('Efficient Frontier')
plt.xlabel('Risk')
plt.ylabel('Expected Returns')
plt.show()