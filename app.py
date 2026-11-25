
import random
import streamlit as st

# 웹앱 제목
st.title("🎨 오늘의 색상 추천")
st.write("버튼을 누르면 어울리는 색상 조합을 추천해 드립니다!")

# 색상 조합 목록
color_combinations = [
    ["#FFB6C1", "#FFC0CB", "#FFFFFF"],
    ["#87CEEB", "#4682B4", "#F0F8FF"],
    ["#98FB98", "#2E8B57", "#F5FFFA"],
    ["#FFD700", "#FFA500", "#FFF8DC"],
    ["#DDA0DD", "#9370DB", "#F8F0FF"],
    ["#FF7F50", "#FA8072", "#FFF0E5"],
    ["#808080", "#2F4F4F", "#D3D3D3"]
]

# 버튼 만들기
if st.button("✨ 어울리는 색상 추천받기"):

    # 무작위 색상 조합 선택
    selected_colors = random.choice(color_combinations)

    st.subheader("🌈 추천 색상 조합")

    # 색상 출력
    for color in selected_colors:
        st.markdown(
            f"""
            <div style="
                background-color: {color};
                padding: 25px;
                border-radius: 10px;
                margin: 10px 0;
                color: black;
                font-weight: bold;
                text-align: center;">
                {color}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.success("오늘의 색상 추천이 완료되었습니다!")
