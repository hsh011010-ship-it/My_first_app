import streamlit as st

st.title("레이아웃")

'### :orange[컬럼: st.columns()]'
col_1, col_2, col_3 = st.columns[(1,2,1)]   # 컬럼 인스턴스 생성. 1:2:1 비율로 컬럼을 나눔

with col_1:
    st.write('## 1번 컬럼')
    st.checkbox('이것은 1번 컬럼에 속한 체크박스1')
    st.checkbox('이것은 1번 컬럼에 속한 체크박스2')

with col_2:
    st.write('## 2번 컬럼')
    st.radio('2번 컬럼의 라디오 버튼', ['radio 1', 'radio 2', 'radio 3'])   # 동일한 라디오 버튼을 생성하면 오류가 발생함
    # 사이드바에 이미 라디오 버튼이 생성되어 있기 때문에, 여기서는 라디오 버튼의 내용을 변경해야 오류가 발생하지 않음

col_3.write('## 3번 컬럼')
col_3.selectbox('3번 컬럼의 셀렉트박스', ['select 1', 'select 2', 'select 3'])
# 사이드바에 이미 셀렉트박스가 생성되어 있기 때문에,여기서는 셀렉트박스의 내용을 변경해야 오류가 발생하지 않음