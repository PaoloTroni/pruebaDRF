from apps.category.serializers import CategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category

class ListCategoriesView(APIView):
    def get(self, request, format=None):
        categories = Category.objects.filter(parent__isnull=True)
   
        if not categories.exists():      
           return Response({'categories': [], 'message': 'No categories found'}, status=status.HTTP_200_OK)  
          
        serializer = CategorySerializer(categories, many=True)
        return Response({'categories': serializer.data}, status=status.HTTP_200_OK)

class CreateNewCategory(APIView):
    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():          
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)