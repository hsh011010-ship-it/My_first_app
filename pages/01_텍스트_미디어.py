import streamlit as st

st.title("텍스트 미디어 페이지")

'## 🔠: 일반 텍스트'

st.title('제목 : st.title()')
st.header('헤더 : st.header()')
st.subheader('서브헤더 : st.subheader()')
st.text('본문 텍스트 : st.text()')
st.markdown('## 마크다운 : st.markdown()') 
st.caption('캡션(작고 흐린 글씨로 표현됨) : st.caption()')

'# 🔠: st.write()'
st.write('# 마크다운 H1 : st.write()')
st.write('### 마크다운 H3 : st.write()')
st.write('')   # 빈 줄 추가

'# 🔠: 색상이 있는 텍스트'
st.write(':red[빨간색 텍스트]')
st.write(':blue[파란색 텍스트]')

'### 코드 블록: st.code()'
st.code('print("Hello, World!")', language='python', line_numbers=True)

'### 코드+결과: st.echo()'
with st.echo():
    # 이 블록의 코드와 결과를 출력
    name = "Seokhyeon Hong"
    st.write("Hello, Streamlit!", name)

'### Latex 수식 작성: st.latex()'
st.latex(r'\int_a^b f(x)dx')

st.divider()   # 구분선