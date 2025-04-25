# app/main.py
from fastapi import FastAPI, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time

app = FastAPI(title="DevOps CI/CD Demo API", version="0.1.0")

REQUEST_COUNT = Counter("api_requests_total", "Total de requisições")
REQUEST_LATENCY = Histogram("api_request_latency_seconds", "Latência das requisições")
POST_COUNT = Counter("api_post_total", "Total de POSTs recebidos")

class Payload(BaseModel):
    nome: str

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/api/v1/event")
def event():
    start = time.time()
    REQUEST_COUNT.inc()
    REQUEST_LATENCY.observe(time.time() - start)
    return {"message": "evento gerado"}

@app.post("/api/v1/send")
def receive_event(payload: Payload):
    POST_COUNT.inc()
    return {"received": payload.nome}


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

