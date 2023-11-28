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
            'About': " ## 有疑问请联系微信信公众号：renhai-lab",
        }
    )


def footer():
    st.markdown(
        """
        ---
        <br>
        <p style="text-align: left; color: #a3a2a2;">免责声明：本项目数据收集于网络，方便自用，仅供交流学习！如有侵权，请联系删除！
        <br>提示：如果获取的项目地址不够详细，那么坐标点则不准确。
        <br>数据更新时间：2023年8月。
        </p>
        """,
        unsafe_allow_html=True
    )
