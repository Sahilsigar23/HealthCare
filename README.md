# Healthcare Backend System

A comprehensive Django-based backend system for managing healthcare records, including patient management, doctor management, and patient-doctor mappings with JWT authentication.

## Features

- **User Authentication**: JWT-based authentication with register and login endpoints
- **Patient Management**: CRUD operations for patient records (accessible only by the user who created them)
- **Doctor Management**: CRUD operations for doctor records
- **Patient-Doctor Mapping**: Assign doctors to patients and manage relationships
- **Secure API**: All endpoints are protected with JWT authentication
- **PostgreSQL Database**: Robust database management with Django ORM
- **Admin Panel**: Django admin interface for easy data management

## Tech Stack

- **Backend Framework**: Django 5.0.1
- **API Framework**: Django REST Framework 3.14.0
- **Authentication**: djangorestframework-simplejwt 5.3.1
- **Database**: PostgreSQL (psycopg 3.2.13)
- **Environment Management**: python-decouple 3.8
- **CORS**: django-cors-headers 4.3.1

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.10 or higher
- PostgreSQL 12 or higher
- pip (Python package installer)

## Installation & Setup

### 1. Clone the Repository
```bash
cd "HealthCare"
```

### 2. Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup

#### Create PostgreSQL Database
```bash
# Login to PostgreSQL
psql -U postgres

# Create database
CREATE DATABASE healthcare_db;

# Exit psql
\q
```

### 5. Environment Configuration

Create a `.env` file in the root directory (copy from `.env.example`):
```bash
cp .env.example .env
```

Update the `.env` file with your database credentials:
```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=*

# Database Configuration
DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=your-postgres-password
DB_HOST=localhost
DB_PORT=5432

# CORS Settings
CORS_ALLOW_ALL_ORIGINS=True
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

### 6. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin account.

### 8. Run Development Server
```bash
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/`

## API Endpoints

### Authentication APIs

#### Register User
- **URL**: `POST /api/auth/register/`
- **Description**: Register a new user
- **Authentication**: Not required
- **Request Body**:
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "SecurePassword123",
  "password_confirm": "SecurePassword123"
}
```
- **Response**:
```json
{
  "message": "User registered successfully",
  "user": {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "created_at": "2026-01-06T15:00:00Z"
  },
  "tokens": {
    "refresh": "refresh_token_here",
    "access": "access_token_here"
  }
}
```

#### Login User
- **URL**: `POST /api/auth/login/`
- **Description**: Login with existing credentials
- **Authentication**: Not required
- **Request Body**:
```json
{
  "email": "john@example.com",
  "password": "SecurePassword123"
}
```
- **Response**: Same as registration response

### Patient Management APIs

#### Create Patient
- **URL**: `POST /api/patients/`
- **Description**: Add a new patient
- **Authentication**: Required (Bearer Token)
- **Request Body**:
```json
{
  "name": "Jane Smith",
  "age": 35,
  "gender": "F",
  "phone": "1234567890",
  "address": "123 Main St, City",
  "medical_history": "No known allergies"
}
```

#### Get All Patients
- **URL**: `GET /api/patients/`
- **Description**: Retrieve all patients created by authenticated user
- **Authentication**: Required (Bearer Token)

#### Get Patient Details
- **URL**: `GET /api/patients/<id>/`
- **Description**: Get details of a specific patient
- **Authentication**: Required (Bearer Token)

#### Update Patient
- **URL**: `PUT /api/patients/<id>/`
- **Description**: Update patient details
- **Authentication**: Required (Bearer Token)
- **Request Body**: Same as Create Patient (all fields optional)

#### Delete Patient
- **URL**: `DELETE /api/patients/<id>/`
- **Description**: Delete a patient record
- **Authentication**: Required (Bearer Token)

### Doctor Management APIs

#### Create Doctor
- **URL**: `POST /api/doctors/`
- **Description**: Add a new doctor
- **Authentication**: Required (Bearer Token)
- **Request Body**:
```json
{
  "name": "Dr. Sarah Johnson",
  "specialization": "CARDIOLOGY",
  "phone": "9876543210",
  "email": "dr.sarah@hospital.com",
  "experience_years": 10,
  "qualification": "MD, MBBS",
  "address": "456 Hospital Rd, City"
}
```

#### Get All Doctors
- **URL**: `GET /api/doctors/`
- **Description**: Retrieve all doctors
- **Authentication**: Required (Bearer Token)

#### Get Doctor Details
- **URL**: `GET /api/doctors/<id>/`
- **Description**: Get details of a specific doctor
- **Authentication**: Required (Bearer Token)

#### Update Doctor
- **URL**: `PUT /api/doctors/<id>/`
- **Description**: Update doctor details
- **Authentication**: Required (Bearer Token)

#### Delete Doctor
- **URL**: `DELETE /api/doctors/<id>/`
- **Description**: Delete a doctor record
- **Authentication**: Required (Bearer Token)

### Patient-Doctor Mapping APIs

#### Create Mapping
- **URL**: `POST /api/mappings/`
- **Description**: Assign a doctor to a patient
- **Authentication**: Required (Bearer Token)
- **Request Body**:
```json
{
  "patient": 1,
  "doctor": 1,
  "notes": "Regular checkup scheduled"
}
```

#### Get All Mappings
- **URL**: `GET /api/mappings/`
- **Description**: Retrieve all patient-doctor mappings for authenticated user's patients
- **Authentication**: Required (Bearer Token)

#### Get Doctors by Patient
- **URL**: `GET /api/mappings/<patient_id>/`
- **Description**: Get all doctors assigned to a specific patient
- **Authentication**: Required (Bearer Token)

#### Delete Mapping
- **URL**: `DELETE /api/mappings/detail/<id>/`
- **Description**: Remove a doctor from a patient
- **Authentication**: Required (Bearer Token)

## Authentication

All protected endpoints require a JWT Bearer token in the Authorization header:

```
Authorization: Bearer <access_token>
```

### Using Authentication in Requests

After login/registration, you'll receive an access token. Use it in subsequent requests:

**Example with cURL**:
```bash
curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     http://127.0.0.1:8000/api/patients/
```

**Example with Postman**:
1. Go to the Authorization tab
2. Select "Bearer Token" as the type
3. Paste your access token in the Token field

## Project Structure

```
healthcare_backend/
├── authentication/          # User authentication app
│   ├── models.py           # Custom User model
│   ├── serializers.py      # User serializers
│   ├── views.py            # Register/Login views
│   └── urls.py             # Auth URLs
├── patients/               # Patient management app
│   ├── models.py           # Patient model
│   ├── serializers.py      # Patient serializers
│   ├── views.py            # Patient CRUD views
│   └── urls.py             # Patient URLs
├── doctors/                # Doctor management app
│   ├── models.py           # Doctor model
│   ├── serializers.py      # Doctor serializers
│   ├── views.py            # Doctor CRUD views
│   └── urls.py             # Doctor URLs
├── mappings/               # Patient-Doctor mapping app
│   ├── models.py           # Mapping model
│   ├── serializers.py      # Mapping serializers
│   ├── views.py            # Mapping views
│   └── urls.py             # Mapping URLs
├── healthcare_backend/     # Project settings
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py             # WSGI configuration
├── manage.py               # Django management script
├── requirements.txt        # Project dependencies
├── .env.example            # Environment variables example
└── README.md               # This file
```

## Database Models

### User Model
- email (EmailField, unique)
- name (CharField)
- password (hashed)
- is_active, is_staff, is_superuser (BooleanFields)

### Patient Model
- user (ForeignKey to User)
- name, age, gender, phone, address
- medical_history
- created_at, updated_at

### Doctor Model
- name, specialization, phone, email
- experience_years, qualification, address
- created_at, updated_at

### PatientDoctorMapping Model
- patient (ForeignKey to Patient)
- doctor (ForeignKey to Doctor)
- assigned_date, notes
- created_at, updated_at

## Testing the API

### Using Postman

1. Import the collection or manually create requests
2. Register a user: `POST /api/auth/register/`
3. Copy the access token from the response
4. Set the token in Authorization header for subsequent requests
5. Test CRUD operations on patients, doctors, and mappings

### Using cURL

**Register User**:
```bash
curl -X POST http://127.0.0.1:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test User",
    "email": "test@example.com",
    "password": "TestPass123",
    "password_confirm": "TestPass123"
  }'
```

**Create Patient**:
```bash
curl -X POST http://127.0.0.1:8000/api/patients/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Patient",
    "age": 45,
    "gender": "M",
    "phone": "1234567890",
    "address": "123 Street",
    "medical_history": "Diabetes"
  }'
```

## Admin Panel

Access the Django admin panel at `http://127.0.0.1:8000/admin/`

Login with the superuser credentials you created earlier to manage:
- Users
- Patients
- Doctors
- Patient-Doctor Mappings

## Error Handling

The API returns appropriate HTTP status codes:
- `200 OK`: Successful GET, PUT, DELETE
- `201 Created`: Successful POST
- `400 Bad Request`: Validation errors
- `401 Unauthorized`: Invalid or missing authentication
- `404 Not Found`: Resource not found

Error responses include descriptive messages:
```json
{
  "field_name": ["Error message here"]
}
```

## Security Features

- JWT-based authentication
- Password hashing with Django's default hasher
- CSRF protection
- SQL injection protection via Django ORM
- XSS protection
- User-specific data isolation (users can only access their own patients)

## Environment Variables

All sensitive configuration is stored in environment variables:
- `SECRET_KEY`: Django secret key
- `DEBUG`: Debug mode (True/False)
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`: Database credentials

## Troubleshooting

### Database Connection Error
- Ensure PostgreSQL is running
- Verify database credentials in `.env`
- Check if database exists: `psql -U postgres -l`

### Migration Errors
- Delete migration files (except `__init__.py`) and re-run `makemigrations`
- Drop and recreate the database if necessary

### JWT Token Errors
- Ensure token is included in Authorization header
- Check if token has expired (tokens expire after 5 hours)
- Generate a new token by logging in again

## Contributing

1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## License

This project is created for assignment purposes.


