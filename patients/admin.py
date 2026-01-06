from django.contrib import admin
from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    """Admin configuration for Patient model."""
    
    list_display = ['name', 'age', 'gender', 'phone', 'user', 'created_at']
    list_filter = ['gender', 'created_at', 'user']
    search_fields = ['name', 'phone', 'user__email']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Patient Information', {
            'fields': ('name', 'age', 'gender', 'phone', 'address')
        }),
        ('Medical Information', {
            'fields': ('medical_history',)
        }),
        ('User Information', {
            'fields': ('user',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )
