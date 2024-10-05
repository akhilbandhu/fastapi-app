from multiprocessing import cpu_count

# Gunicorn config variables
workers = cpu_count() * 2 + 1
worker_class = "uvicorn.workers.UvicornWorker"
bind = "0.0.0.0:80"
