#!/bin/bash

API_URL="http://localhost:8000/query"

QUERIES=(
  "List all customers"
  "Top 3 products by sales"
  "Show all orders from January 2024"
  "List customers from New York"
  "Total sales amount per product"
)

echo "🚀 Evaluator script running against $API_URL"
echo "--------------------------------------------"

for q in "${QUERIES[@]}"; do
  echo "🔎 Query: $q"
  curl -s -X POST "$API_URL" \
    -H "Content-Type: application/json" \
    -d "{\"query\":\"$q\"}"
  echo
  echo "--------------------------------------------"
done
