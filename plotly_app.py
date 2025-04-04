import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import pandas as pd
import streamlit as st

st.title("Plotly 튜토리얼")
# # https://plotly.com/python-api-reference/plotly.express.html#px

# # plotly express
# # high level interface
# # 간단하고 직관적인 문법으로 쉽게 시각화 생성 가능
# # 다양한 표준 차트
# # 세밀한 커스터마이징은 제한
# # 개발용
# # https://wikidocs.net/book/8909 : 책 추천
# # plotly로 시작하는 인터랙티브 데이터 시각화 in r&python : 책 추천천

# # graph object -> matplotlib
# # low level interface
# # 세부적인 커스터마이징 가능
# # 복잡한 상호작용, 레이아웃 만들기 가능

# tips dataset 가져오기
tips = sns.load_dataset('tips')
# 데이터 미리보기
st.subheader('데이터 미리보기')
st.dataframe(tips.head())

# 기본 막대 그래프
st.subheader('1. 기본 막대 그래프')
fig = px.bar(tips, x='day', y='tip', title='요일별 지불 금액($)', 
             labels={'day': '요일', 'tip': '평균 Tip($)'}) # 이름 바꾸기기
st.plotly_chart(fig, use_container_width=True)

# 산점도
st.subheader('2. 산점도')
fig1 = px.scatter(tips, x='total_bill', y='tip',labels={'total_bill': '총액($)', 'tip': '평균 Tip($)'},
                  hover_data=['day', 'time','smoker']) # hover_data : 참고할 데이터 # 커서를 놓으면 데이터 볼 수 있음
st.plotly_chart(fig1)

## 배포된 streamlit 주식차트 대시보드
# https://k7geonnwm8uvbenwvohfwe.streamlit.app/
