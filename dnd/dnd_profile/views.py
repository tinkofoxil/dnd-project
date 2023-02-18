from rest_framework import generics

from .models import Profile
from .serializer import ProfileSerializer


class ProfileAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
