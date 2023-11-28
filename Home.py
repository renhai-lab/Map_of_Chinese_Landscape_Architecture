import streamlit as st
from config import setup_page_config

setup_page_config()

st.markdown(
    f"""
    <div style='text-align: center;'>
        <h1>中国建筑景观地图：互动式景观探索</h1>
        <p>Interactive Map of Chinese Landscape Architecture</p>
    </div>
    """,
    unsafe_allow_html=True)

st.markdown(
    """
    <div style='text-align: center;'>
          <a href="app_desktop" target="_self">
            <img src="./app/static/cover.png" height="200" >
            <p>点击体验吧！</p>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

st.markdown(
    """
    ## 项目简介 | Project Introduction
    
    本项目利用Python的[streamlit](https://streamlit.io/)包创建一个交互式网页，创建了一个交互式网页，专门展示中国的建筑、景观和室内设计作品。
    
    > Streamlit是一个强大的工具，它允许Python开发者快速构建网页应用，特别适合那些熟悉Python但不太了解网页编程语言的用户。
    
    借助地图，用户可以轻松地在地图上浏览附近的设计项目，并通过点击地图上的标记来获取每个项目的摘要信息。
    
    此外，用户还可以点击详情链接，访问每个项目的源网页，以获得更全面的信息。   
    
    ## 更多信息 | More Info
    如果你还有其他问题，可以在我的博客评论或者微信私信我。
    
    - [我的博客](https://cdn.renhai-lab.tech/)
    - [我的GITHUB](https://github.com/renhai-lab)
    - [我的GITEE](https://gitee.com/renhai-lab)
    - 微信公众号: renhai-lab
    - [我的知乎](https://www.zhihu.com/people/Ing_ideas)
    
    <img src="https://cdn.renhai-lab.tech/upload/logo2.jpg" alt="更多账号" style="zoom:50%;" />
    
    ## 免责声明 | Disclaimer
    
    > 本项目数据来源于网络，主要用于个人学习和研究，如有侵权，请联系删除。
    
    """
    , unsafe_allow_html=True)
