#  中国景观建筑交互地图
> landscape_architecture_streamlit_web_display

本项目是通过Python的[streamlit](https://streamlit.io/)包构建网页，用于展示中国建筑、景观、室内等设计作品，可以通过网页地图浏览附近有哪些项目，点击地图标记可以获取摘要信息，也可以点击跳转到源网页。

## 1.成果展示 

### 1）网页入口（遇到无法加载的情况请挂梯子）
- [🏠 导航页](https://landscape-architecture-app-webdisplay.streamlit.app/)

  ![Homepage](https://image-1315363329.cos.ap-shanghai.myqcloud.com/github_repo/202308042205358.gif)

- [💻 电脑端网页](https://landscape-architecture-app-webdisplay.streamlit.app/app_desktop)

  ![desktop](https://image-1315363329.cos.ap-shanghai.myqcloud.com/github_repo/202308042205399.gif)

- [📱 移动端网页](https://landscape-architecture-app-webdisplay.streamlit.app/app_mobile)

### 2）实现的功能
1. **地图查询**
     基于openstreetmap地图，[streamlit-folium加载地图组件，[MongoDB Atlas](https://www.mongodb.com/zh-cn/atlas)数据库提供空间数据的查询和储存。




1. **实现对城市、项目类别以及展示数量的筛选**

   <img src="https://image-1315363329.cos.ap-shanghai.myqcloud.com/github_repo/202308042205010.png" alt="image-20230804164738151" style="zoom:50%;" />

2. **地图的项目点与项目图、项目表格连动展示**

4. **chatgpt总结项目特点**

5. **项目位置反馈**

	定位不一定准确，如发现定位不准确请在网页端提交反馈。包含提交**新位置**和**删除位置**：
​	- 请首先选择地图上的项目，然后点击地图将自动更新经纬度，最后提交链接。
​	- 或者因为项目特殊性或者原文未提及位置，则直接删除位置。
​	![image-20230708013654794](https://image-1315363329.cos.ap-shanghai.myqcloud.com/github_repo/202308042205989.png)


## 写在最后
本项目数据收集于网络，方便自用，仅供交流学习！如有侵权，请联系删除！

## TODO
- [ ] 优化网页端显示效果
- [ ] 页面载入自定义组件bug
- [ ] 解决有些图片未能显示的问题

