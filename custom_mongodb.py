import json
from datetime import datetime

import streamlit as st
from pymongo import MongoClient
from pymongo.server_api import ServerApi


class MongoDB:
    def __init__(self, url, db_name):
        self.client = MongoClient(url, server_api=ServerApi('1'))
        self.db = self.client[db_name]

    def read_city_coordinates(self, collection_name):
        """Read city names and their coordinates from the MongoDB collection."""
        collection = self.db[collection_name]
        cursor = collection.find({})

        city_dict = {}
        for doc in cursor:
            for feature in doc.get('features', []):
                city_name = feature.get('properties', {}).get('city')
                coordinates = feature.get('geometry', {}).get('coordinates', [None, None])

                if city_name:
                    city_dict[city_name] = coordinates

        return city_dict

    def get_city_center(self, city, city_dict):
        """Get the center point of a selected city."""
        if city in city_dict:
            return city_dict[city][1], city_dict[city][0]  # lat, lng
        else:
            raise ValueError(f"City {city} not found.")

    def read_data_from_db(self, collection_name, coordinates, max_distance, max_items, filter_conditions):
        """Read data from the database based on the specified conditions."""
        collection = self.db[collection_name]
        items = self._get_cached_data(collection, coordinates, max_distance, max_items, filter_conditions)
        return self._convert_to_geojson(items)

    def write_data_to_db(self, collection_name, project_name, lat_lng, title_url, delete=False):
        """Write data to the specified MongoDB collection."""
        collection = self.db[collection_name]

        lat, lng = self._parse_lat_lng(lat_lng)
        item = {
            'project_name': project_name,
            'lat': lat,
            'lng': lng,
            'title_url': title_url,
            'delete': delete,
            'status': 'Pending',
            'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        collection.insert_one(item)
        return item

    @staticmethod
    @st.cache_data(ttl=600)
    def _get_cached_data(_collection, coordinates, max_distance, max_items, filter_conditions):
        """Retrieve and cache data from the database."""
        query = {
            "location": {
                "$near": {
                    "$geometry": {"type": "Point", "coordinates": coordinates},
                    "$maxDistance": max_distance
                }
            },
            "类型": {"$in": filter_conditions}
        }
        return list(_collection.find(query, {"_id": 0}).sort("update_date", -1).limit(max_items))

    @staticmethod
    def _convert_to_geojson(items):
        """Convert the items to GeoJSON format."""
        features = []
        for doc in items:
            feature = {
                'type': 'Feature',
                'geometry': doc['location'],
                'properties': {k: v for k, v in doc.items() if k != 'location'}
            }
            features.append(feature)

        return json.dumps({'type': 'FeatureCollection', 'features': features})

    @staticmethod
    def _parse_lat_lng(lat_lng):
        """Parse the latitude and longitude from a string."""
        print("*****************************\n lat_lng", lat_lng)
        if lat_lng:
            lat, lng = lat_lng.replace('lat:', '').replace('lng:', '').split(',')
            return lat.strip(), lng.strip()
        return None, None
