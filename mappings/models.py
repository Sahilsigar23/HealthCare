from django.db import models
from patients.models import Patient
from doctors.models import Doctor


class PatientDoctorMapping(models.Model):
    """Model for storing patient-doctor mappings."""
    
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='doctor_mappings'
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='patient_mappings'
    )
    assigned_date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.patient.name} - Dr. {self.doctor.name}"
    
    class Meta:
        db_table = 'patient_doctor_mappings'
        verbose_name = 'Patient-Doctor Mapping'
        verbose_name_plural = 'Patient-Doctor Mappings'
        unique_together = ['patient', 'doctor']  # Prevent duplicate mappings
        ordering = ['-created_at']
