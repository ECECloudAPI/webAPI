#!/usr/bin/env python3
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
        table_name = 'Sensors'
    id = UnicodeAttribute(hash_key=True)
    buildingId = UnicodeAttribute(default='')
    floor = NumberAttribute(default=0)
    room = NumberAttribute(default=0)
    xpos = NumberAttribute(default=0)
    ypos = NumberAttribute(default=0)
    type = UnicodeAttribute(default='')
    model = UnicodeAttribute(default='')
    data = UnicodeAttribute(default='')


class Building(Model):
    class Meta:
        table_name = 'Buildings'
    id = UnicodeAttribute(hash_key=True)
    ownerId = UnicodeAttribute(default='') 
    status = UnicodeAttribute(default='')


class Robot(Model):
    class Meta:
        table_name = 'Robots'
    id = UnicodeAttribute(hash_key=True)
    buildingId = UnicodeAttribute(default='')
    sensorId = JSONAttribute(default='[]')
    capabilities = JSONAttribute(default='[]')
    movement = UnicodeAttribute(default='')
    floor = NumberAttribute(default=0)
    room = NumberAttribute(default=0)
    xpos = NumberAttribute(default=0)
    ypos = NumberAttribute(default=0)

class User(Model):
    class Meta:
        table_name = 'Users'
    id = UnicodeAttribute(hash_key=True)
    buildingId = UnicodeAttribute(default='')
    floor = NumberAttribute(default=0)
    room = NumberAttribute(default=0)
    xpos = NumberAttribute(default=0)
    ypos = NumberAttribute(default=0)
    message = UnicodeAttribute(default='')
    owner = BooleanAttribute(default=False)
class Login(Model):
	class Meta:
		table_name = 'Login'
	email = UnicodeAttribute(hash_key=True)
	password = UnicodeAttribute(default='')
	userid = UnicodeAttribute(default='')

#for item in Sensor.scan():
#    item.delete()
