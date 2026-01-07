# 📘 Healthcare Backend API Documentation

## Base URL
```
Local Development: http://127.0.0.1:8000
Production: https://your-app.onrender.com
```

## Authentication

All endpoints (except register and login) require JWT authentication.

**Add this header to authenticated requests:**
```
Authorization: Bearer <your_access_token>
```

**Token Expiry:** Access tokens expire after 5 hours

---

# 🔐 Authentication Endpoints

## 1. Register User

Register a new user account.

### Request
```http
POST /api/auth/register/
Content-Type: application/json
```

### Request Body
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "SecurePassword123",
  "password_confirm": "SecurePassword123"
}
```

### Parameters
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| name | string | Yes | User's full name |
| email | string | Yes | Valid email address (must be unique) |
| password | string | Yes | Min 8 characters, validated by Django |
| password_confirm | string | Yes | Must match password |

### Success Response (201 Created)
```json
{
  "message": "User registered successfully",
  "user": {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "created_at": "2026-01-07T15:00:00Z"
  },
  "tokens": {
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
  }
}
```

### Error Response (400 Bad Request)
```json
{
  "email": ["User with this email already exists."],
  "password": ["Password fields didn't match."]
}
```

---

## 2. Login User

Authenticate and receive JWT tokens.

### Request
```http
POST /api/auth/login/
Content-Type: application/json
```

### Request Body
```json
{
  "email": "rajesh.kumar@email.com",
  "password": "Test@123"
}
```

### Parameters
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| email | string | Yes | Registered email address |
| password | string | Yes | User's password |

### Success Response (200 OK)
```json
{
  "message": "Login successful",
  "user": {
    "id": 1,
    "name": "Rajesh Kumar",
    "email": "rajesh.kumar@email.com",
    "created_at": "2026-01-06T10:00:00Z"
  },
  "tokens": {
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
  }
}
```

### Error Response (401 Unauthorized)
```json
{
  "error": "Invalid email or password"
}
```

---

# 🏥 Patient Management Endpoints

## 3. Get All Patients

Retrieve all patients created by the authenticated user.

### Request
```http
GET /api/patients/
Authorization: Bearer <access_token>
```

### Success Response (200 OK)
```json
[
  {
    "id": 1,
    "name": "Suresh Sharma",
    "age": 45,
    "gender": "M",
    "phone": "9123456780",
    "address": "123, Green Park, New Delhi - 110016",
    "medical_history": "Hypertension, Diabetes Type 2. Regular medication for BP control.",
    "user": 1,
    "user_name": "Rajesh Kumar",
    "user_email": "rajesh.kumar@email.com",
    "created_at": "2026-01-06T10:00:00Z",
    "updated_at": "2026-01-06T10:00:00Z"
  },
  {
    "id": 2,
    "name": "Anita Verma",
    "age": 35,
    "gender": "F",
    ...
  }
]
```

### Notes
- Returns only patients created by the authenticated user
- Empty array `[]` if user has no patients

---

## 4. Get Patient by ID

Retrieve details of a specific patient.

### Request
```http
GET /api/patients/{id}/
Authorization: Bearer <access_token>
```

### Path Parameters
| Parameter | Type | Description |
|-----------|------|-------------|
| id | integer | Patient ID |

### Success Response (200 OK)
```json
{
  "id": 1,
  "name": "Suresh Sharma",
  "age": 45,
  "gender": "M",
  "phone": "9123456780",
  "address": "123, Green Park, New Delhi - 110016",
  "medical_history": "Hypertension, Diabetes Type 2. Regular medication for BP control.",
  "user": 1,
  "user_name": "Rajesh Kumar",
  "user_email": "rajesh.kumar@email.com",
  "created_at": "2026-01-06T10:00:00Z",
  "updated_at": "2026-01-06T10:00:00Z"
}
```

### Error Response (404 Not Found)
```json
{
  "detail": "Not found."
}
```

---

## 5. Create Patient

Add a new patient record.

### Request
```http
POST /api/patients/
Authorization: Bearer <access_token>
Content-Type: application/json
```

### Request Body
```json
{
  "name": "Raj Malhotra",
  "age": 42,
  "gender": "M",
  "phone": "9876543221",
  "address": "456, Sector 21, Gurgaon - 122001",
  "medical_history": "No major health issues. Regular checkups recommended."
}
```

### Parameters
| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| name | string | Yes | Max 255 characters |
| age | integer | Yes | 0-150 |
| gender | string | Yes | 'M', 'F', or 'O' |
| phone | string | Yes | Min 10 characters |
| address | string | Yes | Text field |
| medical_history | string | No | Text field, can be empty |

### Success Response (201 Created)
```json
{
  "message": "Patient created successfully",
  "patient": {
    "id": 9,
    "name": "Raj Malhotra",
    "age": 42,
    "gender": "M",
    "phone": "9876543221",
    "address": "456, Sector 21, Gurgaon - 122001",
    "medical_history": "No major health issues. Regular checkups recommended.",
    "user": 1,
    "user_name": "Rajesh Kumar",
    "user_email": "rajesh.kumar@email.com",
    "created_at": "2026-01-07T15:00:00Z",
    "updated_at": "2026-01-07T15:00:00Z"
  }
}
```

### Error Response (400 Bad Request)
```json
{
  "age": ["Age must be between 0 and 150."],
  "phone": ["Phone number must be at least 10 characters."],
  "gender": ["\"X\" is not a valid choice."]
}
```

---

## 6. Update Patient

Update an existing patient's details. Supports partial updates.

### Request
```http
PUT /api/patients/{id}/
Authorization: Bearer <access_token>
Content-Type: application/json
```

### Path Parameters
| Parameter | Type | Description |
|-----------|------|-------------|
| id | integer | Patient ID to update |

### Request Body (All fields optional for partial update)
```json
{
  "age": 43,
  "medical_history": "Updated: Hypertension well-controlled with medication. Last checkup on 05/01/2026."
}
```

### Success Response (200 OK)
```json
{
  "message": "Patient updated successfully",
  "patient": {
    "id": 1,
    "name": "Suresh Sharma",
    "age": 43,
    "gender": "M",
    "phone": "9123456780",
    "address": "123, Green Park, New Delhi - 110016",
    "medical_history": "Updated: Hypertension well-controlled with medication. Last checkup on 05/01/2026.",
    "user": 1,
    "user_name": "Rajesh Kumar",
    "user_email": "rajesh.kumar@email.com",
    "created_at": "2026-01-06T10:00:00Z",
    "updated_at": "2026-01-07T15:30:00Z"
  }
}
```

### Error Response (404 Not Found)
```json
{
  "detail": "Not found."
}
```

---

## 7. Delete Patient

Delete a patient record.

### Request
```http
DELETE /api/patients/{id}/
Authorization: Bearer <access_token>
```

### Path Parameters
| Parameter | Type | Description |
|-----------|------|-------------|
| id | integer | Patient ID to delete |

### Success Response (200 OK)
```json
{
  "message": "Patient deleted successfully"
}
```

### Error Response (404 Not Found)
```json
{
  "detail": "Not found."
}
```

---

# 🩺 Doctor Management Endpoints

## 8. Get All Doctors

Retrieve all doctors in the system (public data).

### Request
```http
GET /api/doctors/
Authorization: Bearer <access_token>
```

### Success Response (200 OK)
```json
[
  {
    "id": 1,
    "name": "Dr. Ramesh Gupta",
    "specialization": "CARDIOLOGY",
    "phone": "9876543210",
    "email": "dr.ramesh@aiims.org",
    "experience_years": 15,
    "qualification": "MBBS, MD (Cardiology), AIIMS Delhi",
    "address": "AIIMS, Ansari Nagar, New Delhi - 110029",
    "created_at": "2026-01-06T10:00:00Z",
    "updated_at": "2026-01-06T10:00:00Z"
  },
  ...
]
```

---

## 9. Get Doctor by ID

Retrieve details of a specific doctor.

### Request
```http
GET /api/doctors/{id}/
Authorization: Bearer <access_token>
```

### Path Parameters
| Parameter | Type | Description |
|-----------|------|-------------|
| id | integer | Doctor ID |

### Success Response (200 OK)
```json
{
  "id": 1,
  "name": "Dr. Ramesh Gupta",
  "specialization": "CARDIOLOGY",
  "phone": "9876543210",
  "email": "dr.ramesh@aiims.org",
  "experience_years": 15,
  "qualification": "MBBS, MD (Cardiology), AIIMS Delhi",
  "address": "AIIMS, Ansari Nagar, New Delhi - 110029",
  "created_at": "2026-01-06T10:00:00Z",
  "updated_at": "2026-01-06T10:00:00Z"
}
```

---

## 10. Create Doctor

Add a new doctor to the system.

### Request
```http
POST /api/doctors/
Authorization: Bearer <access_token>
Content-Type: application/json
```

### Request Body
```json
{
  "name": "Dr. Anjali Verma",
  "specialization": "CARDIOLOGY",
  "phone": "9876543222",
  "email": "dr.anjali@hospital.com",
  "experience_years": 12,
  "qualification": "MBBS, MD (Cardiology), Fellowship in Interventional Cardiology",
  "address": "Apollo Hospitals, Greams Road, Chennai - 600006"
}
```

### Parameters
| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| name | string | Yes | Max 255 characters |
| specialization | string | Yes | See specializations below |
| phone | string | Yes | Min 10 characters |
| email | string | Yes | Valid email, must be unique |
| experience_years | integer | Yes | 0-70 |
| qualification | string | Yes | Max 255 characters |
| address | string | Yes | Text field |

### Available Specializations
- `CARDIOLOGY` - Cardiology
- `NEUROLOGY` - Neurology
- `ORTHOPEDICS` - Orthopedics
- `PEDIATRICS` - Pediatrics
- `GYNECOLOGY` - Gynecology
- `DERMATOLOGY` - Dermatology
- `PSYCHIATRY` - Psychiatry
- `GENERAL` - General Medicine
- `OTHER` - Other

### Success Response (201 Created)
```json
{
  "message": "Doctor created successfully",
  "doctor": {
    "id": 7,
    "name": "Dr. Anjali Verma",
    "specialization": "CARDIOLOGY",
    "phone": "9876543222",
    "email": "dr.anjali@hospital.com",
    "experience_years": 12,
    "qualification": "MBBS, MD (Cardiology), Fellowship in Interventional Cardiology",
    "address": "Apollo Hospitals, Greams Road, Chennai - 600006",
    "created_at": "2026-01-07T15:45:00Z",
    "updated_at": "2026-01-07T15:45:00Z"
  }
}
```

### Error Response (400 Bad Request)
```json
{
  "email": ["A doctor with this email already exists."],
  "experience_years": ["Experience years must be between 0 and 70."]
}
```

---

## 11. Update Doctor

Update doctor details. Supports partial updates.

### Request
```http
PUT /api/doctors/{id}/
Authorization: Bearer <access_token>
Content-Type: application/json
```

### Request Body (All fields optional)
```json
{
  "experience_years": 13,
  "phone": "9876543223"
}
```

### Success Response (200 OK)
```json
{
  "message": "Doctor updated successfully",
  "doctor": {
    "id": 1,
    "name": "Dr. Ramesh Gupta",
    "experience_years": 13,
    "phone": "9876543223",
    ...
  }
}
```

---

## 12. Delete Doctor

Delete a doctor record.

### Request
```http
DELETE /api/doctors/{id}/
Authorization: Bearer <access_token>
```

### Success Response (200 OK)
```json
{
  "message": "Doctor deleted successfully"
}
```

---

# 🔗 Patient-Doctor Mapping Endpoints

## 13. Get All Mappings

Retrieve all patient-doctor mappings for authenticated user's patients.

### Request
```http
GET /api/mappings/
Authorization: Bearer <access_token>
```

### Success Response (200 OK)
```json
[
  {
    "id": 1,
    "patient": 1,
    "doctor": 1,
    "patient_name": "Suresh Sharma",
    "doctor_name": "Dr. Ramesh Gupta",
    "doctor_specialization": "CARDIOLOGY",
    "assigned_date": "2026-01-06",
    "notes": "Regular cardiac checkup scheduled. Monitor BP levels."
  },
  ...
]
```

---

## 14. Get Doctors by Patient ID

Get all doctors assigned to a specific patient.

### Request
```http
GET /api/mappings/{patient_id}/
Authorization: Bearer <access_token>
```

### Path Parameters
| Parameter | Type | Description |
|-----------|------|-------------|
| patient_id | integer | Patient ID |

### Success Response (200 OK)
```json
{
  "patient_id": 1,
  "patient_name": "Suresh Sharma",
  "doctors": [
    {
      "id": 1,
      "patient": 1,
      "doctor": 1,
      "patient_name": "Suresh Sharma",
      "doctor_name": "Dr. Ramesh Gupta",
      "doctor_specialization": "CARDIOLOGY",
      "assigned_date": "2026-01-06",
      "notes": "Regular cardiac checkup scheduled."
    },
    {
      "id": 9,
      "patient": 1,
      "doctor": 5,
      "doctor_name": "Dr. Kavita Desai",
      "doctor_specialization": "DERMATOLOGY",
      ...
    }
  ]
}
```

---

## 15. Assign Doctor to Patient

Create a patient-doctor mapping.

### Request
```http
POST /api/mappings/
Authorization: Bearer <access_token>
Content-Type: application/json
```

### Request Body
```json
{
  "patient": 1,
  "doctor": 2,
  "notes": "Referred for pediatric consultation. Follow-up in 2 weeks."
}
```

### Parameters
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| patient | integer | Yes | Patient ID (must belong to authenticated user) |
| doctor | integer | Yes | Doctor ID |
| notes | string | No | Consultation notes |

### Success Response (201 Created)
```json
{
  "message": "Doctor assigned to patient successfully",
  "mapping": {
    "id": 11,
    "patient": 1,
    "doctor": 2,
    "patient_name": "Suresh Sharma",
    "doctor_name": "Dr. Sunita Reddy",
    "patient_details": {
      "id": 1,
      "name": "Suresh Sharma",
      "age": 45,
      ...
    },
    "doctor_details": {
      "id": 2,
      "name": "Dr. Sunita Reddy",
      "specialization": "PEDIATRICS",
      ...
    },
    "assigned_date": "2026-01-07",
    "notes": "Referred for pediatric consultation. Follow-up in 2 weeks.",
    "created_at": "2026-01-07T16:00:00Z",
    "updated_at": "2026-01-07T16:00:00Z"
  }
}
```

### Error Response (400 Bad Request)
```json
{
  "patient": ["You can only assign doctors to your own patients."]
}
```

### Validation Rules
- Patient must belong to authenticated user
- Cannot create duplicate mapping (same patient + doctor)
- Both patient and doctor must exist

---

## 16. Get Mapping Details

Get details of a specific patient-doctor mapping.

### Request
```http
GET /api/mappings/detail/{id}/
Authorization: Bearer <access_token>
```

### Success Response (200 OK)
```json
{
  "id": 1,
  "patient": 1,
  "doctor": 1,
  "patient_name": "Suresh Sharma",
  "doctor_name": "Dr. Ramesh Gupta",
  "patient_details": { ... },
  "doctor_details": { ... },
  "assigned_date": "2026-01-06",
  "notes": "Regular cardiac checkup scheduled.",
  "created_at": "2026-01-06T10:00:00Z",
  "updated_at": "2026-01-06T10:00:00Z"
}
```

---

## 17. Remove Doctor from Patient

Delete a patient-doctor mapping.

### Request
```http
DELETE /api/mappings/detail/{id}/
Authorization: Bearer <access_token>
```

### Path Parameters
| Parameter | Type | Description |
|-----------|------|-------------|
| id | integer | Mapping ID |

### Success Response (200 OK)
```json
{
  "message": "Doctor removed from patient successfully"
}
```

---

# 📊 Response Status Codes

| Code | Meaning | Description |
|------|---------|-------------|
| 200 | OK | Successful GET, PUT, DELETE |
| 201 | Created | Successful POST |
| 400 | Bad Request | Invalid data or validation error |
| 401 | Unauthorized | Missing or invalid authentication |
| 404 | Not Found | Resource doesn't exist |
| 500 | Server Error | Internal server error |

---

# 🔒 Security Features

## Authentication
- JWT (JSON Web Token) based
- Tokens expire after 5 hours
- Refresh tokens valid for 1 day

## Password Security
- Django password validation
- Minimum 8 characters
- Cannot be too common
- Cannot be similar to email

## Data Isolation
- Users can only view/edit their own patients
- Doctors are public (viewable by all)
- Mappings filtered by patient ownership

## SQL Injection Protection
- Django ORM prevents SQL injection
- All inputs are parameterized

---

# 📝 Examples

## Example 1: Complete Patient Workflow

### 1. Login
```bash
POST /api/auth/login/
{
  "email": "rajesh.kumar@email.com",
  "password": "Test@123"
}

