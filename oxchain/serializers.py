from rest_framework import serializers
from .models import User, CryptoData
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    referral = serializers.CharField(required=False, allow_blank=True)
    password2 = serializers.CharField(write_only=True)  # Added for password confirmation

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'password2', 'nationality', 'wallet', 'referral')
        extra_kwargs = {
            'referral': {'required': False},
            'wallet': {'required': False}
        }

    def validate(self, attrs):
      password = attrs.get('password')
      password2 = attrs.get('password2')

      if password and password2 and password != password2:
          raise serializers.ValidationError({"password": "Password fields didn't match."})

      return attrs

    def create(self, validated_data):
        referral_value = validated_data.get('referral', None)
        wallet_value = validated_data.get('wallet', None)

        user = User.objects.create(
            email=validated_data['email'],
            nationality=validated_data['nationality'],
            referral=referral_value,
            wallet=wallet_value
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.nationality = validated_data.get('nationality', instance.nationality)
        instance.referral = validated_data.get('referral', instance.referral)
        instance.wallet = validated_data.get('wallet', instance.wallet)

        # Check if the 'password' field is provided and update it accordingly
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)

        instance.save()
        return instance
    
class DataSerializer( serializers.ModelSerializer):
    class Meta:
        model = CryptoData
        fields = '__all__'  
