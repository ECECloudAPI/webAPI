
import json
from flask import request, jsonify
from Models import Building, Sensor, Room, Robot

#delete all robots from building
def buidlings_building_id_robots_delete(buildingId) -> str:
    return 'do some magic!'

#get all robots from a building
def buidlings_building_id_robots_get(buildingId) -> str:
    return 'do some magic!'

#create a new robot in a building
def buidlings_building_id_robots_post(buildingId) -> str:
    return 'do some magic!'

#delete all sensors in a building
def buidlings_building_id_sensors_delete(buildingId) -> str:
    return 'do some magic!'

#get all sensors in a building
def buidlings_building_id_sensors_get(buildingId) -> str:
    return 'do some magic!'

#post a new sensors to a building
def buidlings_building_id_sensors_post(buildingId) -> str:
    return 'do some magic!'

#delete a building
def buildings_building_id_delete(buildingId) -> str:
    return 'do some magic!'

#get a building
def buildings_building_id_get(buildingId) -> str:
    return 'wow'
    #return jsonify(Building.get(int(buildingId)))

#update a building
def buildings_building_id_put(buildingId) -> str:
    return 'do some magic!'

#delete all buildings
def buildings_delete() -> str:
    return 'do some magic!'

#create a new building
def buildings_post() -> str:
    data = request.json
    print(data)
    newBuilding = Building(id=data['id'],
                           buildingId=data['buildingId'],
                           building=data['building'],
                           rooms=data['rooms'],
                           owner=data['owner'],
                           users=data['users'],
                           sensors=data['sensors'],
                           robots=data['robots'])
    newBuilding.save()
    return 'New building id=%s created successfully' % (data['id'])

#delete all robots
def robots_delete() -> str:
    return 'do some magic!'

#get all robots
def robots_get() -> str:
    return 'do some magic!'

#delete a robot by ID
def robots_robot_id_delete(robotId) -> str:
    return 'do some magic!'

#get a robot by ID
def robots_robot_id_get(robotId) -> str:
    return 'do some magic!'

#update a robot
def robots_robot_id_put(robotId) -> str:
    return 'do some magic!'

#delete all sensors
def sensors_delete() -> str:
    return 'do some magic!'

#get all sensors
def sensors_get() -> str:
    return 'get all sensors!'

#create a new sensor
def sensors_post() -> str:
    data = request.json
    print(data)
    newSens = Sensor(sensorId=data['sensorId'],
                     sensorType=data['sensorType'],
                     buildingId=data['buildingId'],
                     roomId=data['roomId'],
                     data=data['data'])
    newSens.save()
    return 'New sensor id=%s created successfully' % (data['sensorId'])

#delete a single sensor
def sensors_sensor_id_delete(sensorId) -> str:
    return 'do some magic!'

#get a single sensor
def sensors_sensor_id_get(sensorId) -> str:
    #return jsonify(Sensor.get(sensorId))
    return 'get one sensor!'

#update a single sensor
def sensors_sensor_id_put(sensorId) -> str:
    return 'do some magic!'

#delete all users
def users_delete() -> str:
    return 'do some magic!'

#get all users
def users_get() -> str:
    return 'do some magic!'

#create a new user
def users_post() -> str:
    return 'post user!'

#delete a single user
def users_user_id_delete(userId) -> str:
    return 'do some magic!'

#get a single user
def users_user_id_get(userId) -> str:
    return 'get one user!'

 #update a single user
def users_user_id_put(userId) -> str:
    return 'do some magic!'
