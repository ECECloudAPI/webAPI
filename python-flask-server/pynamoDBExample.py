from Models import Sensor, Building


mySens = Sensor(sensorId = 'an id', sensorType='type', buildingId = 'theidHASH', roomId = 'another hash', data=['data', 'moredata'])
mySens.save()


newBuilding = Building(id = 'another id something', buildingId = 1, building='Franks shop', rooms = ['a', 'b'], owner = 1, users = ['a', 'b'],
sensors = ['a', 'b'], robots = ['a', 'b'])

newBuilding.save()
