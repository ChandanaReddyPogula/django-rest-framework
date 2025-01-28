from rest_framework import serializers
from accounts.models import User

class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50, min_length=8, write_only=True)
    username = serializers.CharField(max_length=45)
    email = serializers.EmailField(max_length=80)

    class Meta:
        model = User
        fields = ["username", "email", "password"]
    
    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'Email is already in use'})
        return attrs