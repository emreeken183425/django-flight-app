from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import RegiterSerializer


class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=RegiterSerializer
