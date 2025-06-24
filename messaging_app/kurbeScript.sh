#!/bin/bash


if ! command -v minikube &> /dev/null
then
    echo "❌ Minikube is not installed. Please install it from https://minikube.sigs.k8s.io/docs/start/"
    exit 1
fi

if ! command -v kubectl &> /dev/null
then
    echo "❌ kubectl is not installed. Please install it from https://kubernetes.io/docs/tasks/tools/"
    exit 1
fi

echo "🚀 Starting Minikube cluster..."
minikube start

echo "🔍 Verifying Kubernetes cluster status..."
kubectl cluster-info
echo "📦 Listing all pods in all namespaces..."
kubectl get pods --all-namespaces

echo "✅ Kubernetes cluster is up and running locally!"  
chmod +x kurbeScript.sh
