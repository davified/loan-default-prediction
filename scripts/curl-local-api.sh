curl -X POST http://localhost:80/predict/ \
  -H "Content-Type: application/json" \
  --data-binary "@scripts/curl-local-api-request.json"