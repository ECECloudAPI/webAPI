# Take care of some imports
from flywheel import Model, Field, Engine, set_

# Set up our data model
class Building(Model):
	__metadata__ = {
		'throughput': {
			'read': 1,
			'write': 1,
		}
	}
	id = Field(hash_key=True)
	buildingId = Field(data_type=int, range_key=True)
	building = Field(data_type=str)
	rooms = Field(data_type=list)
	owner = Field(data_type=int)
	users = Field(data_type=list)
	sensors = Field(data_type=list)
	robots = Field(data_type=list)

def __init__(self, buildingid, building, rooms, owner, users, sensors, robots):
	self.buildingId = buildingid
	self.building = building
	self.rooms = rooms
	self.owner = owner
	self.users = users
	self.sensors = sensors
	self.robots = robots


class Room(Model):
	__metadata__ = {
		'throughput': {
			'read': 1,
			'write': 1,
		}
	}
	roomId = Field(hash_key=True)
	roomName = Field(data_type=str)
	statuses = Field(data_type=list)
	width = Field(data_type=int)
	height = Field(data_type=int)
	length = Field(data_type=int)
	sensors = Field(data_type=list)
	robots = Field(data_type=list)

def __init__(self,roomName, statuses, width, height, length, sensors, robots):
	self.roomName = roomName
	self.statuses  = statuses
	self.width = width
	self.height = height
	self.length  = length
	self.sensors = sensors
	self.robots = robots

'''
class Users(Model):
    userid = Field(hash_key=True)
    location = Field(range_key=True)
    ts = Field(data_type=datetime, index='ts-index')
    text = Field()

    def __init__(self, userid, id, ts, text):
        self.userid = userid
        self.id = id
        self.ts = ts
        self.text = text
'''

class Sensor(Model):
	__metadata__ = {
		'throughput': {
			'read': 1,
			'write': 1,
		}
	}
	sensorId = Field(hash_key=True)
	sensorType = Field(data_type=str)
	buildingId = Field(data_type=str)
	roomId = Field(data_type=str)
	data = Field(data_type=list)
 
def __init__(self, sensorType, buildingId, roomId, data):
	self.sensorType = sensorType
	self.buildingId = buildingId
	self.roomId = roomId
	self.data = data


class Robot(Model):
	robotId = Field(hash_key=True)
	emergency = Field(data_type=bool)
	offensive = Field(data_type=bool)
	sensors = Field(data_type=list)
	buildingId = Field(data_type=int)
	name = Field(data_type = str)
	movement = Field(data_type = str)
	updated = Field()
	floor = Field(data_type = int)
	roomId = Field(data_type = int)


def __init__(self, emergency, offensive, sensors, buildingId, name, movement, updated, floor, roomId):
	self.emergency = emergency
	self.offensive = offensive
	self.sensors = sensors
	self.buildingId = buildingId
	self.name = name
	self.movement = movement
	self.updated = updated
	self.floor = floor
	self.roomId = roomId

# Create an engine and connect to an AWS region
engine = Engine()
engine.connect_to_region('us-east-1')

# Register our model with the engine so it can create the Dynamo table
engine.register(Building, Room, Sensor, Robot)

# Create the dynamo table for our registered model
engine.create_schema()


