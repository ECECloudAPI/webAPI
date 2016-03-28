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
        table_name = 'Sensor'
    id = UnicodeAttribute(hash_key=True)
    buildingID = UnicodeAttribute(hash_key=True)
    floor = NumberAttribute()
    room = NumberAttribute()
    xpos = NumberAttribute()
    ypos = NumberAttribute()
    robot = UnicodeAttribute(hash_key=True)
    from = UnicodeAttribute()
    type = UnicodeAttribute()



class Building(Model):
    class Meta:
        table_name = 'Building'
    id = UnicodeAttribute(hash_key=True)
    status = UnicodeAttribute();


class Robot(Model):
	class Meta:
		table_name = 'Robot'
	id = UnicodeAttribute(hash_key=True)
	buildingID = UnicodeAttribute(hash_key=True)
	sensorID = UnicodeSetAttribute()
	capabilities = UnicodeSetAttribute()
	movement = UnicodeAttribute()
	floor = NumberAttribute()
	room = NumberAttribute()
	xpos = NumberAttribute()
	ypos = NumberAttribute()
	from = UnicodeAttribute()


class Users(Model):
	id = UnicodeAttribute(hash_key=True)
	buildingID = UnicodeAttribute(hash_key=True)
	movement = UnicodeAttribute()
	floor = NumberAttribute()
	room = NumberAttribute()
	xpos = NumberAttribute()
	ypos = NumberAttribute()
	message = UnicodeAttribute()
	owner = BooleanAttribute()









