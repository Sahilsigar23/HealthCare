from django.contrib import admin
from .models import PatientDoctorMapping


@admin.register(PatientDoctorMapping)
class PatientDoctorMappingAdmin(admin.ModelAdmin):
    """Admin configuration for PatientDoctorMapping model."""
    
    list_display = ['patient', 'doctor', 'assigned_date', 'created_at']
    list_filter = ['assigned_date', 'created_at']
    search_fields = ['patient__name', 'doctor__name', 'notes']
    ordering = ['-created_at']
    readonly_fields = ['assigned_date', 'created_at', 'updated_at']
    
    fieldsets = (
        ('Mapping Information', {
            'fields': ('patient', 'doctor', 'notes')
        }),
        ('Timestamps', {
            'fields': ('assigned_date', 'created_at', 'updated_at')
        }),
    )
