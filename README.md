# TP2-DEV

Collaborative FastAPI REST API project.

## Installation

```bash
python -m venv .venv
pip install -r requirements.txt
```

## Usage

Start the development server:

```bash
uvicorn main:app --reload
```

The API will be available at:
- **API**: http://127.0.0.1:8000
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Returns a welcome message |
| GET | `/addition?a={int}&b={int}` | Returns the sum of a and b, plus developer name |

## Testing

```bash
curl http://127.0.0.1:8000/
# {"message":"Hello, World!"}
```