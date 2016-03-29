from storageModels import Sensor, Building, Robot, User

Sensor.create_table(read_capacity_units=1, write_capacity_units=1)
Building.create_table(read_capacity_units=1, write_capacity_units=1)
Robot.create_table(read_capacity_units=1, write_capacity_units=1)
User.create_table(read_capacity_units=1, write_capacity_units=1)
