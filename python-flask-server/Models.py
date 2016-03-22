# Take care of some imports
#from flywheel import Model, Field, Engine, set_
#from flywheel import STRING, STRING_SET, BINARY, NUMBER
# Set up our data model

from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, NumberAttribute, UnicodeSetAttribute, UTCDateTimeAttribute, NumberSetAttribute, BooleanAttribute, JSONAttribute, UnicodeSetAttribute, BinarySetAttribute
)


class Sensor(Model):
	class Meta:
        	table_name = 'Sensor'
	sensorId = UnicodeAttribute(hash_key=True)
	sensorType = UnicodeAttribute()
	buildingId = UnicodeAttribute()
	roomId = UnicodeAttribute()
	data = UnicodeSetAttribute()



class Building(Model):
	class Meta:
        	table_name = 'Building'
	id = UnicodeAttribute(hash_key=True)
	buildingId = NumberAttribute(range_key=True)
	building = UnicodeAttribute()
	rooms = UnicodeSetAttribute()
	owner = NumberAttribute() 
	users = UnicodeSetAttribute()
	sensors = UnicodeSetAttribute()
	robots = UnicodeSetAttribute()


'''
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




class Users(Model):
    userid = Field(hash_key=True)
    location = Field(range_key=True)
    ts = Field(data_type=datetime, index='ts-index')
    text = Field()





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
'''




