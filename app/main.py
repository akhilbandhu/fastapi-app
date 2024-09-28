from fastapi import FastAPI
from prometheus_client import Counter
from starlette_exporter import PrometheusMiddleware, handle_metrics

app = FastAPI()

# Add middleware
app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)

# Define custom metrics
REQUEST_COUNT = Counter("request_count", "Total number of requests")

@app.get("/")
def read_root():
    REQUEST_COUNT.inc()
    return {"message": "Hello, Kubernetes with Monitoring!"}