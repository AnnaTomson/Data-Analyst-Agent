import multiprocessing

# Server socket
bind = "0.0.0.0:8000"

# Worker processes
workers = multiprocessing.cpu_workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "uvicorn.workers.UvicornWorker"

# Logging
loglevel = "info"
accesslog = "-"  # Log to stdout
errorlog = "-"   # Log to stderr

# Timeout
keepalive = 5
timeout = 120
