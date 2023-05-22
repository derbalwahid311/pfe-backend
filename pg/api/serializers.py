from django.forms import ValidationError
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from main.models import Enseignant 

class EnseignantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Enseignant 
        fields = "__all__"

class EnseignantLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def check_user(self, clean_data):
        user = authenticate(username=clean_data['username'], password=clean_data['password'])
        if not user:
            raise ValidationError("user not found")
        return user