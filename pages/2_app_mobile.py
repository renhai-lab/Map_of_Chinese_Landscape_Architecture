from data_functions import *
from folium import plugins
from map_config import *
from custom_mongodb import *
from streamlit_folium import st_folium

st.set_page_config(
    page_title="中国网红建筑景观项目地图 Home",
    page_icon=":world_map:",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://github.com/renhaiidea/Landscape_Architecture_Streamlit_Web_Display',
        'Report a bug': "https://github.com/renhaiidea/Landscape_Architecture_Streamlit_Web_Display/issues",
        'About': " ## 有疑问请发送邮件到：leew71274@gmail.com",
    }
)


"## :world_map: 中国网红建筑景观项目地图"

# 初始化数据
# 加载城市列表
city_center = read_city()
city_list = city_center.index.tolist()
default_city_index = city_list.index('上海市')  # 默认选择第一个城市:上海市
# 加载数据库
mgdb = MongoDB("landscape_db")
collection_name_point = st.secrets['mongo_remote']["collection_name_point"]
collection_name_fb = st.secrets['mongo_remote']["collection_name_fb"]

# 筛选查询框
left1, right1 = st.columns([3, 2])
# 三个类别的筛选框
u1, u2, u3 = left1.columns([3, 4, 3])
# 城市选择框
city = u1.selectbox(
    ':pushpin: 请选择城市',
    city_list,
    index=default_city_index,
    key='city')
# 项目类型选择框
kind = u2.multiselect(
    ':pushpin: 选择项目类型',
    ['景观', '建筑', '室内'],
    ['景观', '建筑', '室内'], )
# 展示数量选择框
default_num=st.secrets['config']["default_num"]
max_num = st.secrets['config']["max_num"]
slide_value = u3.slider(
    ':pushpin: 选择展示数量',
    min_value=1,
    max_value=max_num,
    value=default_num,
    step=99,
    key='default_num')

# 地图处理模块
lat, lng = get_center(city) # 获取选中城市的中心点
# 调用函数获取数据库数据并转换为 GeoJSON 格式
city_data = mgdb.read_from_db(collection_name=collection_name_point,
                               coordinates=tuple([lng, lat]),
                               max_distance=60000,
                               default_num=slide_value,
                               filter=kind)
# 设置缩放级别
zoom_start = 11

# 绘制folium地图 > m
## 首先判断地图的选择
map_style = "Mapbox Street" # TODO 添加更多地图选择
if map_style == 'Mapbox':
    MAPBOX_TILES = st.secrets['others']["MAPBOX_TILES"]
    m = folium.Map(
        location=[lat, lng],
        zoom_start=zoom_start,
        tiles=MAPBOX_TILES,
        attr=map_style,
    )
if map_style == 'Mapbox Street':
    MAPBOX_TILES = st.secrets['others']["MAPBOX_TILES_STREET"]
    m = folium.Map(
        location=[lat, lng],
        zoom_start=zoom_start,
        tiles=MAPBOX_TILES,
        attr=map_style,
    )
else:
    m = folium.Map(
        location=[lat, lng],
        zoom_start=zoom_start,
        tiles='OpenStreetMap', # 访问不稳定?
    )

# 添加定位控件
plugins.LocateControl().add_to(m)

# 添加全屏控件
plugins.Fullscreen(
    position="topright",
    title="全屏",
    title_cancel="退出全屏",
    force_separate_button=True,
).add_to(m)

# 创建一个GeoJson对象载入地图
geojson = folium.GeoJson(city_data,
                         tooltip=tooltip,
                         # popup=popup,
                         # style_function=style_function,
                         # highlight_function=highlight_function,
                         # marker=folium.Marker(icon=folium.Icon()),
                         zoom_on_click=True,
                         ).add_to(m)

# 总体布局分栏
# left1, right2 = st.columns(2)

# 渲染地图
with left1:
    # 渲染
    st_data = st_folium(m,
                        key="map",
                        height=360,
                        use_container_width=True)


