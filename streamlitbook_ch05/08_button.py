# -*- coding:utf-8 -*-
import streamlit as st
def calculate_sales_revenue(price, total_sales):
    revenue = price * total_sales
    return revenue

def main():
    st.title("Sales Revenue Calculator")

    price = st.slider("단가:", 1000, 10000, value=5000)
    st.write("가격: ", price)
    
    total_sales = st.slider("전체 판매 갯수", 1, 1000, value=500)
    st.write("판매: ", total_sales)

    if st.button("매출액 계산"): # 반환값은 True (버튼을 누른다 == T)
        revenue = calculate_sales_revenue(price, total_sales)
        st.write("전체 매출액은", revenue, "원(KRW)")


if __name__ == "__main__":
    main()