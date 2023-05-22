from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EnseignantLoginSerializer, EnseignantSerializer
from rest_framework import permissions, status
from .validations import custom_validation, validate_username, validate_password
from django.shortcuts import render
from rest_framework import generics
from main.models import Enseignant 
from django.contrib.auth.models import User

# Create your views here.

class EnAPIView(generics.ListAPIView):
    queryset = Enseignant.objects.all()
    serializer_class = EnseignantSerializer


class EnseignantLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentification_classes = (SessionAuthentication,)

    def post(self, request):
        data = request.data
        assert validate_username(data)
        assert validate_password(data)
        serializer = EnseignantLoginSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(data)
            usr = User.objects.get(username=data['username'])
            print(usr.enseignant.nom)

            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)


class EnseignantLogout(APIView):
    permission_classes = (permissions.AllowAny,)
    authentification_classes = ()
    
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)

class EngseignantView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentification_clases = (SessionAuthentication,)

    def get(self, request):
        # serializer = EnseignantSerializer(request.user)
        fields = request.user.enseignant.__dict__
        
        # print(fields)
        return Response({'enseignant': {"ID Enseignant": fields['id'], "Nom": fields['nom'], "Prenom": fields['prenom']}}, status=status.HTTP_200_OK)