from streamlit_folium import st_folium

from config import setup_page_config, footer
from data_functions import *
from map_config import create_map

setup_page_config()
st.markdown(
    f"""
    <div style='text-align: center;'>
        <h1>中国建筑景观地图：互动式探索</h1>
        <p>Interactive Map of Chinese Landscape Architecture</p>
    </div>
    """,
    unsafe_allow_html=True)

# 初始化数据库
mg_db = initialize_mongodb()

# 加载城市列表
city_dict, city_list, default_index = get_city_data(mg_db, st.secrets['mongo_remote']["city_points"])

# 三个类别的筛选框
u1, u2, u3 = st.columns([3, 4, 3])
# 城市选择框
city = u1.selectbox(
    ':pushpin: 请选择城市',
    city_list,
    index=default_index,
    key='city')
# 项目类型选择框
kind = u2.multiselect(
    ':pushpin: 选择项目类型',
    ['景观', '建筑', '室内'],
    ['景观', '建筑', '室内'], )

# 展示数量选择框
default_num = st.secrets['config']["default_num"]
max_num = st.secrets['config']["max_num"]
slide_value = u3.slider(
    ':pushpin: 选择展示数量',
    min_value=1,
    max_value=max_num,
    value=default_num,
    step=99,
    key='default_num')

# 地图处理模块
lat, lng = mg_db.get_city_center(city, city_dict)  # 获取选中城市的中心点

# 调用函数获取数据库数据并转换为 GeoJSON 格式
city_data = mg_db.read_data_from_db(projects_points,
                                    coordinates=tuple([lng, lat]),
                                    max_distance=8000,  # 单位：米
                                    max_items=slide_value,
                                    filter_conditions=kind)

# 绘制folium地图 > m
# 创建地图
mapbox_config_dict = st.secrets['others']
m = create_map(lat, lng, city_data, mapbox_config_dict)

# 渲染地图
st_data = st_folium(m,
                    key="map",
                    height=600,
                    use_container_width=True)

last_active_drawing = get_last_active_drawing(st_data)
if last_active_drawing:
    detail_info, image, title_url, project_name, company, feature = get_info_map(last_active_drawing)

    st.markdown(
        f"<div style='text-align: center;'><h3>{project_name}</h3><p>设计公司（团队）：{company}</p></div>",
        unsafe_allow_html=True)
    st.markdown(f'> 项目特点：{feature}')

    if image:
        st.image(image, caption=project_name, use_column_width=True)

    # 使用 st.markdown 显示表格
    markdown_table = create_markdown_table(detail_info)
    st.markdown(markdown_table, unsafe_allow_html=True)

else:
    st.write('请点击地图上的点查看详细信息')

footer()
