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