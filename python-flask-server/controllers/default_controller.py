
import json
import uuid
from flask import request, jsonify
from storageModels import Building, Sensor, User, Robot

def buildings_building_id_robots_delete(buildingId):
    """ method to delete all robots inside a building """
    resultlist = []
    for item in Robot.scan(buildingId__eq=buildingId):
        resultlist.append(item.delete())
    return "%s items deleted." % len(resultlist)

def buildings_building_id_robots_get(buildingId):
    """ method to get all robots inside a building """
    resultlist = []
    for item in Robot.scan(buildingId__eq=buildingId):
        resultlist.append(item.attribute_values)
    return resultlist

def buildings_building_id_robots_post(buildingId):
    """ method to post robot under a  building """
    try:
        building = Building.get(buildingId)
    except Exception:
        return 'Building with id %s does not exist.' % (buildingId)
    newid = str(uuid.uuid4())
    newobj = Robot(id=newid, buildingId=buildingId)
    newobj.save()
    return newobj.attribute_values

def buildings_building_id_sensors_delete(buildingId):
    """ method to delete sensor using building id """
    resultlist = []
    for item in Sensor.scan(buildingId__eq=buildingId):
        resultlist.append(item.delete())
    return "%s items deleted." % len(resultlist)

def buildings_building_id_sensors_get(buildingId, room=[], type=[]):
    """ method to get sensors using building id """
    resultlist = []
    items = []
    if room and type:
       items = Sensor.scan(buildingId__eq=buildingId,room__eq=room,type__eq=type)
    elif room:
       items = Sensor.scan(buildingId__eq=buildingId,room__eq=room)
    elif type:
       items = Sensor.scan(buildingId__eq=buildingId,type__eq=type)
    else:
       items = Sensor.scan(buildingId__eq=buildingId)
    for item in items:
        resultlist.append(item.attribute_values)
    return resultlist

def buildings_building_id_sensors_post(buildingId):
    """ method to post a sensor using sensor id """
    try:
        building = Building.get(buildingId)
    except Exception:
        return 'Building with id=%s does not exist.' % (buildingId)
    newid = str(uuid.uuid4())
    newobj = Sensor(id=newid, buildingId=buildingId)
    newobj.save()
    return newobj.attribute_values

def buildings_building_id_delete(buildingId):
    """ method to delete building using building id """
    try:
        building = Building.get(buildingId)
        building.delete()
    except Exception:
        return 'Building with id=%s does not exist.' % (buildingId)
    return 'Successfully deleted buildingId=%s.' % (buildingId)

def buildings_building_id_get(buildingId):
    """ method to get building using building id """
    try:
        building = Building.get(buildingId)
    except Exception:
        return 'Building with id=%s does not exist.' % (buildingId)
    return building.attribute_values

def buildings_building_id_put(buildingId, newBuilding):
    """ method to update building using building id """
    try:
        building = Building.get(buildingId)
    except Exception:
        return 'Building with id=%s does not exist.' % (buildingId)
    attributes = building.attribute_values.keys()
    for key in newBuilding.keys():
        if key in attributes and key is not 'id':
            building.update_item(key, value=newBuilding[key], action='PUT')
    return 'Building with id=%s updated successfully.' % (buildingId)

def robots_robot_id_delete(robotId):
    """ method to delete a robot using robot id """
    try:
        robot = Robot.get(robotId)
        robot.delete()
    except Exception:      
        return 'Robot with id=%s does not exist.' % (robotId)
    return 'Successfully deleted robot with id=%s.' % (robotId)

def robots_robot_id_get(robotId):
    """ method to get a robot using robot id """
    try:
        robot = Robot.get(robotId)
    except Exception:
        return 'Robot with id=%s does not exist.' % (robotId)
    return robot.attribute_values

def robots_robot_id_put(robotId, newRobot):
    """ method to update a robot using robot id """
    try:
        robot = Robot.get(robotId)
    except Exception:
        return 'Robot with id=%s does not exist.' % (robotId)
    attributes = robot.attribute_values.keys()
    for key in newRobot.keys():
        if key in attributes and key is not 'id':
            robot.update_item(key, value=newRobot[key], action='PUT')
    return 'Robot with id=%s updated successfully.' % (robotId)

def sensors_sensor_id_delete(sensorId):
    """ method to delete a sensor using sensor id """
    try:
        sensor = Sensor.get(sensorId)
        sensor.delete()
    except Exception:
        return 'Sensor with id=%s does not exist.' % (sensorId)
    return 'Successfully deleted sensor with id=%s.' % (sensorId)

