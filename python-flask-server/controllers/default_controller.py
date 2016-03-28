
import json
from flask import request, jsonify
from Models import Building, Sensor

def buidlings_building_id_robots_delete(buildingID) -> str:
    return 'do some magic!'

def buidlings_building_id_robots_get(buildingID) -> str:
    return 'do some magic!'

def buidlings_building_id_robots_post(buildingID) -> str:
    return 'do some magic!'

def buidlings_building_id_sensors_delete(buildingID) -> str:
    return 'do some magic!'

def buidlings_building_id_sensors_get(buildingID) -> str:
    return 'do some magic!'

def buidlings_building_id_sensors_post(buildingID) -> str:
    return 'do some magic!'

def buildings_building_id_delete(buildingID) -> str:
    return 'do some magic!'

def buildings_building_id_get(buildingID) -> str:
    return 'do some magic!'

def buildings_building_id_put(buildingID, newBuilding) -> str:
    return 'do some magic!'

def robots_robot_id_delete(robotID) -> str:
    return 'do some magic!'

def robots_robot_id_get(robotID) -> str:
    return 'do some magic!'

def robots_robot_id_put(robotID, newRobot) -> str:
    return 'do some magic!'

def sensors_sensor_id_delete(sensorID) -> str:
    return 'do some magic!'

def sensors_sensor_id_get(sensorID) -> str:
    #return 'do some magic!'
    print(sensorID)
    try:
        sensor = Sensor.get(sensorID)
        print(sensor.attribute_values)
    except Exception as e:
        print(e)
        return 'Sensor with sensorId=%s does not exist.' % (sensorID)
    return sensor.attribute_values

def sensors_sensor_id_put(sensorID, newSensor) -> str:
    return 'do some magic!'

def users_user_id_delete(userID) -> str:
    return 'do some magic!'

def users_user_id_get(userID) -> str:
    return 'do some magic!'

def users_user_id_put(userID, newUser) -> str:
    return 'do some magic!'

def buildings_delete() -> str:
    return 'do some magic!'

def buildings_get() -> str:
    return 'do some magic!'

def buildings_post() -> str:
    return 'do some magic!'

def robots_delete() -> str:
    return 'do some magic!'

def robots_get() -> str:
    return 'do some magic!'

def sensors_delete() -> str:
    return 'do some magic!'

def sensors_get() -> str:
    return 'do some magic!'

def sensors_post() -> str:
    data = request.json
    print(data)
    newSens = Sensor(sensorId=data['sensorId'],
                     sensorType=data['sensorType'],
                     buildingId=data['buildingId'],
                     roomId=data['roomId'],
                     data=data['data'])
    newSens.save()
    return 'New sensor id=%s created successfully.' % (data['sensorId'])

def users_delete() -> str:
    return 'do some magic!'

def users_get() -> str:
    return 'do some magic!'

def users_post() -> str:
    return 'do some magic!'
