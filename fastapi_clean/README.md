# FastAPI Clean Architecture Project

A clean, well-structured FastAPI project demonstrating best practices for building scalable web applications with Python.

## 📋 Project Overview

This project implements a Clean Architecture pattern with FastAPI, featuring:
- **Layered Architecture**: Separation of concerns across multiple layers
- **Async Support**: Built with async/await for high performance
- **Database Integration**: SQLAlchemy ORM with async support
- **Authentication**: JWT-based security
- **API Documentation**: Auto-generated Swagger UI and ReDoc
- **Environment Configuration**: Settings management with Pydantic

## 🗂️ Project Structure

```
fastapi_clean/
├── app/
│   ├── api/                    # API route handlers (Controller layer)
│   │   ├── __init__.py
│   │   └── user_routes.py      # User endpoints (GET, POST, PUT, DELETE)
│   │
│   ├── core/                   # Core configuration and utilities
│   │   ├── __init__.py
│   │   ├── config.py           # Application settings (database URL, env vars, etc.)
│   │   └── security.py         # Authentication and authorization logic
│   │
│   ├── db/                     # Database layer
│   │   ├── __init__.py
│   │   ├── database.py         # Database engine, session factory, dependency
│   │   └── models.py           # SQLAlchemy ORM models
│   │
│   ├── repository/             # Data Access layer (Repository pattern)
│   │   ├── __init__.py
│   │   └── user_repo.py        # Database queries for User entity
│   │
│   ├── schemas/                # Request/Response validation models
│   │   ├── __init__.py
│   │   └── user_schema.py      # Pydantic models for User
│   │
│   ├── services/               # Business logic layer
│   │   ├── __init__.py
│   │   └── user_service.py     # User business operations
│   │
│   ├── main.py                 # Application entry point
│   └── __pycache__/
│
├── fast_venv/                  # Python virtual environment
│
├── .env                        # Environment variables (local development)
├── requirements.txt            # Python dependencies
├── users.db                    # SQLite database (generated at runtime)
└── README.md                   # This file

```

## 🏗️ Architecture Layers

### 1. **API Layer** (`api/`)
- Handles HTTP requests and responses
- Contains route definitions and endpoints
- Receives requests and validates input schemas
- Returns responses formatted according to output schemas

### 2. **Service Layer** (`services/`)
- Contains business logic and core application workflows
- Orchestrates data operations
- Handles complex operations that involve multiple repositories
- Independent of HTTP/framework specifics

### 3. **Repository Layer** (`repository/`)
- Data access abstraction layer
- Communicates with the database
- Encapsulates SQL queries and ORM operations
- Makes the service layer database-agnostic

### 4. **Database Layer** (`db/`)
- Database connection and session management
- SQLAlchemy models and ORM definitions
- Database initialization and configuration

### 5. **Schema Layer** (`schemas/`)
- Pydantic models for request/response validation
- Type hints and documentation for APIs
- Automatic validation and serialization

### 6. **Core Layer** (`core/`)
- Application configuration and settings
- Security utilities (JWT, password hashing)
- Environment variable management

## 📦 Dependencies

```
fastapi                 # Web framework
uvicorn                 # ASGI server
sqlalchemy              # ORM and database toolkit
aiosqlite               # Async SQLite driver
asyncpg                 # Async PostgreSQL driver
python-jose             # JWT token handling
passlib[bcrypt]         # Password hashing
python-dotenv           # Environment variable management
pydantic-settings       # Configuration validation
email-validator         # Email validation
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip or poetry

### 1. Clone the Repository
```bash
git clone https://github.com/manishjnits/fastApi_proj.git
cd fastapi_clean
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv fast_venv
fast_venv\Scripts\activate

# Linux/macOS
python -m venv fast_venv
source fast_venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the project root:
```env
APP_NAME=FastAPI Clean
DEBUG=True
DATABASE_URL=sqlite:///./users.db
```

### 5. Run the Application
```bash
uvicorn app.main:app --reload
```

The application will be available at `http://localhost:8000`

## 📚 API Documentation

### Automatic Documentation

Once the application is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### API Endpoints

#### Users
- `GET /users/` - Get all users
- `POST /users/` - Create a new user
- `GET /users/{user_id}` - Get user by ID
- `PUT /users/{user_id}` - Update user
- `DELETE /users/{user_id}` - Delete user

### Example Requests

**Create User:**
```bash
curl -X POST "http://localhost:8000/users/" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com"
  }'
```

**Get All Users:**
```bash
curl "http://localhost:8000/users/"
```

## 🗄️ Database

### Current Setup
- **Database**: SQLite (`users.db`)
- **ORM**: SQLAlchemy 2.0
- **Async Support**: Yes (via aiosqlite)

### Switching Databases

To use PostgreSQL instead:
1. Install PostgreSQL driver: `pip install asyncpg`
2. Update `.env`:
   ```env
   DATABASE_URL=postgresql+asyncpg://user:password@localhost/dbname
   ```
3. Restart the application

## 🔐 Security Features

- Password hashing with bcrypt
- JWT token authentication (if implemented in security.py)
- Input validation via Pydantic schemas
- CORS support (can be configured in main.py)

## 🧪 Testing

To add tests, create a `tests/` directory:
```bash
pytest
```

## 📝 Configuration

Application settings are managed in `app/core/config.py` using Pydantic Settings:
- Environment-based configuration
- Type validation
- IDE autocomplete support

## 🔄 Development Workflow

1. **Define API Contract**: Update schemas in `schemas/`
2. **Create Database Model**: Add model to `db/models.py`
3. **Implement Repository**: Add data access in `repository/`
4. **Write Business Logic**: Add logic in `services/`
5. **Create Endpoints**: Add routes in `api/`

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Manish Jaiswal

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

**Last Updated**: May 9, 2026
