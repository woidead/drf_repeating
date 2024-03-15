from rest_framework import generics
from .models import Celebrity, Category


class CelebrityAPIView(generics.ListAPIView):
    queryset = Celebrity.objects.all()
    serializer_class = CelebritySerilizer
    