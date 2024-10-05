from fastapi import FastAPI, Request
from prometheus_client import Counter, Histogram, Gauge
from starlette_exporter import PrometheusMiddleware, handle_metrics
import time

app = FastAPI()

# Add middleware
app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)

# Define custom metrics
REQUEST_COUNT = Counter("request_count", "Total number of requests")
REQUEST_DURATION = Histogram("request_duration_seconds", "Request duration in seconds")
ACTIVE_REQUESTS = Gauge("active_requests", "Number of active requests")

@app.middleware("http")
async def track_requests(request: Request, call_next):
    ACTIVE_REQUESTS.inc()
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    REQUEST_DURATION.observe(duration)
    ACTIVE_REQUESTS.dec()
    return response

@app.get("/")
def read_root():
    REQUEST_COUNT.inc()
    return {"message": "Hello, Kubernetes with Monitoring!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    REQUEST_COUNT.inc()
    return {"item_id": item_id, "name": f"Item {item_id}"}