#!/usr/bin/env python3
import rospy
from query_service_pkg.srv import QueryStation, QueryStationResponse

# 题目给定的数据库
station_db = {
    "510000": {"name": "城市:广州", "location": "广州省"},
    "610000": {"name": "城市:成都", "location": "四川省"},
    "04547": {"name": "城市:首尔", "location": "韩国"},
    "2000": {"name": "城市:悉尼", "location": "澳大利亚"},
    "10001": {"name": "城市:纽约", "location": "美国"},
    "310000": {"name": "城市:杭州", "location": "浙江省"},
    "5003": {"name": "城市:卑尔根", "location": "瑞典"},
    "665000": {"name": "城市:普洱", "location": "云南省"},
    "710000": {"name": "城市:西安", "location": "陕西省"},
    "333000": {"name": "城市:景德镇", "location": "江西省"}
}

def handle_query(req):
    rospy.loginfo(f"收到查询请求，编号: {req.station_id}")
    if req.station_id in station_db:
        name = station_db[req.station_id]["name"]
        loc = station_db[req.station_id]["location"]
    else:
        name = "未知站点"
        loc = "未知位置"
    return QueryStationResponse(station_name=name, station_location=loc)

def server():
    rospy.init_node('station_query_server')
    s = rospy.Service('query_station_service', QueryStation, handle_query)
    rospy.loginfo("服务端已启动，等待请求...")
    rospy.spin()

if __name__ == "__main__":
    server()