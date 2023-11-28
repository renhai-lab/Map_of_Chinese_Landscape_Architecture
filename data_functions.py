# import geopandas as gpd
import requests
import streamlit as st
# 导入随机UA
from fake_useragent import UserAgent

from custom_mongodb import MongoDB

# 数据库参数
city_points = st.secrets['mongo_remote']["city_points"]
projects_points = st.secrets['mongo_remote']["project_points"]
project_points_fb = st.secrets['mongo_remote']["project_points_fb"]
# 随机UA
ua = UserAgent()


def initialize_mongodb():
    """Initialize MongoDB instance."""
    url = st.secrets["mongo_remote"]["MONGO_REMOTE_URL"]
    db_name = st.secrets['mongo_remote']["db_name"]
    return MongoDB(url, db_name)


def get_city_data(mg_db, city_points):
    """获取城市数据"""
    city_dict = mg_db.read_city_coordinates(collection_name=city_points)
    city_list = list(city_dict.keys())
    default_index = city_list.index('上海市')  # 默认选择上海市
    return city_dict, city_list, default_index


@st.cache_data(ttl=600)
def get_last_active_drawing(st_data):
    last_active_drawing = st_data.get("last_active_drawing")
    if last_active_drawing:
        return last_active_drawing
    return None


@st._cache_data
def get_name_and_title_url(json_data):
    """获取点击的数据"""
    project_name = json_data['properties']['项目名称']
    title_url = json_data['properties']['标题链接']
    return project_name, title_url


@st.cache_data(ttl=600)
def get_info_map(json_data):
    properties = json_data["properties"]

    # 直接从 properties 中提取所需数据
    image_url = properties.get("封面")
    title_url = properties.get("标题链接")
    project_name = properties.get("项目名称")
    company = properties.get("设计公司")
    feature = properties.get("项目特点")

    # 创建一个包含所需详细信息的字典
    detail_info = {
        '链接': title_url,
        '景观设计团队': properties.get('景观设计团队'),
        '设计师/设计团队': properties.get('设计师/设计团队'),
        '设计时间/开始时间': properties.get('设计时间/开始时间'),
        '完成年份': properties.get('完成年份'),
        '占地面积(平方米)': properties.get('占地面积(平方米)'),
        '建筑面积(平方米)': properties.get('建筑面积(平方米)'),
        '项目地址': properties.get('项目地址'),
        '业主单位': properties.get('业主单位'),
        '更新日期': properties.get('更新日期'),
        '位置可信度_0_1': properties.get('位置可信度_0_1')
    }

    # 过滤掉值为 None 的键 并且转置
    filtered_info = [{"key": key, "Value": value} for key, value in detail_info.items() if value is not None]
    # 获取图片
    image = fetch_image_with_headers(image_url) if image_url else None

    return filtered_info, image, title_url, project_name, company, feature


def fetch_image_with_headers(url):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Dnt": "1",
        "User-Agent": ua.random,
    }
    response = requests.get(url, headers=headers)
    return response.content if response.status_code == 200 else None


def create_markdown_table(detail_info):
    table = "| 名称 | 说明 |\n| --- | --- |\n"
    for item in detail_info:
        key, value = item['key'], item['Value']

        # 检查值是否为URL，如果是，则将其格式化为Markdown超链接
        if isinstance(value, str) and value.startswith("http"):
            value = f"[查看详情]({value})"

        table += f"| **{key}** | {value} |\n"
    return table
