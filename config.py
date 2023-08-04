import streamlit as st




# streamlit页面通用参数
def setup_page_config():
    st.set_page_config(
        page_title="中国网红建筑景观项目地图 Home",
        page_icon=":world_map:",
        layout="wide",
        initial_sidebar_state="collapsed",
        menu_items={
            'Get Help': 'https://github.com/renhaiidea/Landscape_Architecture_Streamlit_Web_Display',
            'Report a bug': "https://github.com/renhaiidea/Landscape_Architecture_Streamlit_Web_Display/issues",
            'About': " ## 有疑问请发送邮件到：leew71274@gmail.com",
        }
    )


def footer():
    st.markdown(
        """
        <br>
        <a href="app_mobile" target="_self">📱 移动端网页（维护中）</a><br>
        <p style="text-align: left;">本项目数据收集于网络，方便自用，仅供交流学习！如有侵权，请联系删除！</p>
        """,
        unsafe_allow_html=True
    )