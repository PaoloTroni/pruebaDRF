from apps.category.serializers import CategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Category
from rest_framework.pagination import PageNumberPagination


class ListCategoriesView(APIView):
    def get(self, request, format=None):
        if Category.objects.all().exists():
           # CÓDIGO NUEVO USANDO EL SERIALIZADOR
           categories = Category.objects        
           serializer = CategorySerializer(categories, many=True)
           return Response({'categories': serializer.data}, status=status.HTTP_200_OK)
        
        #>>>> DEJE EL CODIGO ANTERIOR AQUÍ PARA COMPARACIÓN <<<<#
           """        
           
           categories = Category.objects.all()

           result = []

           for category in categories:
                if not category.parent:
                    item = {}
                    item['id'] = category.id
                    item['name'] = category.name
                    item['thumbnail'] = category.thumbnail.url
                    item['description'] = category.description

                    item['sub_categories'] = []

                    for cat in categories:
                        sub_item = {}
                        if cat.parent and cat.parent.id == category.id:
                            sub_item['id'] = cat.id
                            sub_item['name'] = cat.name
                            sub_item['thumbnail'] = cat.thumbnail.url
                            sub_item['description'] = category.description

                            item['sub_categories'].append(sub_item)

                    result.append(item)
                    
           return Response({'categories': result}, status=status.HTTP_200_OK)"""
        else:
            return Response({'error': 'No categories found'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class CreateNewCategory(APIView):
    def post(self, request, format=None):

        data = {
            'name': request.data.get('name'),
            'description': request.data.get('description')
        }
        print("Request Data: ", request.data) 

        serializer = CategorySerializer(data=data)

        if serializer.is_valid():
          
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)