# FastAPI Kubernetes Deployment

This project demonstrates how to deploy a FastAPI application using Kubernetes. It includes a simple FastAPI app, Dockerfile for containerization, and Kubernetes configuration files for deployment and service creation.

## Project Structure

- `app/`: Contains the FastAPI application
  - `main.py`: Main FastAPI application file
  - `requirements.txt`: Python dependencies
  - `Dockerfile`: Instructions for building the Docker image
- `deployment.yaml`: Kubernetes Deployment configuration
- `service.yaml`: Kubernetes Service configuration

## FastAPI Application

The FastAPI application is a simple API with two endpoints:

1. Root endpoint (`/`): Returns a greeting message
2. Items endpoint (`/items/{item_id}`): Returns item details

For more details, see:
python:app/main.py


## Docker Configuration

The application is containerized using Docker. The Dockerfile specifies:

- Python 3.12 slim image as the base
- Installation of dependencies from `requirements.txt`
- Copying of application files
- Command to run the FastAPI app using Uvicorn

For more details, see:
app/Dockerfile


## Kubernetes Deployment

The application is deployed on Kubernetes using the following configurations:

### Deployment

- Creates 2 replicas of the FastAPI application
- Uses the `fastapi-app:latest` image
- Sets the image pull policy to `Never` (assumes local image)

For more details, see:
deployment.yaml


### Service

- Exposes the application using a NodePort service
- Maps port 80 of the container to NodePort 30001

For more details, see:
service.yaml

## Getting Started

The following instructions are for local deployment on Minikube.
To get a quick start, run the following command:
```
./app/setup.sh
```
After the setup is complete, you can access the application via Minikube service or NodePort.
To access Grafana, navigate to http://localhost:3000 and log in with username 'admin' and the retrieved password.

To start the service, run the following command:
```
minikube service fastapi-service
```

To start locust, run the following command:
```
locust -f app/locustfile.py --host=<URL-FROM-MINIKUBE-COMMAND-ABOVE>
```

Add number of workers and per second spawn rate in the UI as you want. 
You can see the results in the locust UI and then also in Grafana under FastAPI monitoringdashboard.

If you want to do it manually, follow the steps below:

1. Build the Docker image:
   ```
   docker build -t fastapi-app:latest ./app
   ```

2. Apply the Kubernetes configurations:
   ```
   kubectl apply -f deployment.yaml
   kubectl apply -f service.yaml
   ```

3. Access the application:
   - If using Minikube, run `minikube service fastapi-service`
   - Otherwise, access the application at `http://<node-ip>:30001`

## Dependencies

- Python 3.12
- FastAPI
- Uvicorn

For a complete list of Python dependencies, see:
app/requirements.txt

## Integrating Prometheus and Grafana for Monitoring

This section guides you through integrating Prometheus and Grafana to monitor your FastAPI application running on Kubernetes.

### Overview

	•	Prometheus: Collects and stores metrics from your application and cluster.
	•	Grafana: Visualizes the metrics collected by Prometheus.

### Install Helm

Helm is a package manager for Kubernetes. It simplifies the deployment and management of applications on Kubernetes.

#### macOS

```
brew install helm
```

### Add Helm Repositories

```
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
```

### Install Prometheus

```
helm install monitoring prometheus-community/kube-prometheus-stack
```

### Expose Grafana Service

```
kubectl port-forward svc/monitoring-grafana 3000:80
```

### Access Grafana

Open your web browser and navigate to `http://localhost:3000`. Use the default username and password `admin` to log in.

### Retieve Grafana Password

```
kubectl get secret --namespace default monitoring-grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
```

Username: admin
Password: Use the output from the command above.

### Verify Prometheus Target

```
kubectl port-forward svc/monitoring-kube-prometheus-prometheus 9090:9090
```

Open your web browser and navigate to `http://localhost:9090`.


## Cleanup
# Delete application resources
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml

# Delete Prometheus and Grafana
helm uninstall monitoring

# If using Minikube, stop the cluster
minikube stop