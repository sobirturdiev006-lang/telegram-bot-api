# Telegram Bot API - Account Management

A Django REST Framework-based backend API for managing Telegram user accounts. This service handles user registration, profile management, and data persistence for Telegram bot applications.

## 🎯 Project Overview

This portfolio project demonstrates:
- RESTful API design using Django REST Framework
- Database modeling with proper validation
- Error handling and exception management
- CORS configuration for cross-origin requests
- Comprehensive API testing
- Security best practices

## 📁 Project Structure

`
telegram-bot-api/
├── api/                          # Main application
│   ├── models.py                 # Account model with validation
│   ├── serializers.py            # DRF serializers for API
│   ├── views.py                  # API views and endpoints
│   ├── urls.py                   # URL routing
│   ├── admin.py                  # Django admin interface
│   ├── tests.py                  # Comprehensive test suite
│   └── migrations/               # Database migrations
├── config/                       # Project configuration
│   ├── settings.py               # Django settings
│   ├── urls.py                   # Main URL configuration
│   └── wsgi.py                   # WSGI application
├── manage.py                     # Django management script
├── requirements.txt              # Project dependencies
├── .env.example                  # Environment variables template
└── README.md                     # This file
`

## 🛠️ Technologies

- **Python 3.11+** - Programming language
- **Django 6.0** - Web framework
- **Django REST Framework 3.16** - API framework
- **django-cors-headers 4.3** - CORS support
- **Pillow 12.1** - Image processing
- **pytest 8.1** - Testing framework
- **python-dotenv 1.2** - Environment management

## 📋 Requirements

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## 🚀 Installation & Setup

### 1. Clone Repository
`ash
git clone https://github.com/sobirturdiev006-lang/telegram-bot-api.git
cd telegram-bot-api
`

### 2. Create Virtual Environment
`ash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
`

### 3. Install Dependencies
`ash
pip install -r requirements.txt
`

### 4. Configure Environment Variables
`ash
cp .env.example .env
`

Edit .env and set the following:
`env
SECRET_KEY=your-secret-key-here-generate-a-secure-one
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000
`

### 5. Run Database Migrations
`ash
python manage.py migrate
`

### 6. Create Superuser (Optional)
`ash
python manage.py createsuperuser
`

### 7. Start Development Server
`ash
python manage.py runserver
`

Server will be available at: http://localhost:8000

## 📚 API Endpoints

### 1. Create Account (User Registration)
- **Method:** POST
- **URL:** /api/start/
- **Description:** Register a new Telegram user account

**Request Body:**
`json
{
  "first_name": "John",
  "last_name": "Doe",
  "username": "johndoe",
  "telegram_id": "123456789"
}
`

**Success Response (201 Created):**
`json
{
  "status": "success",
  "message": "Account successfully created",
  "data": {
    "first_name": "John",
    "last_name": "Doe",
    "username": "johndoe",
    "telegram_id": "123456789"
  }
}
`

**Error Response (400 Bad Request):**
`json
{
  "status": "error",
  "message": "Account could not be created",
  "errors": "Telegram ID already registered"
}
`

### 2. List All Accounts
- **Method:** GET
- **URL:** /api/accounts/
- **Description:** Retrieve all registered accounts with pagination

**Response (200 OK):**
`json
{
  "count": 5,
  "next": "http://localhost:8000/api/accounts/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "first_name": "John",
      "last_name": "Doe",
      "username": "johndoe",
      "telegram_id": "123456789",
      "phone_number": null,
      "image": null,
      "created_at": "2025-07-10T12:00:00Z",
      "updated_at": "2025-07-10T12:00:00Z"
    }
  ]
}
`

## 📊 Account Model

| Field | Type | Validation | Description |
|-------|------|-----------|-------------|
| id | Integer | Primary Key | Unique account identifier |
| irst_name | CharField(100) | Optional | User's first name |
| last_name | CharField(100) | Optional | User's last name |
| username | CharField(100) | Optional | Telegram username |
| 	elegram_id | CharField(100) | Unique, Required | Unique Telegram user ID |
| phone_number | CharField(20) | Regex Validation | Phone number with format +998XXXXXXXXX |
| image | ImageField | Optional | User profile image |
| created_at | DateTime | Auto | Account creation timestamp |
| updated_at | DateTime | Auto | Last update timestamp |

### Model Methods

**full_name (property):**
- Returns concatenated first and last name
- Handles null values gracefully
- Returns 'Unknown User' if both names are null

**__str__:**
- Returns full name or username or Telegram ID as string representation

## 🧪 Testing

### Run All Tests
`ash
pytest
`

### Run Specific Test File
`ash
pytest api/tests.py
`

### Run Specific Test Class
`ash
pytest api/tests.py::AccountModelTestCase
`

### Run with Coverage
`ash
pytest --cov=api api/tests.py
`

### Test Coverage
The test suite includes:
- **Model Tests:** Account creation, validation, string representation
- **API Tests:** Account registration, duplicate handling, list retrieval
- **Validation Tests:** Phone number format, required fields
- **Edge Cases:** Null values, missing fields

## 🔒 Security Features

- ✅ Environment-based settings (no hardcoded secrets)
- ✅ CORS configuration for controlled cross-origin access
- ✅ Input validation and error handling
- ✅ Phone number format validation
- ✅ Unique constraint on telegram_id
- ✅ XSS protection enabled
- ✅ CSRF middleware protection
- ✅ Conditional DEBUG mode based on environment

## 🐛 Error Handling

All endpoints return consistent error responses:

`json
{
  "status": "error",
  "message": "Human-readable error message",
  "errors": "Detailed error information"
}
`

Common error codes:
- **400 Bad Request:** Validation error, missing required fields
- **201 Created:** Account successfully created
- **200 OK:** Successful data retrieval

## 📖 Admin Interface

Access Django admin at: http://localhost:8000/admin

**Admin Features:**
- View and manage user accounts
- Search accounts by name, username, or telegram_id
- Filter accounts by creation date
- Upload/manage user profile images
- View metadata (created_at, updated_at)

## 🔧 Development

### Code Quality
- Type hints in function signatures
- Comprehensive docstrings
- Clear error messages
- Proper exception handling

### Best Practices Implemented
- DRY (Don't Repeat Yourself)
- Separation of concerns (Models, Views, Serializers)
- RESTful API design principles
- Consistent naming conventions
- Proper HTTP status codes

## 📝 Environment Variables

Create .env file in the project root:

`env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=False

# Allowed Hosts
ALLOWED_HOSTS=localhost,127.0.0.1

# CORS Configuration
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000
`

## 🚀 Deployment

### Before Deployment
1. Set DEBUG=False in .env
2. Generate a secure SECRET_KEY
3. Set appropriate ALLOWED_HOSTS
4. Configure CORS_ALLOWED_ORIGINS
5. Use a production database (PostgreSQL recommended)
6. Set up proper static file serving
7. Use HTTPS in production

### Production Database Setup
Update settings.py to use PostgreSQL:
`python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'telegram_bot_api',
        'USER': 'postgres',
        'PASSWORD': 'your-password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
`

## 📄 License

MIT License - See LICENSE file for details

## 👤 Author

**Sobirjon Turdiev**
- GitHub: [@sobirturdiev006-lang](https://github.com/sobirturdiev006-lang)

## 📧 Support

For issues, questions, or suggestions, please create an issue on GitHub.

---

**Last Updated:** July 10, 2025
