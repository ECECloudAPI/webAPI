
import json
import uuid
from flask import request, jsonify
from storageModels import Building, Sensor, User, Robot

def buildings_building_id_robots_delete(buildingID) -> str:
    resultList = []
    for item in Robot.scan(buildingID__eq=buildingID):
        resultList.append(item.delete())
    return "%s items deleted." % len(resultList)

def buildings_building_id_robots_get(buildingID) -> str:
    resultList = []
    for item in Robot.scan(buildingID__eq=buildingID):
        resultList.append(item.attribute_values)
    return ( resultList )

def buildings_building_id_robots_post(buildingID) -> str:
    try:
        building = Building.get(buildingID)
    except Exception as e:
        print(e)
        return 'Building with id %s does not exist.' % (buildingID)
    newID = str(uuid.uuid4())
    newObj = Robot(id=newID, buildingID=buildingID)
    newObj.save()
    return newObj.attribute_values

def buildings_building_id_sensors_delete(buildingID) -> str:
    resultList = []
    for item in Sensor.scan(buildingID__eq=buildingID):
        resultList.append(item.delete())
    return "%s items deleted." % len(resultList)

def buildings_building_id_sensors_get(buildingID) -> str:
    resultList = []
    for item in Sensor.scan(buildingID__eq=buildingID):
        resultList.append(item.attribute_values)
    return ( resultList )

def buildings_building_id_sensors_post(buildingID) -> str:
    try:
        building = Building.get(buildingID)
    except Exception as e:
        print(e)
        return 'Building with id=%s does not exist.' % (buildingID)
    newID = str(uuid.uuid4())
    newObj = Sensor(id=newID, buildingID=buildingID)
    newObj.save()
    return newObj.attribute_values

def buildings_building_id_delete(buildingID) -> str:
    try:
        building = Building.get(buildingID)
        building.delete()
    except Exception as e:
        return 'Building with id=%s does not exist.' % (buildingID)
    return 'Successfully deleted buildingID=%s.' % (buildingID)

def buildings_building_id_get(buildingID) -> str:
    try:
        building = Building.get(buildingID)
    except Exception as e:
        print(e)
        return 'Building with id=%s does not exist.' % (buildingID)
    return building.attribute_values

def buildings_building_id_put(buildingID, newBuilding) -> str:
    try:
        building = Building.get(buildingID)
    except Exception as e:
        return 'Building with id=%s does not exist.' % (buildingID)
    attributes = building.attribute_values.keys()
    for key in newBuilding.keys():
        if key in attributes and key is not 'id':
            building.update_item(key, value=newBuilding[key], action='PUT')
    return 'Building with id=%s updated successfully.' % (buildingID)

def robots_robot_id_delete(robotID) -> str:
    try:
        robot = Robot.get(robotID)
        robot.delete()
    except Exception as e:      
        return 'Robot with id=%s does not exist.' % (robotID)
    return 'Successfully deleted robot with id=%s.' % (robotID)

def robots_robot_id_get(robotID) -> str:
    try:
        robot = Robot.get(robotID)
    except Exception as e:
        return 'Robot with id=%s does not exist.' % (robotID)
    return robot.attribute_values

def robots_robot_id_put(robotID, newRobot) -> str:
    try:
        robot = Robot.get(robotID)
    except Exception as e:
        return 'Robot with id=%s does not exist.' % (robotID)
    attributes = robot.attribute_values.keys()
    for key in newRobot.keys():
        if key in attributes and key is not 'id':
            robot.update_item(key, value=newRobot[key], action='PUT')
    return 'Robot with id=%s updated successfully.' % (robotID)

def sensors_sensor_id_delete(sensorID) -> str:
    try:
        sensor = Sensor.get(sensorID)
        sensor.delete()
    except Exception as e:
        return 'Sensor with id=%s does not exist.' % (sensorID)
    return 'Successfully deleted sensor with id=%s.' % (sensorID)

def sensors_sensor_id_get(sensorID) -> str:
    try:
        sensor = Sensor.get(sensorID)
    except Exception as e:
        return 'Sensor with id=%s does not exist.' % (sensorID)
    return sensor.attribute_values

def sensors_sensor_id_put(sensorID, newSensor) -> str:
    try:
        sensor = Sensor.get(sensorID)
    except Exception as e:
        return 'Sensor with id=%s does not exist.' % (sensorID)
    attributes = sensor.attribute_values.keys()
    for key in newSensor.keys():
        if key in attributes and key is not 'id':
            sensor.update_item(key, value=newSensor[key], action='PUT')
    return 'Sensor with id=%s updated successfully.' % (sensorID)

def users_user_id_delete(userID) -> str:
    try:
        user = User.get(userID)
        user.delete()
    except Exception as e:      
        return 'User with id=%s does not exist.' % (userID)
    return 'Successfully deleted user with id=%s.' % (userID)

def users_user_id_get(userID) -> str:
    try:
        user = User.get(userID)
    except Exception as e:
        return 'User with id=%s does not exist.' % (userID)
    return user.attribute_values

def users_user_id_put(userID, newUser) -> str:
    try:
        user = User.get(userID)
    except Exception as e:
        return 'User with id=%s does not exist.' % (userID)
    attributes = user.attribute_values.keys()
    for key in newUser.keys():
        if key in attributes and key is not 'id':
            user.update_item(key, value=newUser[key], action='PUT')
    return 'User with id=%s updated successfully.' % (userID)

def buildings_delete() -> str:
    temp = []
    for item in Building.scan():
        temp.append(item.delete())
    return "%s items deleted." % len(temp)

def buildings_get() -> str:
    resultList = []
    for item in Building.scan():
        resultList.append(item.attribute_values)
    return resultList

def buildings_post() -> str:
    newID = str(uuid.uuid4())
    newObj = Building(id=newID)
    newObj.save()
    return newObj.attribute_values

def robots_delete() -> str:
    temp = []
    for item in Robot.scan():
        temp.append(item.delete())
    return "%s items deleted." % len(temp)

def robots_get() -> str:
    resultList = []
    for item in Robot.scan():
        resultList.append(item.attribute_values)
    return resultList

def sensors_delete() -> str:
    temp = []
    for item in Sensor.scan():
        temp.append(item.delete())
    return "%s items deleted." % len(temp)

def sensors_get() -> str:
    resultList = []
    for item in Sensor.scan():
        resultList.append(item.attribute_values)
    return resultList

def sensors_post() -> str:
    newID = str(uuid.uuid4())
    sensorObj = Sensor(id=newID)
    sensorObj.save()
    return sensorObj.attribute_values

def users_delete() -> str:
    temp = []
    for item in User.scan():
        temp.append(item.delete())
    return "%s items deleted." % len(temp)

def users_get() -> str:
    resultList = []
    for item in User.scan():
        resultList.append(item.attribute_values)
    return resultList

def users_post() -> str:
    newID = str(uuid.uuid4())
    newObj = User(id=newID)
    newObj.save()
    return newObj.attribute_values
