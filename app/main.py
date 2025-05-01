"""Módulo principal da API FastAPI para demonstração de CI/CD."""

import asyncio # Standard library imports first
import time
import os

from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse, FileResponse
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from pydantic import BaseModel, EmailStr

app = FastAPI(title="DevOps CI/CD Demo API", version="0.1.0")

REQUEST_COUNT = Counter("api_requests_total", "Total de requisições")
REQUEST_LATENCY = Histogram("api_request_latency_seconds", "Latência das requisições")


# --- Modelos Pydantic ---
class UserCreate(BaseModel):
    """Modelo Pydantic para criação de usuário."""
    nome: str
    email: EmailStr


# --- Endpoints Existentes ---
@app.get("/")
def root():
    """Endpoint raiz que retorna um status 'ok'."""
    return {"status": "ok"}


@app.get("/api/v1/event")
def event():
    """Endpoint que simula a geração de um evento e registra métricas."""
    start = time.time()
    REQUEST_COUNT.inc()
    # Simular algum trabalho antes de observar a latência
    time.sleep(0.01)
    REQUEST_LATENCY.observe(time.time() - start)
    return {"message": "evento gerado"}


@app.get("/metrics")
def metrics():
    """Endpoint que expõe as métricas do Prometheus."""
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


# --- Novos Endpoints ---

@app.get("/api/v1/users")
def get_users():
    """Retorna uma lista simulada de usuários."""
    start = time.time()
    REQUEST_COUNT.inc()
    # Simular busca em banco de dados
    time.sleep(0.05)
    users_db = [
        {"id": 1, "nome": "Alice"},
        {"id": 2, "nome": "Bob"},
        {"id": 3, "nome": "Charlie"},
    ]
    REQUEST_LATENCY.observe(time.time() - start)
    return users_db


@app.post("/api/v1/users")
def create_user(user: UserCreate):
    """Recebe dados de um novo usuário e confirma o cadastro."""
    start = time.time()
    REQUEST_COUNT.inc()
    # Simular inserção em banco de dados
    time.sleep(0.1)
    REQUEST_LATENCY.observe(time.time() - start)
    return {
        "message": f"Usuário '{user.nome}' com email '{user.email}' cadastrado com sucesso!"
    }


@app.get("/api/v1/status/{codigo}")
def get_status(codigo: int):
    """Retorna o código de status fornecido."""
    start = time.time()
    REQUEST_COUNT.inc()
    # Simular verificação de status
    time.sleep(0.02)
    REQUEST_LATENCY.observe(time.time() - start)
    return JSONResponse(content={"status_code_recebido": codigo}, status_code=200)


@app.get("/api/v1/delay/{segundos}")
async def introduce_delay(segundos: int):
    """Aguarda um número específico de segundos."""
    start = time.time()
    REQUEST_COUNT.inc()
    await asyncio.sleep(segundos)  # Usar asyncio.sleep para não bloquear o event loop
    REQUEST_LATENCY.observe(time.time() - start)
    return {"message": f"Aguardei por {segundos} segundos."}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.get("/robots.txt")
def robots_txt():
    """Retorna o arquivo robots.txt."""
    return FileResponse(os.path.join(BASE_DIR, "static", "robots.txt"), media_type="text/plain")

@app.get("/sitemap.xml")
def sitemap_xml():
    """Retorna o arquivo sitemap.xml."""
    return FileResponse(os.path.join(BASE_DIR, "static", "sitemap.xml"), media_type="application/xml")
