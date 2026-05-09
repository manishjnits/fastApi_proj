# FaslaAPI Project

A clean FastAPI project structure.

## Project Structure

```
faslapi_clean/
├── app/
│   ├── api/               # API route handlers
│   ├── core/              # Configuration
│   ├── db/                # Database setup and models
│   ├── repository/        # Data access layer
│   ├── schemas/           # Pydantic schemas
│   ├── services/          # Business logic
│   └── main.py            # Application entry point
├── requirements.txt       # Python dependencies
└── README.md
```

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

## API Documentation

Once running, visit `http://localhost:8000/docs` for Swagger UI documentation.