# Save the access token
```

### 2. Create Patient
```bash
POST /api/patients/
Authorization: Bearer {token}
{
  "name": "New Patient",
  "age": 35,
  "gender": "M",
  "phone": "9876543230",
  "address": "Test Address",
  "medical_history": "Test history"
}

# Patient created with ID: 9
```

### 3. Get All Doctors
```bash
GET /api/doctors/
Authorization: Bearer {token}

# See list of 6 doctors
```

### 4. Assign Doctor
```bash
POST /api/mappings/
Authorization: Bearer {token}
{
  "patient": 9,
  "doctor": 1,
  "notes": "Initial consultation"
}
```

### 5. View Patient's Doctors
```bash
GET /api/mappings/9/
Authorization: Bearer {token}

# See Dr. Ramesh Gupta assigned
```

---

## Example 2: User Isolation Test

### Login as User 1 (Rajesh)
```bash
POST /api/auth/login/
{"email": "rajesh.kumar@email.com", "password": "Test@123"}
# Token: token1
```

### Get Patients
```bash
GET /api/patients/
Authorization: Bearer {token1}
# Returns: 3 patients (IDs: 1, 2, 3)
```

### Login as User 2 (Priya)
```bash
POST /api/auth/login/
{"email": "priya.sharma@email.com", "password": "Test@123"}
# Token: token2
```

### Get Patients Again
```bash
GET /api/patients/
Authorization: Bearer {token2}
# Returns: 3 DIFFERENT patients (IDs: 4, 5, 6)
```

✅ **Proves data isolation works!**

---

# 🧪 Test Credentials

## Users

| Name | Email | Password | Role | Patients |
|------|-------|----------|------|----------|
| Admin User | admin@healthcare.com | admin@123 | Superuser | All (8) |
| Rajesh Kumar | rajesh.kumar@email.com | Test@123 | User | 3 |
| Priya Sharma | priya.sharma@email.com | Test@123 | User | 3 |
| Amit Patel | amit.patel@email.com | Test@123 | User | 2 |

## Doctors (IDs 1-6)

| ID | Name | Specialization | Hospital |
|----|------|----------------|----------|
| 1 | Dr. Ramesh Gupta | CARDIOLOGY | AIIMS Delhi |
| 2 | Dr. Sunita Reddy | PEDIATRICS | Apollo Hyderabad |
| 3 | Dr. Vikram Singh | ORTHOPEDICS | Fortis Noida |
| 4 | Dr. Meera Iyer | GYNECOLOGY | Manipal Bangalore |
| 5 | Dr. Arjun Mehta | NEUROLOGY | Max Delhi |
| 6 | Dr. Kavita Desai | DERMATOLOGY | Medanta Gurgaon |

## Patients (IDs 1-8)

| ID | Name | Age | Gender | Owner |
|----|------|-----|--------|-------|
| 1 | Suresh Sharma | 45 | M | Rajesh |
| 2 | Anita Verma | 35 | F | Rajesh |
| 3 | Ramesh Patil | 60 | M | Rajesh |
| 4 | Lakshmi Nair | 28 | F | Priya |
| 5 | Vijay Kumar | 52 | M | Priya |
| 6 | Deepa Reddy | 40 | F | Priya |
| 7 | Arun Singh | 32 | M | Amit |
| 8 | Pooja Kapoor | 55 | F | Amit |

---

# 🛠️ Common Use Cases

## Use Case 1: Register New User
```http
POST /api/auth/register/
{
  "name": "New User",
  "email": "newuser@email.com",
  "password": "NewPass@123",
  "password_confirm": "NewPass@123"
}
```

## Use Case 2: Add Patient with Medical History
```http
POST /api/patients/
Authorization: Bearer {token}
{
  "name": "Patient Name",
  "age": 50,
  "gender": "M",
  "phone": "9876543240",
  "address": "Full address with pincode",
  "medical_history": "Detailed medical history including previous surgeries, allergies, current medications, etc."
}
```

## Use Case 3: Multi-Doctor Assignment
```http
# Assign Cardiologist
POST /api/mappings/
{"patient": 1, "doctor": 1, "notes": "Cardiac evaluation"}

