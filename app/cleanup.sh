#!/bin/bash

# Variables
APP_NAME="fastapi-app"
NAMESPACE="default"  # Change if you used a different namespace
PROM_RELEASE_NAME="monitoring"

echo "Starting cleanup..."

# Delete application resources
echo "Deleting FastAPI deployment and service..."
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml

# Uninstall Prometheus and Grafana
echo "Uninstalling Prometheus and Grafana..."
helm uninstall $PROM_RELEASE_NAME --namespace $NAMESPACE

# Kill any port-forwarding processes if running
echo "Killing port-forwarding processes..."

# Find processes running kubectl port-forward and kill them
PIDS=$(pgrep -f "kubectl port-forward")
if [ -n "$PIDS" ]; then
    kill $PIDS
    echo "Killed port-forward processes: $PIDS"
else
    echo "No port-forward processes found."
fi

# Stop Minikube (optional)
read -p "Do you want to stop Minikube? (y/n): " STOP_MINIKUBE
if [ "$STOP_MINIKUBE" = "y" ]; then
    echo "Stopping Minikube..."
    minikube stop
fi

echo "Cleanup complete!"
