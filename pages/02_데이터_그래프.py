import streamlit as st

st.title("데이터 그래프 페이지")

'### :orange[Pandas 데이터프레임]'
import pandas as pd
df = pd.DataFrame(
    {'id': [1, 2, 3],
     'name': ['Alice', 'Bob', 'Charlie'],
     'age': [24, 35, 45]
    }
)
df   # 데이터프레임 출력


'### :orange[지표(Metric)]'
col1, col2, col3 = st.columns(3)   # 3개의 컬럼 생성
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")