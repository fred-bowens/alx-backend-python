#!/bin/bash

echo "Applying updated blue deployment with image version 2.0..."
kubectl apply -f blue_deployment.yaml

echo " Monitoring rollout status of blue deployment..."
kubectl rollout status deployment/django-blue

echo "Testing live traffic with curl during rollout..."
for i in {1..20}; do
  curl -s http://$(minikube ip)/api/ >> curl-log.txt
  echo "Request $i complete"
  sleep 1
done &
CURL_PID=$!

wait $CURL_PID
echo " Curl test completed. Check curl-log.txt for response continuity."

echo " Verifying running pods after rollout:"
kubectl get pods -l version=blue -o wide

echo "Rolling update complete with zero downtime (if all responses were received)."
