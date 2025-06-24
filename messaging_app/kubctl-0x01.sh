#!/bin/bash

echo "Scaling deployment to 3 replicas..."
kubectl scale deployment django-messaging-deployment --replicas=3

echo " Verifying running pods..."
kubectl get pods -l app=django-messaging

echo "Waiting for all pods to become 'Running'..."
kubectl wait --for=condition=Ready pods -l app=django-messaging --timeout=60s


echo " Performing load test using wrk..."

SERVICE_IP=$(minikube service django-messaging-service --url)
wrk -t4 -c50 -d10s "$SERVICE_IP"

echo " Monitoring resource usage (CPU & Memory)..."
kubectl top pods

echo "Scaling and monitoring complete."

chmod +x kubctl-0x01.sh
