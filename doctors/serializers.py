from rest_framework import serializers
from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    """Serializer for Doctor model."""
    
    class Meta:
        model = Doctor
        fields = [
            'id', 'name', 'specialization', 'phone', 'email',
            'experience_years', 'qualification', 'address',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def validate_experience_years(self, value):
        """Validate experience years is positive."""
        if value < 0 or value > 70:
            raise serializers.ValidationError("Experience years must be between 0 and 70.")
        return value
    
    def validate_phone(self, value):
        """Validate phone number."""
        if len(value) < 10:
            raise serializers.ValidationError("Phone number must be at least 10 characters.")
        return value
    
    def validate_email(self, value):
        """Validate email uniqueness for create operation."""
        if self.instance is None:  # Creating new doctor
            if Doctor.objects.filter(email=value).exists():
                raise serializers.ValidationError("A doctor with this email already exists.")
        else:  # Updating existing doctor
            if Doctor.objects.filter(email=value).exclude(id=self.instance.id).exists():
                raise serializers.ValidationError("A doctor with this email already exists.")
        return value
