# Proxy Redirect API
# Instale as dependências com:
# pip install fastapi uvicorn requests

from fastapi import FastAPI, Request
from fastapi.responses import Response, JSONResponse
from fastapi import Body
import requests

app = FastAPI()

@app.post("/proxy")
def proxy(
    payload: dict = Body(...)
):
    # Espera um JSON com: url, method, headers, body
    url = payload.get("url")
    method = payload.get("method", "GET").upper()
    headers = payload.get("headers", {})
    body = payload.get("body", None)
    
    if not url:
        return JSONResponse({"error": "url é obrigatório"}, status_code=400)

    # Usa requests para fazer a requisição
    resp = requests.request(
        method,
        url,
        headers=headers,
        data=body,
        verify=False
    )

    return Response(content=resp.content, status_code=resp.status_code, headers=dict(resp.headers))

# Para rodar:
# uvicorn main:app --reload
