import folium
from folium import plugins

# 创建一个GeoJsonTooltip对象
custom_tooltip = folium.GeoJsonTooltip(
    fields=['项目名称', '设计公司', '关键词'],
    aliases=['项目名称：', '设计公司：', '关键词：'],
    sticky=True,
    labels=True,
    localize=True,
    max_width=250,  # 设置初始的最大宽度
    max_height=100,  # 设置初始的最大高度
    max_length=500  # 设置初始的最大文本长度
)


def create_with_basemap(map_style, lat, lng, zoom_start, mapbox_config_dict):
    # 首先判断底图的选择
    if map_style == 'Mapbox':
        tiles = mapbox_config_dict["MAPBOX_TILES"]

    if map_style == 'Mapbox Street':
        tiles = mapbox_config_dict["MAPBOX_TILES_STREET"]
    else:
        tiles = 'OpenStreetMap'

    m = folium.Map(
        location=[lat, lng],
        zoom_start=zoom_start,
        tiles=tiles,
        attr=map_style,
    )
    return m


def create_map(lat, lng, city_data, mapbox_config_dict):
    m = create_with_basemap(map_style="Mapbox Street",
                            lat=lat,
                            lng=lng,
                            zoom_start=15,
                            mapbox_config_dict=mapbox_config_dict)
    # 添加定位控件
    plugins.LocateControl().add_to(m)

    # 添加全屏控件
    plugins.Fullscreen(
        position="topright",
        title="全屏",
        title_cancel="退出全屏",
        force_separate_button=True,
    ).add_to(m)

    # 将GeoJson对象载入地图
    folium.GeoJson(city_data,
                   tooltip=custom_tooltip,
                   zoom_on_click=True,
                   ).add_to(m)

    return m
