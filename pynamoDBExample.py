from models import Sensor, Building


mySens = Sensor(sensorId = 'yet another id',
                sensorType='type',
                buildingId = 'theHASH',
                roomId = 'another hash',
                data=['data', 'moredata'])
mySens.save()


newBuilding = Building(id = 'one other id something',
                       buildingId = '1',
                       building='Franks shop',
                       rooms = ['a', 'b'],
                       owner = 1,
                       users = ['a', 'b'],
                       sensors = ['a', 'b'],
                       robots = ['a', 'b'])
newBuilding.save()
