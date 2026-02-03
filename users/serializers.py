from rest_framework import serializers
from .models import User
from .services import hash_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    
    class Meta:
        model = User
        fields = ('first_name', 'middle_name', 'last_name', 'email', 'password_hash', 'is_active', 'created_at', 'updated_at')
        read_only_fields = ('is_active', 'created_at', 'updated_at')

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data['password_hash'] = hash_password(password)
        user = User.objects.create(**validated_data)
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.password_hash = hash_password(password)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance