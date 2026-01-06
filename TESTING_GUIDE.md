# Healthcare Backend API - Testing Guide

## 🚀 Quick Start Testing

The server is running at `http://127.0.0.1:8000/`

---

## Method 1: Using Web Browser (Easiest)

### Step 1: View Welcome Page
Open your browser and go to: **http://127.0.0.1:8000/**

You'll see all available endpoints and test credentials!

### Step 2: Access Admin Panel
1. Go to: **http://127.0.0.1:8000/admin/**
2. Login with: **admin@healthcare.com** / **admin@123**
3. Browse through:
   - **Users** - See all 4 registered users
   - **Patients** - View 8 Indian patients with medical histories
   - **Doctors** - Browse 6 doctors from major hospitals
   - **Patient-Doctor Mappings** - See relationships

---

## Method 2: Using PowerShell/Command Prompt (API Testing)

### Step 1: Login to Get JWT Token

Open PowerShell and run:

```powershell
$response = Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/auth/login/" -Method Post -Body (@{
    email = "rajesh.kumar@email.com"
    password = "Test@123"
} | ConvertTo-Json) -ContentType "application/json"

$token = $response.tokens.access
Write-Host "Access Token: $token"
```

Or using curl:
```bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ ^
  -H "Content-Type: application/json" ^
  -d "{\"email\":\"rajesh.kumar@email.com\",\"password\":\"Test@123\"}"
```

**Copy the `access` token from the response!**

### Step 2: Test Patient Endpoints

**Get All Patients:**
```powershell
$headers = @{Authorization = "Bearer $token"}
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/patients/" -Headers $headers
```

Or with curl:
```bash
curl -H "Authorization: Bearer YOUR_TOKEN_HERE" http://127.0.0.1:8000/api/patients/
```

