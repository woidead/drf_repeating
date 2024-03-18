from .models import Celebrity, Category
from .serializers import CelebritySerializer
from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

# class CelebrityAPIView(generics.ListAPIView):
#     queryset = Celebrity.objects.all()
#     serializer_class = CelebritySerializer

class CelebrityAPIView(APIView):
    def get(self, request):
        data = Celebrity.objects.all().values()
        return Response({'data': list(data)})
    
    def post(self, request):
        celeba = Celebrity.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            category_id=request.data['category_id']
        )
        return Response({"data":model_to_dict(celeba)})