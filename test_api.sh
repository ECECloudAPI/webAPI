
# POST sensors/
curl -X POST -H "Cache-Control: no-cache" -H "Postman-Token: 02bd02a2-6e5d-daaf-ef8e-ff2d353dd46a" -d '' "http://0.0.0.0:8080/api/sensors/"

# GET sensors/{sensorID}
curl -X GET -H "Cache-Control: no-cache" -H "Postman-Token: c61f9cdc-c509-4b05-d05b-7dbdee88d107" "http://0.0.0.0:8080/api/sensors/ca519d63-e81a-4df1-bdb1-ffe85df435ce"
