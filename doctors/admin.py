from django.contrib import admin
from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    """Admin configuration for Doctor model."""
    
    list_display = ['name', 'specialization', 'phone', 'email', 'experience_years', 'created_at']
    list_filter = ['specialization', 'created_at']
    search_fields = ['name', 'phone', 'email', 'specialization']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Doctor Information', {
            'fields': ('name', 'specialization', 'phone', 'email')
        }),
        ('Professional Details', {
            'fields': ('qualification', 'experience_years', 'address')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )
