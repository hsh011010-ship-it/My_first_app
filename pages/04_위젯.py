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


'# 🏋️‍♂️ :blue[버튼]'

'### :orange[기본 버튼: st.button()]'
button = st.button('일반 버튼')
if button:
    st.write('버튼이 클릭되었습니다.')

primary_button = st.button('주요 버튼', type='primary')
if primary_button:
    st.write('주요 버튼이 클릭되었습니다.')

'### :orange[다운로드 버튼: st.download_button()]'
with open("assets/25년도 1학기 홍익대 전경-2.jpg", "rb") as file:
    st.download_button(
        label="이미지 파일 다운로드",   # 버튼 라벨
        data=file,   # 다운로드할 파일 경로
        file_name="hongik_univ.jpg",   # 다운로드 파일명
        mime="image/jpeg"   # 파일 형식
        )

'### :orange[피드백 버튼: st.feedback()]'
sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"당신은 {sentiment_mapping[selected]} star(s)을 선택하였습니다.")

sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
selected = st.feedback("thumbs")
if selected is not None:
    st.markdown(f"당신은 {sentiment_mapping[selected]} 을 선택하였습니다.")
    
'### :orange[링크 버튼: st.link_button()]'
st.link_button("갤러리 링크", "https://streamlit.io/gallery")


'### :orange[체크박스]'
check = st.checkbox('여기를 체크하세요')
if check:
    st.write('체크되었습니다.')

'### :orange[라디오 버튼]'
radio = st.radio('여기에서 선택하세요', ['선택 1', '선택 2', '선택 3'])
st.write(radio+'가 선택되었습니다.')

'### :orange[셀렉트 박스]'
select = st.selectbox('여기에서 선택하세요', ['선택 1', '선택 2', '선택 3'])
st.write(select+'가 선택되었습니다.')

'### :orange[멀티 셀렉트 박스]'
multi = st.multiselect('여기에서 여러 값을 선택하세요', ['선택 1', '선택 2', '선택 3'])
st.write(f'{type(multi) = }, {multi}가 선택되었습니다.')