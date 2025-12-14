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


'# :blue[Streamlit 그래프]'
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
    )

'#### :orange[st.area_chart()]'
st.area_chart(chart_data)

'#### :orange[st.line_chart()]'
st.line_chart(chart_data)

'#### :orange[st.bar_chart()]'
st.bar_chart(chart_data)

'#### :orange[st.scatter_chart()]'
st.scatter_chart(chart_data)

'#### :orange[st.map()]'
df = pd.DataFrame(
    np.random.randn(100, 2) / [100, 100] + [37.55, 126.92],
    colums= ['lat', 'lon'],
)
st.map(df)