# Assign Dermatologist (same patient)
POST /api/mappings/
{"patient": 1, "doctor": 6, "notes": "Skin condition check"}

# View all doctors for patient
GET /api/mappings/1/
```

---

# ⚠️ Error Handling

## Validation Errors (400)
```json
{
  "field_name": ["Error message describing the issue"]
}
```

## Authentication Errors (401)
```json
{
  "detail": "Authentication credentials were not provided."
}
```

## Permission Errors (403)
```json
{
  "patient": ["You can only assign doctors to your own patients."]
}
```

## Not Found Errors (404)
```json
{
  "detail": "Not found."
}
```

---

# 📚 Additional Information

## Gender Choices
- `M` - Male
- `F` - Female
- `O` - Other

## Date Formats
All dates are in ISO 8601 format:
- DateTime: `"2026-01-07T15:45:00Z"`
- Date: `"2026-01-07"`

## Field Validations
- **Email:** Must be valid email format
- **Phone:** Minimum 10 characters
- **Age:** Must be between 0 and 150
- **Experience:** Must be between 0 and 70

## Unique Constraints
- User email must be unique
- Doctor email must be unique
- Patient-Doctor mapping (patient + doctor) must be unique

---

# 🔧 Rate Limiting

**Current:** No rate limiting implemented
**Recommendation:** Add rate limiting for production

---

# 📞 API Support

For issues or questions:
- Check error message in response
- Review this documentation
- Check server logs
- Verify authentication token

---

**Last Updated:** January 7, 2026
**Version:** 1.0.0
**Server:** http://127.0.0.1:8000/
