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