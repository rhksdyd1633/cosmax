import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="급똥열차 - 개찰구 안 화장실 안내",
    page_icon="🚽",
    layout="centered",
)

# 스트림릿 기본 여백/헤더를 최대한 없애서 원본 HTML 디자인이 꽉 차게 보이도록 조정
st.markdown(
    """
    <style>
        .block-container { padding: 0 !important; max-width: 100% !important; }
        header[data-testid="stHeader"] { display: none; }
        #MainMenu, footer { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)

HTML_FILE = Path(__file__).parent / "geuptong_train.html"
html_content = HTML_FILE.read_text(encoding="utf-8")

# 원본 HTML/CSS/JS를 그대로 iframe에 렌더링
components.html(html_content, height=1600, scrolling=True)
