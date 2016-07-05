# Usage

### Basic
curl http://localhost
curl http://localhost/health | python -m json.tool
curl http://localhost/404

### API (names)
curl -X GET http://localhost/names
curl -X GET http://localhost/names | python -m json.tool

curl -X POST http://localhost/names -H "Content-Type: application/json" -d '{"firstname": "John", "lastname":"Doe"}' 
curl -X DELETE http://localhost/names/2
curl -X GET http://localhost/names | python -m json.tool

### SQL
mysql -h 127.0.0.1 -u root -pPassword123 api -e "select * from names"
