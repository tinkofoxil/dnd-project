from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Profile
from .serializer import ProfileSerializer


class ProfileAPIList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileAPIUpdate(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
