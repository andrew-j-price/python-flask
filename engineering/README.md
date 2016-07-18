# Usage

### Basic
curl http://localhost
curl http://localhost/health | python -m json.tool
curl http://localhost/health | jq '.[] | select(.API == "Healthy")'
curl http://localhost/404


### API (minions)
curl -X GET http://localhost/minions
curl -X GET http://localhost/minions | python -m json.tool
curl -X GET http://localhost/minions | jq '.[] | select(.firstname == "Bob")'

curl -X POST http://localhost/minions -H "Content-Type: application/json" -d '{"firstname": "Norbert", "lastname":"BooYah"}'
curl -X DELETE http://localhost/minions/2


### API (users)
curl -X GET http://localhost/users
curl -X GET http://localhost/users | python -m json.tool
curl -X GET http://localhost/users | jq '.[] | select(.state == "NC")'

curl -X POST http://localhost/users -H "Content-Type: application/json" -d '{"name": "Christopher", "city":"Wilmington", "state":"NC", "country":"USA"}'
curl -X DELETE http://localhost/users/2


### SQL
mysql -h 127.0.0.1 -u root -pPassword123 api -e "select * from minions"
mysql -h 127.0.0.1 -u root -pPassword123 api -e "select * from users"
