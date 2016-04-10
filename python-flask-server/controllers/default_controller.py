
import json
import uuid
from flask import request, jsonify
from storageModels import Building, Sensor, User, Robot

def buildings_building_id_robots_delete(buildingId):
    resultList = []
    for item in Robot.scan(buildingId__eq=buildingId):
        resultList.append(item.delete())
    return "%s items deleted." % len(resultList)

def buildings_building_id_robots_get(buildingId):
    resultList = []
    for item in Robot.scan(buildingId__eq=buildingId):
        resultList.append(item.attribute_values)
    return ( resultList )

def buildings_building_id_robots_post(buildingId):
    try:
        building = Building.get(buildingId)
    except Exception as e:
        print(e)
        return 'Building with id %s does not exist.' % (buildingId)
    newID = str(uuid.uuid4())
    newObj = Robot(id=newID, buildingId=buildingId)
    newObj.save()
    return newObj.attribute_values

def buildings_building_id_sensors_delete(buildingId):
    resultList = []
    for item in Sensor.scan(buildingId__eq=buildingId):
        resultList.append(item.delete())
    return "%s items deleted." % len(resultList)

def buildings_building_id_sensors_get(buildingId):
    resultList = []
    for item in Sensor.scan(buildingId__eq=buildingId):
        resultList.append(item.attribute_values)
    return ( resultList )

def buildings_building_id_sensors_post(buildingId):
    try:
        building = Building.get(buildingId)
    except Exception as e:
        print(e)
        return 'Building with id=%s does not exist.' % (buildingId)
    newID = str(uuid.uuid4())
    newObj = Sensor(id=newID, buildingId=buildingId)
    newObj.save()
    return newObj.attribute_values

def buildings_building_id_delete(buildingId):
    try:
        building = Building.get(buildingId)
        building.delete()
    except Exception as e:
        return 'Building with id=%s does not exist.' % (buildingId)
    return 'Successfully deleted buildingId=%s.' % (buildingId)

def buildings_building_id_get(buildingId):
    try:
        building = Building.get(buildingId)
    except Exception as e:
        print(e)
        return 'Building with id=%s does not exist.' % (buildingId)
    return building.attribute_values

def buildings_building_id_put(buildingId, newBuilding):
    try:
        building = Building.get(buildingId)
    except Exception as e:
        return 'Building with id=%s does not exist.' % (buildingId)
    attributes = building.attribute_values.keys()
    for key in newBuilding.keys():
        if key in attributes and key is not 'id':
            building.update_item(key, value=newBuilding[key], action='PUT')
    return 'Building with id=%s updated successfully.' % (buildingId)

def robots_robot_id_delete(robotId):
    try:
        robot = Robot.get(robotId)
        robot.delete()
    except Exception as e:      
        return 'Robot with id=%s does not exist.' % (robotId)
    return 'Successfully deleted robot with id=%s.' % (robotId)

def robots_robot_id_get(robotId):
    try:
        robot = Robot.get(robotId)
    except Exception as e:
        return 'Robot with id=%s does not exist.' % (robotId)
    return robot.attribute_values

def robots_robot_id_put(robotId, newRobot):
    try:
        robot = Robot.get(robotId)
    except Exception as e:
        return 'Robot with id=%s does not exist.' % (robotId)
    attributes = robot.attribute_values.keys()
    for key in newRobot.keys():
        if key in attributes and key is not 'id':
            robot.update_item(key, value=newRobot[key], action='PUT')
    return 'Robot with id=%s updated successfully.' % (robotId)

def sensors_sensor_id_delete(sensorId):
    try:
        sensor = Sensor.get(sensorId)
        sensor.delete()
    except Exception as e:
        return 'Sensor with id=%s does not exist.' % (sensorId)
    return 'Successfully deleted sensor with id=%s.' % (sensorId)

def sensors_sensor_id_get(sensorId):
    try:
        sensor = Sensor.get(sensorId)
    except Exception as e:
        return 'Sensor with id=%s does not exist.' % (sensorId)
    return sensor.attribute_values

def sensors_sensor_id_put(sensorId, newSensor):
    try:
        sensor = Sensor.get(sensorId)
    except Exception as e:
        return 'Sensor with id=%s does not exist.' % (sensorId)
    attributes = sensor.attribute_values.keys()
    for key in newSensor.keys():
        if key in attributes and key is not 'id':
            sensor.update_item(key, value=newSensor[key], action='PUT')
    return 'Sensor with id=%s updated successfully.' % (sensorId)

def users_user_id_delete(userId):
    try:
        user = User.get(userId)
        user.delete()
    except Exception as e:      
        return 'User with id=%s does not exist.' % (userId)
    return 'Successfully deleted user with id=%s.' % (userId)

def users_user_id_get(userId):
    try:
        user = User.get(userId)
    except Exception as e:
        return 'User with id=%s does not exist.' % (userId)
    return user.attribute_values

def users_user_id_put(userId, newUser):
    try:
        user = User.get(userId)
    except Exception as e:
        return 'User with id=%s does not exist.' % (userId)
    attributes = user.attribute_values.keys()
    for key in newUser.keys():
        if key in attributes and key is not 'id':
            user.update_item(key, value=newUser[key], action='PUT')
    return 'User with id=%s updated successfully.' % (userId)

def buildings_delete():
    temp = []
    for item in Building.scan():
        temp.append(item.delete())
    return "%s items deleted." % len(temp)

def buildings_get():
    resultList = []
    for item in Building.scan():
        resultList.append(item.attribute_values)
    return resultList

def buildings_post():
    newID = str(uuid.uuid4())
    newObj = Building(id=newID)
    newObj.save()
    return newObj.attribute_values

def robots_delete():
    temp = []
    for item in Robot.scan():
        temp.append(item.delete())
    return "%s items deleted." % len(temp)

def robots_get():
    resultList = []
    for item in Robot.scan():
        resultList.append(item.attribute_values)
    return resultList

def sensors_delete():
    temp = []
    for item in Sensor.scan():
        temp.append(item.delete())
    return "%s items deleted." % len(temp)

def sensors_get():
    resultList = []
    for item in Sensor.scan():
        resultList.append(item.attribute_values)
    return resultList

def sensors_post():
    newID = str(uuid.uuid4())
    sensorObj = Sensor(id=newID)
    sensorObj.save()
    return sensorObj.attribute_values

def users_delete():
    temp = []
    for item in User.scan():
        temp.append(item.delete())
    return "%s items deleted." % len(temp)

def users_get():
    resultList = []
    for item in User.scan():
        resultList.append(item.attribute_values)
    return resultList

def users_post():
    newID = str(uuid.uuid4())
    newObj = User(id=newID)
    newObj.save()
    return newObj.attribute_values
