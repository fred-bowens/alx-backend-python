#!/bin/bash


echo " Deploying blue version..."
kubectl apply -f blue_deployment.yaml

echo " Routing service to blue deployment..."
kubectl apply -f kubeservice.yaml

echo " Deploying green version..."
kubectl apply -f green_deployment.yaml

echo " Waiting for green pods to be ready..."
kubectl wait --for=condition=Ready pods -l version=green --timeout=60s

echo " Checking logs for green deployment pods..."
GREEN_PODS=$(kubectl get pods -l version=green -o name)
for pod in $GREEN_PODS; do
    echo " Logs for $pod:"
    kubectl logs "$pod"
done

echo "Blue-Green deployments active. Update the service selector to switch traffic when ready."
