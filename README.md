# Instructions
This is basic template which includes a FastAPI, MongoDB (ORM), Logs, Authentication / Authorisation, and Error Handling.

## Uvicorn (Development)
```bash
pip install requirements
uvicorn main:app --reload
```

## Docker (Production)
```bash
docker build -f Dockerfile . -t fast_api_app
docker run -p 8000:80 -d fast_api_app 
```

### Docker compose
```bash
docker compose up -d --build
```