# mobile把反馈和删除le
# col1, col2 = st.columns(2)
# # 加入反馈复选框
# fb_button = col1.checkbox(label=':loudspeaker: 提交新位置', value=False, key='fb_button',
#                         help='如果您发现项目位置不准确，请选中项目后在此处留言', disabled=False)
# # 加入删除位置复选框
# del_button = col2.checkbox(label=':heavy_exclamation_mark: 删除位置', value=False, key='del_button',
#                          help='如果难以确认地址则删除位置', disabled=False)
#
# # 复选框逻辑判断
# # 如果提交反馈和删除位置有一个被选中，执行以下代码
# if del_button or fb_button:
#     # 获取地图上的点击事件
#     last_active_drawing = st_data.get("last_active_drawing", None)
#
#     if last_active_drawing: # 如果有点击事件
#         project_name, title_url = get_click_info(last_active_drawing)
#     else:
#         project_name = None
#         title_url = None
#
#     # 启动推送
#     pushkey = st.secrets["others"]["pushkey"]
#     pushdeer = PushDeer(pushkey=pushkey)
#
#
#     # 如果反馈被选中
#     if fb_button:
#         if project_name is None:
#             col1.markdown('> :red[请首先选择地图上的项目]')
#         else:
#             text1 = col1.text_input(
#                 "**1.要提交项目名称：**",
#                 project_name,
#                 key="placeholder1"
#             )
#
#             # 获取新的经纬度
#             try:
#                 last_clicked = st_data.get("last_clicked", None)
#                 lat = last_clicked['lat']
#                 lng = last_clicked['lng']
#
#             except:
#                 lat = None
#                 lng = None
#
#             # 获取旧经纬度
#             try:
#                 last_active_drawing = st_data.get("last_active_drawing", None)
#                 old_lat = last_active_drawing['geometry']['coordinates'][1]
#                 old_lng = last_active_drawing['geometry']['coordinates'][0]
#             except:
#                 old_lat = None
#                 old_lng = None
#
#             if last_clicked is None or (old_lng == lng or old_lat == lat):
#                 col1.markdown('> 请点击地图将:red[自动更新]下方经纬度')
#                 title = '2.经纬度:red[**未更新**,请点击地图将自动更新下方经纬度]'
#             else:
#                 _text = "2.地理坐标**已更新**（点击地图将会自动更新下方经纬度）："
#                 title =  _text
#
#                 text2 = col1.text_input(
#                     title,
#                     f"Latitude: {round(lat, 6)}, Longitude: {round(lng, 6)}",
#                     key="placeholder2",
#                 )
#                 # 提交反馈
#                 if project_name is not None and title == _text:
#                     if col1.button(":arrow_right: 提交反馈"):
#                         # 写入数据库
#                         item = mgdb.write_to_db(collection_name=collection_name_fb,
#                                          project_name=project_name,
#                                          lat_lng=text2,
#                                          title_url=title_url)
#
#                         col1.write(":blush: 提交成功，感谢您的反馈！")
#                         # 推送
#                         pushdeer.send_text("streamlit 数据写入成功", desp=f"{item}")
#
#     # 如果删除位置被选中
#     else:
#         # 获取点击的项目信息
#         if project_name is None:
#             col1.markdown('> :red[请首先选择地图上的项目]')
#         else:
#             text1 = col1.text_input(
#                 "**要删除的项目名称：**",
#                 project_name,
#                 key="placeholder1"
#             )
#             if col1.button(":arrow_right: 提交反馈"):
#
#                 # 写入数据库
#                 item = mgdb.write_to_db(collection_name=collection_name_fb,
#                                         project_name=project_name,
#                                         lat_lng=text1,
#                                         title_url=title_url)
#
#                 col1.write(":blush: 提交成功，感谢您的反馈！")
#                 # 推送
#                 pushdeer.send_text("streamlit 数据写入成功", desp=f"{item}")

# 右侧栏
with right1:
    # 获取地图上的点击事件
    last_active_drawing = st_data.get("last_active_drawing", None)
    # 如果有点击事件
    if last_active_drawing:
        # 获取点击的数据
        single_df, image, title_url, project_name, company, feature = get_info_map(last_active_drawing)
        right1.markdown(
            f"""
            <div style='text-align: center;'>
                <h3>{project_name}</h3>
                <p>设计公司（团队）：{company}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        right1.markdown(f'> 项目特点：{feature}')
        if not pd.isna(image):
            right1.image(image, caption=f'{project_name}', use_column_width='auto')

        right1.dataframe(single_df, height=250, use_container_width=True)


    else:
        right1.write('请点击地图上的点查看详细信息')

st.markdown(
    """
    <br>
    <a href="app_desktop" target="_self">更多信息:请点击电脑版查看</a><br>
    <br>
    <p style="text-align: left;">👈 本项目数据收集于网络，方便自用，仅供交流学习！如有侵权，请联系删除！</p>
    """,
    unsafe_allow_html=True
)