from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User
from .models import PasswordResetToken


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password_confirm = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'password_confirm')
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError("Passwords don't match")
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 
                'profile_picture', 'date_joined', 'is_verified')
        read_only_fields = ('id', 'date_joined', 'is_verified')



User = User

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        
        if not email or not password:
            raise serializers.ValidationError({'detail': 'Enter email and password'})
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({'detail': 'Wrong email or password'})
        
        if not user.is_verified:
            raise serializers.ValidationError({'detail': 'Email is not verified. Please check your inbox.'})
        
        if not user.check_password(password):
            raise serializers.ValidationError({'detail': 'Wrong email or password'})
        
        attrs['user'] = user
        return attrs









class RequestPasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, attrs):
        email = attrs.get("email")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({"detail": "No user with this email"})

        attrs["user"] = user
        return attrs


class SetNewPasswordSerializer(serializers.Serializer):
    token = serializers.UUIDField()
    new_password = serializers.CharField()

    def validate(self, attrs):
        token = attrs.get("token")
        new_password = attrs.get("new_password")

        try:
            reset_token = PasswordResetToken.objects.get(token=token)
        except PasswordResetToken.DoesNotExist:
            raise serializers.ValidationError({"detail": "Invalid or expired token"})

        # Check expiry
        if reset_token.is_expired():
            reset_token.delete()
            raise serializers.ValidationError({"detail": "Token expired"})

        # Set new password
        user = reset_token.user
        user.set_password(new_password)
        user.save()

        # Delete token after use
        reset_token.delete()

        return attrs