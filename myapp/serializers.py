from django.urls import path, include
from myapp.models import Company,reg_user
from django.contrib.auth import get_user_model
from rest_framework import routers, serializers, viewsets
User=get_user_model()
# Serializers define the API representation.
class UserRegister(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=User
        fields=["username","password","email","password2"]
    def save(self):
        reg=User(email=self.validated_data['email'],
                 username=self.validated_data['username'])
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password!=password2:
            raise serializers.ValidationError({'password':'password does not match'})
        reg.set_password(password)
        reg.save()
        return reg
    
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = reg_user
        fields = "__all__"
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
