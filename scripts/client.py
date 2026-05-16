#!/usr/bin/env python3
import sys
import rospy
from query_service_pkg.srv import QueryStation, QueryStationRequest

def query_station(station_id):
    rospy.init_node('station_query_client', anonymous=True)
    rospy.wait_for_service('query_station_service')
    try:
        proxy = rospy.ServiceProxy('query_station_service', QueryStation)
        resp = proxy(station_id)
        return resp.station_name, resp.station_location
    except rospy.ServiceException as e:
        rospy.logerr(f"调用失败: {e}")
        return None, None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使用方法: rosrun query_service_pkg client.py <station_id>")
        sys.exit(1)
    
    station_id = sys.argv[1]
    name, location = query_station(station_id)
    
    if name is not None and location is not None:
        print("="*30)
        print("      站点查询结果")
        print("="*30)
        print(f"编号: {station_id}")
        print(f"名称: {name}")
        print(f"位置: {location}")
        print("="*30)