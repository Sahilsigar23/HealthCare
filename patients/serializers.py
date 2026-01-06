from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    """Serializer for Patient model."""
    
    user_name = serializers.CharField(source='user.name', read_only=True)
    user_email = serializers.CharField(source='user.email', read_only=True)
    
    class Meta:
        model = Patient
        fields = [
            'id', 'name', 'age', 'gender', 'phone', 'address',
            'medical_history', 'user', 'user_name', 'user_email',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']
    
    def validate_age(self, value):
        """Validate age is positive."""
        if value < 0 or value > 150:
            raise serializers.ValidationError("Age must be between 0 and 150.")
        return value
    
    def validate_phone(self, value):
        """Validate phone number."""
        if len(value) < 10:
            raise serializers.ValidationError("Phone number must be at least 10 characters.")
        return value
