# 참고 : 파이썬 증권데이터 분석(김황후 저)

### Chapter6 트레이딩 전략과 구현
## p256 효율적 투자선 구하기 + p263 샤프 지수 구하기

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
sharpe_ratio = []

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
    # 샤프 지수 추가
    sharpe_ratio.append(returns/risk)

portfolio = {'Returns': port_ret, 'Risk': port_risk, 'Sharpe': sharpe_ratio}
for i, s in enumerate(stocks):
    portfolio[s] = [weight[i] for weight in port_weights]
df = pd.DataFrame(portfolio)
df = df[['Returns', 'Risk', 'Sharpe'] + [s for s in stocks]]

max_sharpe = df.loc[df['Sharpe'] == df['Sharpe'].max()]
min_risk = df.loc[df['Risk'] ==df['Risk'].min()]


# 효율적 투자선(Efficient Frontier) 확인
df.plot.scatter(x='Risk', y='Returns', c='Sharpe', cmap='viridis',
                edgecolors='k', figsize=(11, 7), grid=True)
plt.scatter(x=max_sharpe['Risk'], y=max_sharpe['Returns'], c='r',
            marker='*', s=300)
plt.scatter(x=min_risk['Risk'], y=min_risk['Returns'], c='r',
            marker='X', s=200)
plt.title('Porfolio Optimization')
plt.xlabel('Risk')
plt.ylabel('Expected Returns')
plt.show()

max_sharpe
min_risk