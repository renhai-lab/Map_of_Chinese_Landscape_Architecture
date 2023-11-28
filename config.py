import streamlit as st


# streamlit页面通用参数
def setup_page_config():
    st.set_page_config(
        page_title="中国建筑景观地图：互动式景观探索 Home",
        page_icon=":world_map:",
        layout="centered",
        initial_sidebar_state="collapsed",
        menu_items={
            'Get Help': 'https://github.com/renhai-lab/Map_of_Chinese_Landscape_Architecture',
            'Report a bug': "https://github.com/renhai-lab/Map_of_Chinese_Landscape_Architecture/issues",
            'About': " ## 有疑问请发送邮件到：renhailab@163.com或者关注微信公众号renhai-lab",
        }
    )


def footer():
    st.markdown(
        """
        <br>
        <p style="text-align: left;">本项目数据收集于网络，方便自用，仅供交流学习！如有侵权，请联系删除！</p>
        """,
        unsafe_allow_html=True
    )
