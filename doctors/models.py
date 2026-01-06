from django.db import models


class Doctor(models.Model):
    """Model for storing doctor information."""
    
    SPECIALIZATION_CHOICES = [
        ('CARDIOLOGY', 'Cardiology'),
        ('NEUROLOGY', 'Neurology'),
        ('ORTHOPEDICS', 'Orthopedics'),
        ('PEDIATRICS', 'Pediatrics'),
        ('GYNECOLOGY', 'Gynecology'),
        ('DERMATOLOGY', 'Dermatology'),
        ('PSYCHIATRY', 'Psychiatry'),
        ('GENERAL', 'General Medicine'),
        ('OTHER', 'Other'),
    ]
    
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=50, choices=SPECIALIZATION_CHOICES)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    experience_years = models.IntegerField(help_text='Years of experience')
    qualification = models.CharField(max_length=255)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Dr. {self.name} - {self.specialization}"
    
    class Meta:
        db_table = 'doctors'
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'
        ordering = ['-created_at']
