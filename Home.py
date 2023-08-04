import streamlit as st

st.set_page_config(
    page_title="中国网红建筑景观项目地图 Home",
    page_icon=":world_map:",
    layout="centered",
    menu_items={
        'Get Help': 'https://github.com/renhaiidea/Landscape_Architecture_Streamlit_Web_Display',
        'Report a bug': "https://github.com/renhaiidea/Landscape_Architecture_Streamlit_Web_Display/issues",
        'About': " ## 有疑问请发送邮件到：leew71274@gmail.com",
    }
)
st.markdown(
    f"""
    <div style='text-align: center;'>
        <h1>🗺 中国网红建筑景观项目地图</h1>
        <p>请根据使用情况选择页面, 或者点击左侧侧边栏访问</p>
    </div>
    """,
    unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])




col1.markdown(
    """
    <div style='text-align: center;'>
          <a href="app_desktop" target="_self">
            <img src="./app/static/computer.gif" height="200" >
        </a>
        <p>👆 电脑端</p>
    </div>
    """,
    unsafe_allow_html=True
)

col2.markdown(
    """
    <div style='text-align: center;'>
          <a href="app_mobile" target="_self">
            <img src="./app/static/Phone-with-map-and-geolocation.gif" height="200" >
        </a>
        <p>👆 移动端(维护中，使用电脑端)</p>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("---")
# st.write(
#     "Share on social media with the hashtag [#prettymaps](https://twitter.com/search?q=%23prettymaps&src=typed_query) !"
# )
st.markdown(
    "更多信息请访问 :star: : [github](https://github.com/renhaiidea/Landscape_Architecture_Streamlit_Web_Display)"
)