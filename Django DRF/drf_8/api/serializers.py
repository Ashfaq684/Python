from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    # Validators
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name should be start with R')
    
    name = serializers.CharField(validators=[start_with_r])
    
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
    
    # Field level Validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        
        return value
    
    # Object level validation
    def validate(self, data):
        name = data.get('name')
        city = data.get('city')
        if name.lower() == 'ratul' and city.lower() != 'dhaka':
            raise serializers.ValidationError('City must be Dhaka')
        
        return data
