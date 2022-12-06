# Instructions

## Development
```bash
pip install requirements
uvicorn main:app --reload
```

## Production
```bash
docker build -f Dockerfile . -t fast_api_app
docker run -p 8000:80 -d fast_api_app 
```
