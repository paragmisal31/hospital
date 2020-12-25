from allauth.account.adapter import get_adapter
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'is_doctor', 'is_patient')


class CustomRegisterSerializer(RegisterSerializer):
    is_patient = serializers.BooleanField()
    is_doctor = serializers.BooleanField()

    class Meta:
        model = User
        fields = ('username', 'password', 'is_doctor', 'is_patient')

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            
            'is_doctor': self.validated_data.get('is_doctor', ''),
            'is_patient': self.validated_data.get('is_patient', '')
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.is_doctor = self.cleaned_data.get('is_doctor')
        user.is_patient = self.cleaned_data.get('is_patient')
        user.save()
        adapter.save_user(request, user, self)
        return user


class TokenSerializer(serializers.ModelSerializer):
    user_type = serializers.SerializerMethodField()

    class Meta:
        model = Token
        fields = ('key', 'user', 'user_type')

    def get_user_type(self, obj):
        serializer_data = UserSerializer(
            obj.user
        ).data
        is_doctor = serializer_data.get('is_doctor')
        is_patient = serializer_data.get('is_patient')
        return {
            'is_doctor': is_doctor,
            'is_patient': is_patient
        }
