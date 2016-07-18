# Usage

curl 127.0.0.1

curl 127.0.0.1/articles
curl 127.0.0.1/articles/123

curl 127.0.0.1/hello
curl 127.0.0.1/hello?name=Lucas

curl -X GET http://127.0.0.1/echo
curl -X POST http://127.0.0.1/echo
curl -X PATCH http://127.0.0.1/echo
curl -X PUT http://127.0.0.1/echo
curl -X DELETE http://127.0.0.1/echo

curl -v -H "Content-type: text/plain" \
-X POST 127.0.0.1/messages -d '"Hello Data"'

curl -v -H "Content-type: application/json" \
-X POST 127.0.0.1/messages -d '{"message":"Hello Data"}'

curl 127.0.0.1/health
curl 127.0.0.1/health | python -m json.tool

curl 127.0.0.1/users/2
curl 127.0.0.1/users/4
