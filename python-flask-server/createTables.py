
from Models import  Sensor, Building

Sensor.create_table(read_capacity_units=1, write_capacity_units=1)
Building.create_table(read_capacity_units=1, write_capacity_units=1)
