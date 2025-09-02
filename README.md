# Proxy Redirect API para N8N

Uma API FastAPI que funciona como proxy HTTP para redirecionar requisições, especialmente útil para contornar limitações de CORS e SSL em workflows do N8N.

## 🚀 Como usar

### Instalação com Docker

1. Clone o repositório
2. Entre na pasta do projeto:
```bash
cd http_request_n8n
```

3. Suba o container:
```bash
docker-compose up --build
```

A API estará disponível em `http://localhost/proxy`

### 📡 Endpoint

**POST** `/proxy`

#### Parâmetros do JSON:

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `url` | string | ✅ | URL de destino da requisição |
| `method` | string | ❌ | Método HTTP (GET, POST, PUT, DELETE, etc). Padrão: GET |
| `headers` | object | ❌ | Headers da requisição |
| `body` | string | ❌ | Corpo da requisição (para POST, PUT, etc) |

#### Exemplo de requisição:

```json
{
  "url": "https://api.exemplo.com/dados",
  "method": "POST",
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer seu-token"
  },
  "body": "{\"parametro\": \"valor\"}"
}
```

## 🔧 Configuração no N8N

### 1. Adicione um nó HTTP Request

### 2. Configure o nó:
- **Method**: POST
- **URL**: `http://seu-servidor/proxy`
- **Headers**:
  ```
  Content-Type: application/json
  ```

### 3. No corpo da requisição (Body):
```json
{
  "url": "{{ $json.url_destino }}",
  "method": "POST",
  "headers": {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
  },
  "body": "{{ $json.dados | toJsonString }}"
}
```

### 4. Exemplo prático - Consulta de CEP:
```json
{
  "url": "https://viacep.com.br/ws/01310-100/json/",
  "method": "GET",
  "headers": {
    "Accept": "application/json"
  }
}
```

## 🔧 Vantagens

✅ **Contorna CORS**: Remove limitações de origem cruzada  
✅ **SSL/TLS**: Ignora problemas de certificado  
✅ **Headers customizados**: Adicione qualquer header necessário  
✅ **Todos os métodos HTTP**: GET, POST, PUT, DELETE, PATCH  
✅ **Simples**: Interface JSON fácil de usar  

## 🐳 Estrutura Docker

- **FastAPI**: API principal na porta 8000
- **Nginx**: Proxy reverso na porta 80
- **Volume**: Configuração nginx.conf

## 📝 Logs

Para ver os logs:
```bash
docker-compose logs -f
```

## ⚠️ Notas importantes

- Esta API ignora verificação SSL (`verify=False`) para contornar problemas de certificado
- Recomendado apenas para ambientes de desenvolvimento/teste
- Para produção, configure certificados SSL adequados

## 🛠️ Troubleshooting

**Erro de conexão SSL**: A API já está configurada para ignorar certificados SSL inválidos.

**Timeout**: Aumente o timeout no N8N ou na configuração do Docker se necessário.

**CORS**: Use esta API como proxy para contornar limitações de CORS.
Skip https in n8n with redirects in python
