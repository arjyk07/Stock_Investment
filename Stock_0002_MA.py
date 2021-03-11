# 참고 : https://chancoding.tistory.com/110?category=846070
from pandas_datareader import data
from datetime import datetime
import matplotlib.pyplot as plt
# pip install IPython
from IPython.display import display

start_date = datetime(2020,1,1)
end_date = datetime(2021,3,11)

kospi_df = data.get_data_yahoo("^KS11", start_date, end_date)
LGD_df = data.get_data_yahoo('034220.KS', start_date, end_date)
kodex200 = data.get_data_yahoo('069500.KS', start_date, end_date)

LGD_df.index   # 데이터프레임 구성 확인 - 인덱스
LGD_df.columns # 데이터프레임 구성 확인 - 컬럼

# 추가 그래프 출력 : LG디스플레이 VS KOSPI VS KODEX200
plt.plot(LGD_df.index, LGD_df.Close, 'b', label='LG Display')
plt.plot(kospi_df.index, kospi_df.Close, 'r--', label='KOSPI')
plt.plot(kodex200.index, kodex200.Close, 'g', label='KODEX 200')
plt.legend(loc='best')
plt.show()



# 주식 이동평균선
kospi_df['MA3'] = kospi_df['Close'].rolling(3).mean()
kospi_df['MA5'] = kospi_df['Close'].rolling(5).mean()
kospi_df['MA10'] = kospi_df['Close'].rolling(10).mean()
kospi_df['MA60'] = kospi_df['Close'].rolling(60).mean()

kospi_df[['Close', 'MA3', 'MA5', 'MA10', 'MA60']].plot()
display(kospi_df.head(5))

fig, ax = plt.subplots(figsize=(10,5))
ax.set_title('KOSPI INDEX', fontsize=15)
ax.set_ylabel('KOSPI')
ax.set_xlabel('Date Time')
ax.plot(kospi_df.index, kospi_df[['Close','MA5','MA10']])
ax.legend(['Close','MA5','MA10'])
plt.show()