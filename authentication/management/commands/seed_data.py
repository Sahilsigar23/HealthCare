from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from patients.models import Patient
from doctors.models import Doctor
from mappings.models import PatientDoctorMapping

User = get_user_model()


class Command(BaseCommand):
    help = 'Seed database with Indian dummy healthcare data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding database with Indian healthcare data...')

        # Create Users
        users_data = [
            {'email': 'rajesh.kumar@email.com', 'name': 'Rajesh Kumar', 'password': 'Test@123'},
            {'email': 'priya.sharma@email.com', 'name': 'Priya Sharma', 'password': 'Test@123'},
            {'email': 'amit.patel@email.com', 'name': 'Amit Patel', 'password': 'Test@123'},
        ]

        users = []
        for user_data in users_data:
            user, created = User.objects.get_or_create(
                email=user_data['email'],
                defaults={
                    'name': user_data['name']
                }
            )
            if created:
                user.set_password(user_data['password'])
                user.save()
                self.stdout.write(self.style.SUCCESS(f'Created user: {user.name}'))
            users.append(user)

        # Create Admin User
        admin_user, created = User.objects.get_or_create(
            email='admin@healthcare.com',
            defaults={
                'name': 'Admin User',
                'is_staff': True,
                'is_superuser': True
            }
        )
        if created:
            admin_user.set_password('admin@123')
            admin_user.save()
            self.stdout.write(self.style.SUCCESS(f'Created admin: {admin_user.name}'))

        # Create Doctors
        doctors_data = [
            {
                'name': 'Dr. Ramesh Gupta',
                'specialization': 'CARDIOLOGY',
                'phone': '9876543210',
                'email': 'dr.ramesh@aiims.org',
                'experience_years': 15,
                'qualification': 'MBBS, MD (Cardiology), AIIMS Delhi',
                'address': 'AIIMS, Ansari Nagar, New Delhi - 110029'
            },
            {
                'name': 'Dr. Sunita Reddy',
                'specialization': 'PEDIATRICS',
                'phone': '9876543211',
                'email': 'dr.sunita@apollo.org',
                'experience_years': 12,
                'qualification': 'MBBS, MD (Pediatrics), Apollo Hospitals',
                'address': 'Apollo Hospitals, Jubilee Hills, Hyderabad - 500033'
            },
            {
                'name': 'Dr. Vikram Singh',
                'specialization': 'ORTHOPEDICS',
                'phone': '9876543212',
                'email': 'dr.vikram@fortis.org',
                'experience_years': 18,
                'qualification': 'MBBS, MS (Orthopedics), Fortis Hospital',
                'address': 'Fortis Hospital, Sector 62, Noida - 201301'
            },
            {
                'name': 'Dr. Meera Iyer',
                'specialization': 'GYNECOLOGY',
                'phone': '9876543213',
                'email': 'dr.meera@manipal.org',
                'experience_years': 10,
                'qualification': 'MBBS, MD (Gynecology), Manipal Hospital',
                'address': 'Manipal Hospital, HAL Airport Road, Bangalore - 560017'
            },
            {
                'name': 'Dr. Arjun Mehta',
                'specialization': 'NEUROLOGY',
                'phone': '9876543214',
                'email': 'dr.arjun@max.org',
                'experience_years': 20,
                'qualification': 'MBBS, DM (Neurology), Max Hospital',
                'address': 'Max Super Specialty Hospital, Saket, New Delhi - 110017'
            },
            {
                'name': 'Dr. Kavita Desai',
                'specialization': 'DERMATOLOGY',
                'phone': '9876543215',
                'email': 'dr.kavita@medanta.org',
                'experience_years': 8,
                'qualification': 'MBBS, MD (Dermatology), Medanta Hospital',
                'address': 'Medanta The Medicity, Sector 38, Gurgaon - 122001'
            },
        ]

        doctors = []
        for doctor_data in doctors_data:
            doctor, created = Doctor.objects.get_or_create(
                email=doctor_data['email'],
                defaults=doctor_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created doctor: {doctor.name}'))
            doctors.append(doctor)

        # Create Patients
        patients_data = [
            {
                'name': 'Suresh Sharma',
                'age': 45,
                'gender': 'M',
                'phone': '9123456780',
                'address': '123, Green Park, New Delhi - 110016',
                'medical_history': 'Hypertension, Diabetes Type 2. Regular medication for BP control.'
            },
            {
                'name': 'Anita Verma',
                'age': 35,
                'gender': 'F',
                'phone': '9123456781',
                'address': '456, Banjara Hills, Hyderabad - 500034',
                'medical_history': 'Asthma. Uses inhaler daily. No known allergies.'
            },
            {
                'name': 'Ramesh Patil',
                'age': 60,
                'gender': 'M',
                'phone': '9123456782',
                'address': '789, MG Road, Pune - 411001',
                'medical_history': 'Arthritis. Previous knee surgery in 2020. Regular physiotherapy.'
            },
            {
                'name': 'Lakshmi Nair',
                'age': 28,
                'gender': 'F',
                'phone': '9123456783',
                'address': '321, Koramangala, Bangalore - 560034',
                'medical_history': 'Pregnant - 6 months. No complications. First pregnancy.'
            },
            {
                'name': 'Vijay Kumar',
                'age': 52,
                'gender': 'M',
                'phone': '9123456784',
                'address': '654, Rohini Sector 15, New Delhi - 110085',
                'medical_history': 'Migraine. Family history of neurological conditions.'
            },
            {
                'name': 'Deepa Reddy',
                'age': 40,
                'gender': 'F',
                'phone': '9123456785',
                'address': '987, Jubilee Hills, Hyderabad - 500033',
                'medical_history': 'Skin allergies. Sensitive to certain cosmetics and foods.'
            },
            {
                'name': 'Arun Singh',
                'age': 32,
                'gender': 'M',
                'phone': '9123456786',
                'address': '147, Sector 62, Noida - 201301',
                'medical_history': 'Sports injury - ankle. Regular follow-ups required.'
            },
            {
                'name': 'Pooja Kapoor',
                'age': 55,
                'gender': 'F',
                'phone': '9123456787',
                'address': '258, South Extension, New Delhi - 110049',
                'medical_history': 'Thyroid disorder. Regular medication. Annual checkups.'
            },
        ]

        patients = []
        # Distribute patients among users
        for i, patient_data in enumerate(patients_data):
            user = users[i % len(users)]
            patient, created = Patient.objects.get_or_create(
                phone=patient_data['phone'],
                defaults={**patient_data, 'user': user}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created patient: {patient.name}'))
            patients.append(patient)

        # Create Patient-Doctor Mappings
        mappings_data = [
            {'patient_idx': 0, 'doctor_idx': 0, 'notes': 'Regular cardiac checkup scheduled. Monitor BP levels.'},
            {'patient_idx': 1, 'doctor_idx': 1, 'notes': 'Asthma management plan review. Adjust inhaler dosage if needed.'},
            {'patient_idx': 2, 'doctor_idx': 2, 'notes': 'Post-surgery follow-up. Physiotherapy progress evaluation.'},
            {'patient_idx': 3, 'doctor_idx': 3, 'notes': 'Prenatal care. Monthly checkups scheduled.'},
            {'patient_idx': 4, 'doctor_idx': 4, 'notes': 'Migraine treatment plan. MRI scheduled for next month.'},
            {'patient_idx': 5, 'doctor_idx': 5, 'notes': 'Allergy testing completed. Prescribed topical ointments.'},
            {'patient_idx': 6, 'doctor_idx': 2, 'notes': 'Sports injury rehabilitation. Weekly physiotherapy sessions.'},
            {'patient_idx': 7, 'doctor_idx': 0, 'notes': 'Thyroid and cardiac health monitoring. Regular blood tests.'},
            # Additional cross-referrals
            {'patient_idx': 0, 'doctor_idx': 5, 'notes': 'Referred for skin examination related to medication side effects.'},
            {'patient_idx': 3, 'doctor_idx': 1, 'notes': 'Pediatric consultation for post-delivery care planning.'},
        ]

        for mapping_data in mappings_data:
            patient = patients[mapping_data['patient_idx']]
            doctor = doctors[mapping_data['doctor_idx']]
            mapping, created = PatientDoctorMapping.objects.get_or_create(
                patient=patient,
                doctor=doctor,
                defaults={'notes': mapping_data['notes']}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(
                    f'Mapped {patient.name} to {doctor.name}'
                ))

        self.stdout.write(self.style.SUCCESS('\n=== Database Seeded Successfully! ==='))
        self.stdout.write(self.style.SUCCESS(f'Users: {len(users) + 1} (including admin)'))
        self.stdout.write(self.style.SUCCESS(f'Doctors: {len(doctors)}'))
        self.stdout.write(self.style.SUCCESS(f'Patients: {len(patients)}'))
        self.stdout.write(self.style.SUCCESS(f'Mappings: {len(mappings_data)}'))
        self.stdout.write(self.style.SUCCESS('\n=== Login Credentials ==='))
        self.stdout.write(self.style.WARNING('Admin: admin@healthcare.com / admin@123'))
        self.stdout.write(self.style.WARNING('User 1: rajesh.kumar@email.com / Test@123'))
        self.stdout.write(self.style.WARNING('User 2: priya.sharma@email.com / Test@123'))
        self.stdout.write(self.style.WARNING('User 3: amit.patel@email.com / Test@123'))
