# 참고 : 파이썬 증권데이터 분석(김황후 저)

### p282 볼린저 밴드를 이용한 반전 매매기법(Reversals)
import matplotlib.pyplot as plt
import Analyzer

mk = Analyzer.MarketDB()
df = mk.get_daily_price('LG디스플레이', '2020-10-21', '2021.03.16')

df['MA20'] =d
