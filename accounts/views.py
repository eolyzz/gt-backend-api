from django.shortcuts import render


# Create your views here.

from rest_framework import viewsets
from .serializers import UserCreateSerializer
from .models import UserAccount

class UserAccountViewSet(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserCreateSerializer
