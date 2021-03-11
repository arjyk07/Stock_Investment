# 참고 : https://chancoding.tistory.com/108

# 1.pandas_datareader 설치하기
# pip install pandas_datareader

# 2. 지수데이터 불러오기
from pandas_datareader import data
from datetime import datetime

# KOSPI 지수데이터
df1 = data.DataReader("^KS11", "yahoo")
df2 = data.get_data_yahoo("^KS11")

# 날짜지정
start_date = datetime(2007,1,1)
end_date = datetime(2020,3,3)
df = data.get_data_yahoo("^KS11", start_date, end_date)



