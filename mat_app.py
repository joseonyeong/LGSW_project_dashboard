import streamlit as st
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

## bash 창에서 실행 -> 해당 경로 진입 -> streamlit run mat_app.py
# st.title("Matplotlib 튜토리얼")

# 기본 설정
# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False # 음수 지정 x
sns.set(font='Malgun Gothic',
        rc={'axes.unicode_minus' : False},
        style='darkgrid'
        )

# 페이지 설정
st.set_page_config(page_title="Matplotlib & Seaborn 튜토리얼", layout="wide")
st.title("Matplotlib & Seaborn 튜토리얼") # 제목

# 데이터셋 불러오기
tips = sns.load_dataset('tips')

# 데이터 미리보기
# 소제목
st.subheader('데이터 미리보기')
# tip 데이터셋 출력
st.dataframe(tips.head())

## 교재 p.406 살짝 다름 주의
# 기본 막대 그래프, matplotlib & seaborn
st.subheader("1. 기본 막대 그래프")
## 객체 지향으로 작성하는 이유
## : 그래프를 그리는 목적 : 예쁘게 출력하기 위해
## : ax (객체지향)으로 접근할 경우 세부적으로 세세하게 접근할 수 있음
fig, ax = plt.subplots(figsize=(10,6)) # 객체 지향 방식으로 차트 작성

## 통계와 관련된 시각화 자료 == seaborn
## https://seaborn.pydata.org/
sns.barplot(data = tips, x = 'day', y = 'total_bill', ax = ax)

## 시각화 자료를 이쁘게 다듬을 때 == matplotlib
## https://matplotlib.org/stable/api/index
ax.set_title('요일별 평균 지불 금액') # matplotlib
ax.set_xlabel('요일') # matplotlib
ax.set_ylabel('평균 지불 금액($)') # matplotlib

# plt.show() # jupyter, colab에서 출력할 때 사용
## 웹상에 띄울 때 == streamlit
st.pyplot(fig)

# 산점도
st.subheader("2. 산점도")

# x축, y축이 연속형 변수여야함.
fig1, ax1 = plt.subplots(figsize=(10, 6)) # matplotlib

sns.barplot(data=tips, x='day', y='total_bill', ax=ax) # seaborn
sns.scatterplot(data=tips, x = 'total_bill', y = 'tip', hue='day', size='size', ax=ax1)
st.pyplot(fig1)

# 히트맵
st.subheader('3. 히트맵')

# 요일과 시간별 평균 팁 계산
pivot_df = tips.pivot_table(values='tip', index='day', columns='time', aggfunc='mean')
fig2, ax2 = plt.subplots(figsize=(10,6))
sns.heatmap(pivot_df, annot=True, fmt='.2f', ax=ax2)
st.pyplot(fig2)

# 회귀선이 있는 산점도
st.subheader('회귀선이 있는 산점도')

fig3, ax3 = plt.subplots(figsize=(10,6))
sns.regplot(data=tips, x='total_bill', y='tip', scatter_kws={'alpha':0.5}, ax=ax3) # alpha는 투명도
st.pyplot(fig3)

## gpt에게 질문을 할 때는
## fig, ax = plt.subplots() 형식으로 짜달라고 해야 함.