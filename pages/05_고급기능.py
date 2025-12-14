import streamlit as st

st.title("고급 기능")

import time

@st.cache_data
def long_running_function(param1):
    time.sleep(5)  
    return param1 * param1

start = time.time()

# 숫자 입력은 입력된 값을 반환
num_1 = st.number_input('입력한 숫자의 제곱을 계산합니다.')
st.write(f'{num_1}의 제곱은 {long_running_function(num_1)}입니다.' +
         f'계산시간은 {time.time() - start:.2f}초 소요')
st.write(' :green[캐싱이 적용되면 동일한 계산은 저장된 결과를 사용하여 빠르게 처리함]')