**Get Specific Patient (ID: 1):**
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/patients/1/" -Headers $headers
```

**Create New Patient:**
```powershell
$patientData = @{
    name = "Raj Malhotra"
    age = 42
    gender = "M"
    phone = "9988776655"
    address = "45, Connaught Place, New Delhi - 110001"
    medical_history = "Regular health checkups. No major issues."
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/patients/" -Method Post -Headers $headers -Body $patientData -ContentType "application/json"
```

### Step 3: Test Doctor Endpoints

**Get All Doctors:**
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/doctors/" -Headers $headers
```

**Get Specific Doctor (ID: 1):**
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/doctors/1/" -Headers $headers
```

### Step 4: Test Mapping Endpoints

**Get All Mappings:**
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/mappings/" -Headers $headers
```

**Get Doctors for Specific Patient (Patient ID: 1):**
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/mappings/1/" -Headers $headers
```

---

## Method 3: Using Postman (Recommended for Full Testing)

### Setup Postman:

#### 1. **Login Request:**
- Method: `POST`
- URL: `http://127.0.0.1:8000/api/auth/login/`
- Headers: `Content-Type: application/json`
- Body (raw JSON):
```json
{
  "email": "rajesh.kumar@email.com",
  "password": "Test@123"
}
```
- Click **Send**
- Copy the `access` token from response

#### 2. **Set Authorization for Other Requests:**
- For all subsequent requests:
  - Go to **Authorization** tab
  - Type: **Bearer Token**
  - Token: Paste your access token

#### 3. **Test Patients API:**

**GET All Patients:**
- Method: `GET`
- URL: `http://127.0.0.1:8000/api/patients/`
- Authorization: Bearer Token

**POST Create Patient:**
- Method: `POST`
- URL: `http://127.0.0.1:8000/api/patients/`
- Authorization: Bearer Token
- Body (raw JSON):
```json
{
  "name": "Sanjay Kumar",
  "age": 38,
  "gender": "M",
  "phone": "9876543299",
  "address": "789, Sector 18, Noida - 201301",
  "medical_history": "Hypertension under control. Regular exercise."
}
```

**PUT Update Patient (ID: 1):**
- Method: `PUT`
- URL: `http://127.0.0.1:8000/api/patients/1/`
- Authorization: Bearer Token
- Body (raw JSON):
```json
{
  "age": 46,
  "medical_history": "Updated: Hypertension managed with medication."
}
```

**DELETE Patient (ID: 9):**
- Method: `DELETE`
- URL: `http://127.0.0.1:8000/api/patients/9/`
- Authorization: Bearer Token

#### 4. **Test Doctors API:**

**GET All Doctors:**
- Method: `GET`
- URL: `http://127.0.0.1:8000/api/doctors/`
- Authorization: Bearer Token

**POST Create Doctor:**
- Method: `POST`
- URL: `http://127.0.0.1:8000/api/doctors/`
- Body:
```json
{
  "name": "Dr. Priya Nair",
  "specialization": "GENERAL",
  "phone": "9876543298",
  "email": "dr.priya@hospital.com",
  "experience_years": 7,
  "qualification": "MBBS, General Medicine",
  "address": "City Hospital, Mumbai - 400001"
}
```

#### 5. **Test Mappings API:**

**POST Assign Doctor to Patient:**
- Method: `POST`
- URL: `http://127.0.0.1:8000/api/mappings/`
- Body:
```json
{
  "patient": 1,
  "doctor": 2,
  "notes": "Referred for specialized treatment"
}
```

**GET Doctors for Patient:**
- Method: `GET`
- URL: `http://127.0.0.1:8000/api/mappings/1/`

**DELETE Remove Mapping:**
- Method: `DELETE`
- URL: `http://127.0.0.1:8000/api/mappings/detail/1/`

---

## Method 4: Using Python Requests

Create a file `test_api.py`:

```python
import requests
import json

BASE_URL = "http://127.0.0.1:8000"

# Step 1: Login
login_data = {
    "email": "rajesh.kumar@email.com",
    "password": "Test@123"
}

response = requests.post(f"{BASE_URL}/api/auth/login/", json=login_data)
token = response.json()['tokens']['access']
print(f"Token: {token}\n")

# Set headers with token
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

# Step 2: Get all patients
response = requests.get(f"{BASE_URL}/api/patients/", headers=headers)
print("Patients:", json.dumps(response.json(), indent=2))

# Step 3: Get all doctors
response = requests.get(f"{BASE_URL}/api/doctors/", headers=headers)
print("\nDoctors:", json.dumps(response.json(), indent=2))

# Step 4: Create new patient
new_patient = {
    "name": "Test Patient",
    "age": 30,
    "gender": "M",
    "phone": "9999999999",
    "address": "Test Address",
    "medical_history": "Test history"
}
response = requests.post(f"{BASE_URL}/api/patients/", headers=headers, json=new_patient)
print("\nNew Patient:", json.dumps(response.json(), indent=2))
```

Run: `python test_api.py`

---

## 📝 Test Credentials

### Users:
- **Admin**: admin@healthcare.com / admin@123
- **User 1**: rajesh.kumar@email.com / Test@123
- **User 2**: priya.sharma@email.com / Test@123
- **User 3**: amit.patel@email.com / Test@123

### Database Contains:
- ✅ 4 Users
- ✅ 6 Doctors (Dr. Ramesh Gupta, Dr. Sunita Reddy, etc.)
- ✅ 8 Patients (Suresh Sharma, Anita Verma, etc.)
- ✅ 10 Patient-Doctor Mappings

---

## 🔍 Expected Results

### Successful Login Response:
```json
{
  "message": "Login successful",
  "user": {
    "id": 1,
    "name": "Rajesh Kumar",
    "email": "rajesh.kumar@email.com",
    "created_at": "2026-01-06T..."
  },
  "tokens": {
    "refresh": "eyJ0eXAiOiJKV1QiLC...",
    "access": "eyJ0eXAiOiJKV1QiLC..."
  }
}
```

### Get Patients Response:
```json
[
  {
    "id": 1,
    "name": "Suresh Sharma",
    "age": 45,
    "gender": "M",
    "phone": "9123456780",
    "address": "123, Green Park, New Delhi - 110016",
    "medical_history": "Hypertension, Diabetes Type 2...",
    "user": 1,
    "user_name": "Rajesh Kumar",
    "user_email": "rajesh.kumar@email.com"
  }
]
```

---

## ⚠️ Common Issues

### 1. 401 Unauthorized
**Cause**: Missing or expired token
**Solution**: Login again to get a new token

### 2. 404 Not Found
**Cause**: Wrong endpoint or resource doesn't exist
**Solution**: Check the URL and make sure the resource ID is correct

### 3. 400 Bad Request
**Cause**: Invalid data in request body
**Solution**: Check the request body format and required fields

---

## 📚 Additional Resources

- **Full API Documentation**: See `API_DOCUMENTATION.md`
- **Setup Instructions**: See `README.md`
- **Admin Panel**: http://127.0.0.1:8000/admin/

---

## 🎯 Quick Test Checklist

- [ ] Login with test credentials
- [ ] View all patients (should see 8 patients)
- [ ] View all doctors (should see 6 doctors)
- [ ] Create a new patient
- [ ] Update an existing patient
- [ ] View patient-doctor mappings
- [ ] Assign a doctor to a patient
- [ ] Access admin panel
- [ ] Browse database through admin interface

---

**Happy Testing! 🚀**
