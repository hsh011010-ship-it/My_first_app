import streamlit as st

st.title("위젯")

'# 🤖 :blue[사용자 입력]'

'### :orange[텍스트 입력]'
text = st.text_input('여기에 텍스트를 입력하세요')
st.write(f'입력된 텍스트: {text}')

'### :orange[숫자 입력]'
number = st.number_input('여기에 숫자를 입력하세요')
st.write(f'입력된 숫자: {number}')

'### :orange[날짜 입력]'
date = st.date_input('날짜를 선택하세요')
st.write(f'선택된 날짜: {date}')

'### :orange[시간 입력]'
time = st.time_input('시간을 선택하세요')
st.write(f'선택된 시간: {time}')

'### :orange[파일 업로드]'
file = st.file_uploader('파일을 업로드하세요')

# 파일을 임시적으로 사용하는 방법
if file:
    st.write(f'업로드된 파일: {file}')

# 파일을 별도로 저장하는 방법
import os
if file:
    # 파일을 저장할 경로 지정
    file_path = os.path.join('C:/Users/USER/Desktop/데이터 시각화', file.name)
    # 파일 저장
    with open(file_path, 'wb') as f:   # 'wb'는 바이너리 쓰기 모드
        f.write(file.getbuffer())
    st.write(f'파일이 저장되었습니다: {file_path}')