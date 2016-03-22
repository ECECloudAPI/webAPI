from models import  Sensor, Building, Robot, Room

Sensor.create_table(read_capacity_units=1, write_capacity_units=1)
Building.create_table(read_capacity_units=1, write_capacity_units=1)
Robot.create_table(read_capacity_units=1, write_capacity_units=1)
Room.create_table(read_capacity_units=1, write_capacity_units=1)
