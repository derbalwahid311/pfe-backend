from rest_framework import serializers
from main.models import Enseignant 

class Enseignanatserializers(serializers.ModelSerializer):
    class Meta:
        model=Enseignant 
        fields = "__all__"