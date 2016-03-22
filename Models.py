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
    buildingId = UnicodeAttribute(range_key=True)
    building = UnicodeAttribute()
    rooms = UnicodeSetAttribute()
    owner = NumberAttribute()
    users = UnicodeSetAttribute()
    sensors = UnicodeSetAttribute()
    robots = UnicodeSetAttribute()



class Room(Model):
    class Meta:
        table_name = 'Room'
    roomId = UnicodeAttribute(hash_key=True)
    roomName = UnicodeAttribute()
    statuses = UnicodeSetAttribute()
    width = NumberAttribute()
    height = NumberAttribute()
    length = NumberAttribute()
    sensors = UnicodeSetAttribute()
    robots = UnicodeSetAttribute()



class Robot(Model):
    class Meta:
       	table_name = 'Robot'
    robotId = UnicodeAttribute(hash_key=True)
    emergency = BooleanAttribute()
    offensive = BooleanAttribute()
    sensors = UnicodeSetAttribute()
    buildingId = NumberAttribute()
    name = UnicodeAttribute()
    movement = UnicodeAttribute()
    updated = UTCDateTimeAttribute()
    floor = NumberAttribute()
    roomId = NumberAttribute()

'''
class Users(Model):
    userid = Field(hash_key=True)
    location = Field(range_key=True)
    ts = Field(data_type=datetime, index='ts-index')
    text = Field()


'''