def sensors_sensor_id_get(sensorId):
    """ method to get a sensor using sensor id """
    try:
        sensor = Sensor.get(sensorId)
    except Exception:
        return 'Sensor with id=%s does not exist.' % (sensorId)
    return sensor.attribute_values

def sensors_sensor_id_put(sensorId, newSensor):
    """ method to update sensor using sensor id """
    try:
        sensor = Sensor.get(sensorId)
    except Exception:
        return 'Sensor with id=%s does not exist.' % (sensorId)
    attributes = sensor.attribute_values.keys()
    for key in newSensor.keys():
        if key in attributes and key is not 'id':
            sensor.update_item(key, value=newSensor[key], action='PUT')
    return 'Sensor with id=%s updated successfully.' % (sensorId)

def users_user_id_delete(userId):
    """ method to delete user using user id """
    try:
        user = User.get(userId)
        user.delete()
    except Exception:      
        return 'User with id=%s does not exist.' % (userId)
    return 'Successfully deleted user with id=%s.' % (userId)

def users_user_id_get(userId):
    """ method to retrieve user using user id """
    try:
        user = User.get(userId)
    except Exception:
        return 'User with id=%s does not exist.' % (userId)
    return user.attribute_values

def users_user_id_put(userId, newUser):
    """ method to update a user using user id """
    try:
        user = User.get(userId)
    except Exception:
        return 'User with id=%s does not exist.' % (userId)
    attributes = user.attribute_values.keys()
    for key in newUser.keys():
        if key in attributes and key is not 'id':
            user.update_item(key, value=newUser[key], action='PUT')
    return 'User with id=%s updated successfully.' % (userId)

def buildings_delete():
    """ method to delete all buildings """
    temp = []
    for item in Building.scan():
        temp.append(item.delete())
    return "%s items deleted." % len(temp)

def buildings_get():
    """ method to get all buildings """
    resultlist = []
    for item in Building.scan():
        resultlist.append(item.attribute_values)
    return resultlist

def buildings_post():
    """ method to post a new building """
    newid = str(uuid.uuid4())
    newobj = Building(id=newid)
    newobj.save()
    return newobj.attribute_values

def robots_delete():
    """ method to delete all robots """
    temp = []
    for item in Robot.scan():
        temp.append(item.delete())
    return "%s items deleted." % len(temp)

def robots_get():
    """ method to get all robots """
    resultlist = []
    for item in Robot.scan():
        resultlist.append(item.attribute_values)
    return resultlist

def sensors_delete():
    """ method to delete sensor """
    temp = []
    for item in Sensor.scan():
        temp.append(item.delete())
    return "%s items deleted." % len(temp)

def sensors_get():
    """ method to get all sensors """
    resultlist = []
    for item in Sensor.scan():
        resultlist.append(item.attribute_values)
    return resultlist

def sensors_post():
    """ method to post a new sensor """
    newid = str(uuid.uuid4())
    sensorobj = Sensor(id=newid)
    sensorobj.save()
    return sensorobj.attribute_values

def users_delete():
    """ method to delete all users """
    temp = []
    for item in User.scan():
        temp.append(item.delete())
    return "%s items deleted." % len(temp)

def users_get(owner=[], buildingId=[], room=[]):
    """ method to get all users """
    resultlist = []
    items = []
    if (owner != [] and buildingId != [] and room != []):
       items = User.scan(owner__eq=owner, buildingId__eq=buildingId, room__eq=room);
    elif (buildingId != [] and room != []):
       items = User.scan(buildingId__eq=buildingId, room__eq=room);
    elif (owner != [] and buildingId != []):
       items = User.scan(owner__eq=owner, buildingId__eq=buildingId);
    elif (owner != [] and room != []):
       items = User.scan(owner__eq=owner, room__eq=room);
    elif (owner != []):
       items = User.scan(owner__eq=owner);
    elif (buildingId != []):
       items = User.scan(buildingId__eq=buildingId);
    elif (room != []):
       items = User.scan(room__eq=room);
    else:
       items = User.scan();
    for item in items:
        resultlist.append(item.attribute_values)
    return resultlist;

    #resultlist = []
    #for item in User.scan():
    #    resultlist.append(item.attribute_values)
    #return resultlist

def users_post():
    """ method to post a new user """
    newid = str(uuid.uuid4())
    newobj = User(id=newid)
    newobj.save()
    return newobj.attribute_values
