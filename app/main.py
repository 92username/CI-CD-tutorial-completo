from fastapi import FastAPI, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time

app = FastAPI(title="DevOps CI/CD Demo API", version="0.1.0")

REQUEST_COUNT = Counter("api_requests_total", "Total de requisições")
REQUEST_LATENCY = Histogram("api_request_latency_seconds", "Latência das requisições")

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/api/v1/event")
def event():
    start = time.time()
    REQUEST_COUNT.inc()
    REQUEST_LATENCY.observe(time.time() - start)
    return {"message": "evento gerado"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)