import streamlit as st
import pandas as pd

st.title('쿨메신저 메시지 뷰어')

# 파일 업로드
uploaded_file = st.file_uploader("메시지 파일을 업로드하세요 (.xls 형식)", type="xls")

if uploaded_file is not None:
    # 업로드된 파일을 데이터프레임으로 읽기
    df = pd.read_excel(uploaded_file)
    
    # 데이터프레임 확인
    st.subheader('전체 메시지')
    st.dataframe(df)
    
    # 검색어 입력
    search_term = st.text_input('검색어를 입력하세요')
    
    if search_term:
        # 검색 기능 구현
        search_result = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]
        
        st.subheader('검색 결과')
        st.dataframe(search_result)
else:
    st.write('왼쪽 사이드바에서 파일을 업로드해주세요.')
