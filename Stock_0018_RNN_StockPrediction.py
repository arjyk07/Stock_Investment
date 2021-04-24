# 참고 : 파이썬 증권데이터 분석(김황후 저)

# p443 RNN으로 주가 예측하기
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
import numpy as np
import matplotlib.pyplot as plt
import Analyzer

# LG디스플레이 OHLVC 데이터 조회
mk = Analyzer.MarketDB()
raw_df = mk.get_daily_price('LG디스플레이', '2017-01-01', '2021-03-30')

def MinMaxScaler(data):
    """ 최소값과 최대값을 이용하여 0 ~ 1 값으로 변환 """
    numerator = data - np.min(data, 0)
    denominator = np.max(data, 0) - np.min(data, 0)
    return numerator / (denominator + 1e-7)

# 데이터 전처리
dfx = raw_df[['open', 'high', 'low', 'volume', 'close']]
dfx = MinMaxScaler(dfx)     # 계산속도 향상을 위해 데이터의 스케일을 0~1로 변경
dfy = dfx[['close']]
x = dfx.values.tolist()
y = dfy.values.tolist()

# 데이터셋 생성
data_x = []
data_y = []
window_size = 10            # 10일 간의 OHLVC 데이터
for i in range(len(y) - window_size):
    _x = x[i : i + window_size]     # 다음날 종가(i+window_size)는 포함되지 않음
    _y = y[i + window_size]         # 다음날 종가
    data_x.append(_x)
    data_y.append(_y)
print(_x, "->", _y)

# 훈련 데이터셋 생성(70%)
train_size = int(len(data_y) * 0.7)
train_x = np.array(data_x[0 : train_size])
train_y = np.array(data_y[0 : train_size])

# 테스트 데이터셋 생성(30%)
test_size = len(data_y) - train_size
test_x = np.array(data_x[train_size : len(data_x)])
test_y = np.array(data_y[train_size : len(data_y)])

# 모델 생성
model = Sequential()
model.add(LSTM(units=10, activation='relu', return_sequences=True,
               input_shape=(window_size, 5)))
model.add(Dropout(0.1))
model.add(LSTM(units=10, activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(units=1))
model.summary()

# 학습 및 예측
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(train_x, train_y, epochs=60, batch_size=30)           # 학습
pred_y = model.predict(test_x)                                  # 예측

# 실제 종가와 예측치를 그래프로 비교
plt.figure()
plt.plot(test_y, color='red', label='real LG Display stock price')
plt.plot(pred_y, color='blue', label='predicted LG Display stock price')
plt.title('LG Display stock price prediction')
plt.xlabel('time')
plt.ylabel('stock price')
plt.legend()
plt.show()

# 다음날 예측 종가 출력
print("LG Display's price :", raw_df.close[-1]*pred_y[-1]/dfy.close[-1])

