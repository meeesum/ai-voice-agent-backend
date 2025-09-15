# Logistics Voice Agent Backend

A FastAPI-based backend for an AI-powered voice agent system that handles logistics operations. This backend integrates with OpenAI for AI capabilities, Retell for voice processing, and Supabase for authentication and data storage.

## 🚀 Features

- **FastAPI Framework**: Modern, fast web framework for building APIs
- **AI Integration**: OpenAI API integration for intelligent responses
- **Voice Processing**: Retell API integration for voice agent capabilities
- **Authentication**: Supabase-based authentication system
- **Database**: PostgreSQL database with psycopg2 for direct connections
- **Real-time Communication**: WebSocket support for real-time interactions
- **Webhooks**: Support for external webhook integrations
- **CORS Support**: Cross-origin resource sharing enabled
- **Error Handling**: Comprehensive error handling middleware

## 📁 Project Structure

```
ai-voice-agent-backend/
│
├── readme.md
├── requirements.txt
├── main.py                 # FastAPI app entry point
├── .env                    # Environment variables (not in repo)
├── test_db.py             # Database connection test
│
└── app/
    ├── config.py          # Configuration settings
    ├── schemas.py         # Pydantic models
    │
    ├── db/
    │   ├── __init__.py
    │   ├── base.py        # SQLAlchemy base
    │   ├── models.py      # Database models
    │   ├── session.py     # Database session management
    │   └── init_db.py     # Database initialization
    │
    ├── routers/
    │   ├── __init__.py
    │   ├── auth.py        # Authentication endpoints
    │   ├── calls.py       # Call management endpoints
    │   └── webhook.py     # Webhook endpoints
    │
    ├── services/
    │   ├── __init__.py
    │   ├── openai_client.py   # OpenAI integration
    │   └── retell_client.py   # Retell integration
    │
    ├── dependencies/
    │   ├── __init__.py
    │   └── supabase_auth.py   # Supabase authentication
    │
    ├── middleware/
    │   ├── __init__.py
    │   └── error_handler.py   # Error handling middleware
    │
    ├── schemas/
    │   ├── __init__.py
    │   └── call.py        # Call-related schemas
    │
    ├── utils/
    │   ├── __init__.py
    │   ├── nlp_helpers.py     # NLP utility functions
    │   └── postprocess.py     # Response post-processing
    │
    └── tests/
        ├── __init__.py
        └── test_sample.py     # Sample tests
```

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- PostgreSQL database (or Supabase)
- OpenAI API key
- Retell API key

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/meeesum/ai-voice-agent-backend.git
   cd ai-voice-agent-backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   # source .venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Setup**
   
   Create a `.env` file in the root directory:
   ```env
   # Database Configuration
   db_host=your_db_host
   db_port=5432
   db_name=your_db_name
   db_user=your_db_user
   db_password=your_db_password
   
   # Supabase Configuration
   SUPABASE_URL=your_supabase_url
   SUPABASE_SERVICE_KEY=your_supabase_service_key
   SUPABASE_ANON_KEY=your_supabase_anon_key
   
   # API Keys
   OPENAI_API_KEY=your_openai_api_key
   RETELL_API_KEY=your_retell_api_key
   ```

5. **Initialize Database**
   ```bash
   python -m app.db.init_db
   ```

6. **Test Database Connection**
   ```bash
   python test_db.py
   ```

## 🚦 Running the Application

### Development
```bash
uvicorn main:app --reload
```

### Production
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

The API will be available at:
- **API**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 📚 API Endpoints

### Health Check
- `GET /health` - Service health status

### Authentication
- `POST /auth/login` - User authentication
- `GET /auth/user` - Get current user info

### Calls Management
- `POST /calls/` - Create new call
- `GET /calls/{call_id}` - Get call details
- `PUT /calls/{call_id}` - Update call
- `DELETE /calls/{call_id}` - End call

### Webhooks
- `POST /webhook/retell` - Retell webhook handler
- `POST /webhook/openai` - OpenAI webhook handler

## 🔧 Configuration

The application uses Pydantic Settings for configuration management. All settings are defined in `app/config.py` and can be overridden via environment variables.

### Key Configuration Options:
- **PROJECT_NAME**: Application name
- **VERSION**: Application version
- **Database settings**: PostgreSQL connection parameters
- **API keys**: External service credentials

## 🗄️ Database

The application uses PostgreSQL with psycopg2 for direct database connections. Database models are defined using SQLAlchemy for schema management.

### Key Models:
- **User**: User authentication and profile
- **Call**: Voice call records and metadata
- **Session**: User session management

## 🔒 Authentication

Authentication is handled through Supabase with JWT tokens. The system supports:
- User registration and login
- JWT token validation
- Protected endpoints with user dependencies

## 🤖 AI Integration

### OpenAI Integration
- Chat completions for intelligent responses
- Function calling for structured interactions
- Custom prompts for logistics domain

### Retell Integration
- Voice-to-text conversion
- Text-to-speech synthesis
- Real-time voice streaming

## 🧪 Testing

Run tests using:
```bash
python -m pytest app/tests/
```

## 📦 Dependencies

### Core Dependencies:
- **fastapi**: Web framework
- **uvicorn**: ASGI server
- **pydantic**: Data validation
- **psycopg2-binary**: PostgreSQL adapter
- **sqlalchemy**: ORM
- **httpx**: HTTP client
- **openai**: OpenAI API client
- **python-dotenv**: Environment variable management

## 🚀 Deployment

### Docker (Optional)
```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Environment Variables for Production
Ensure all environment variables are properly set in your production environment.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For support and questions, please open an issue in the GitHub repository.

---

**Built with ❤️ using FastAPI and modern Python tooling**