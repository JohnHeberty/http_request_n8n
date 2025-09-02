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

    # Prepara o body para a requisição
    request_data = None
    request_json = None
    
    if body is not None:
        if isinstance(body, (dict, list)):
            # Se é um objeto/lista, envia como JSON
            request_json = body
            # Garante que o Content-Type está correto
            if "Content-Type" not in headers:
                headers["Content-Type"] = "application/json"
        else:
            # Se é string ou outros tipos, envia como data
            request_data = body

    # Usa requests para fazer a requisição
    resp = requests.request(
        method,
        url,
        headers=headers,
        data=request_data,
        json=request_json,
        verify=False
    )

    return Response(content=resp.content, status_code=resp.status_code, headers=dict(resp.headers))

# Para rodar:
# uvicorn main:app --reload
