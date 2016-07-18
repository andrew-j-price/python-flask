# Usage

curl 127.0.0.1

curl 127.0.0.1/health
curl 127.0.0.1/health | python -m json.tool
curl 127.0.0.1/health | jq '.[] | select(.API == "Healthy")'

curl 127.0.0.1/404
