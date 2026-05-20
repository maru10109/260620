import streamlit as st
import time
from datetime import datetime

# 페이지 설정
st.set_page_config(
    page_title="어머나 세상에!",
    page_icon="🦸‍♂️",
    layout="wide"
)

# 커스텀 CSS로 스타일링
st.markdown("""
    <style>
    .main-title {
        font-size: 60px;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(90deg, #ff6b6b, #feca57, #48dbfb, #ff9ff3);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: rainbow 3s ease infinite;
    }
    @keyframes rainbow {
        0%, 100% { filter: hue-rotate(0deg); }
        50% { filter: hue-rotate(180deg); }
    }
    .big-emoji {
        font-size: 80px;
        text-align: center;
        animation: bounce 1s infinite;
    }
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-20px); }
    }
    .stButton>button {
        background: linear-gradient(90deg, #ff6b6b, #feca57);
        color: white;
        font-size: 20px;
        font-weight: bold;
        border-radius: 20px;
        padding: 10px 30px;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# 메인 타이틀
st.markdown('<p class="main-title">✨ 어머나 세상에 ✨</p>', unsafe_allow_html=True)
st.markdown('<p class="big-emoji">🤦‍♂️ 🤦‍♀️ 🦸‍♂️</p>', unsafe_allow_html=True)

st.markdown("---")

# 사이드바
with st.sidebar:
    st.header("🎛️ 컨트롤 패널")
    name = st.text_input("이름을 입력하세요", "당곡인")
    mood = st.select_slider(
        "오늘 기분은?",
        options=["😭", "😢", "😐", "😊", "🤩"],
        value="😊"
    )
    surprise_level = st.slider("놀람 레벨", 1, 100, 50)

# 컬럼 레이아웃
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("놀람 지수", f"{surprise_level}%", f"+{surprise_level-50}")
with col2:
    st.metric("현재 기분", mood)
with col3:
    st.metric("현재 시각", datetime.now().strftime("%H:%M:%S"))

st.markdown("---")

# 인터랙티브 버튼
st.subheader(f"👋 {name}님, 환영합니다!")

if st.button("🎉 마법의 버튼을 눌러보세요!"):
    with st.spinner("두구두구..."):
        time.sleep(1)
    st.balloons()
    st.success(f"헉!!! {name}님 진짜 기깔나네요! 🦸‍♂️✨")
    st.snow()

# 탭 구성
tab1, tab2, tab3 = st.tabs(["📢 놀람 표현", "🎨 갤러리", "💬 메시지"])

with tab1:
    st.write("### 놀람 강도별 표현")
    if surprise_level < 30:
        st.info("😯 어? 그래?")
    elif surprise_level < 70:
        st.warning("😲 헉! 진짜??")
    else:
        st.error("🤯 어머나 세상에에에엥!!!")

with tab2:
    st.write("### 이모지 갤러리")
    emojis = ["🤦‍♂️", "🤦‍♀️", "🦸‍♂️", "🦸‍♀️", "🥳", "🤩", "😱", "🤯"]
    cols = st.columns(4)
    for i, emoji in enumerate(emojis):
        with cols[i % 4]:
            st.markdown(f"<p style='font-size:60px; text-align:center;'>{emoji}</p>", 
                        unsafe_allow_html=True)

with tab3:
    message = st.text_area("하고 싶은 말을 적어보세요!", "헉!!🦸‍♂️")
    if st.button("전송 💌"):
        st.success(f"💌 메시지: {message}")
        st.toast("메시지가 전송되었어요!", icon="✅")

st.markdown("---")
st.caption("Made with ❤️ by 당곡고 학생")
