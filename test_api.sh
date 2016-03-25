
# POST buildings/
curl -X POST -H "Content-Type: application/json" -H "Cache-Control: no-cache" -H "Postman-Token: 50b14706-3ec7-770c-806d-1d96ddc94a81" -d '{
    "id" : "topSecret",
    "buildingId" : "6",
    "building" : "LaveryHall",
    "rooms" : ["a", "b"],
    "owner" : 2,
    "users" : ["Chang", "Apple"],
    "sensors" : ["m", "n"],
    "robots" : ["R2"]
}' "http://0.0.0.0:8080/api/buildings/"

# POST sensors/
curl -X POST -H "Content-Type: application/json" -H "Cache-Control: no-cache" -H "Postman-Token: a74e3fc2-9f63-a014-6c71-aa98fb2536d4" -d '{
    "sensorId" : "3",
    "sensorType" : "Top Secret",
    "buildingId" : "6",
    "roomId" : "404",
    "data" : ["foo", "bar"]
}' "http://0.0.0.0:8080/api/sensors/"
