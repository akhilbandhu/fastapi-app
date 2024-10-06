from fastapi import FastAPI, Request
from starlette_exporter import PrometheusMiddleware, handle_metrics
import time

app = FastAPI()

# Add middleware
app.add_middleware(
    PrometheusMiddleware,
    app_name="fastapi_app",
    group_paths=True
)
app.add_route("/metrics", handle_metrics)

@app.get("/")
def read_root():
    return {"message": "Hello, Kubernetes with Monitoring!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}"}
