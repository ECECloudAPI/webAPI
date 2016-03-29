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
    buildingID = UnicodeAttribute(default='')
    floor = NumberAttribute(default=0)
    room = NumberAttribute(default=0)
    xpos = NumberAttribute(default=0)
    ypos = NumberAttribute(default=0)
    robot = UnicodeAttribute(default='')
    fromVal = UnicodeAttribute(default='')
    type = UnicodeAttribute(default='')


class Building(Model):
    class Meta:
        table_name = 'Building'
    id = UnicodeAttribute(hash_key=True)
    status = UnicodeAttribute(default='')


class Robot(Model):
    class Meta:
        table_name = 'Robot'
    id = UnicodeAttribute(hash_key=True)
    buildingID = UnicodeAttribute(default='')
    sensorID = UnicodeSetAttribute(default='')
    capabilities = UnicodeSetAttribute(default='')
    movement = UnicodeAttribute(default='')
    floor = NumberAttribute(default=0)
    room = NumberAttribute(default=0)
    xpos = NumberAttribute(default=0)
    ypos = NumberAttribute(default=0)
    fromVal = UnicodeAttribute(default='')


class User(Model):
    class Meta:
        table_name = 'User'
    id = UnicodeAttribute(hash_key=True)
    buildingID = UnicodeAttribute(default='')
    floor = NumberAttribute(default=0)
    room = NumberAttribute(default=0)
    xpos = NumberAttribute(default=0)
    ypos = NumberAttribute(default=0)
    message = UnicodeAttribute(default='')
    owner = BooleanAttribute(default=False)

#for item in Sensor.scan():
#    item.delete()