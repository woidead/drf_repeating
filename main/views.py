from rest_framework import generics
from .models import Celebrity, Category
from .serializers import CelebritySerializer


class CelebrityAPIView(generics.ListAPIView):
    queryset = Celebrity.objects.all()
    serializer_class = CelebritySerializer
    